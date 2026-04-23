import { getLead, saveLead, createLead } from './memory';
import type { Lead } from './memory';
import { askGemini } from './gemini';
import { VITOR_PROMPT, ANA_PROMPT } from './prompts';
import { EvolutionClient } from './evolution-client';

const CLOSER_PHONE = process.env.CLOSER_PHONE ?? '';
const MAX_MESSAGES = 20;

export interface IncomingMessage {
  from: string;        // ID limpo (só dígitos) — chave do lead
  remoteJid: string;   // JID completo (@s.whatsapp.net ou @lid) — usado para envio
  text: string;        // texto ou transcrição de áudio
  senderName: string;
  mediaBase64?: string; // base64 de imagem (quando enviada pelo lead)
  mediaMime?: string;   // 'image/jpeg', 'image/png', etc.
}

// ─── Entrada principal: mensagem recebida ────────────────────────────────────

export async function handleMessage(
  msg: IncomingMessage,
  evolution: EvolutionClient,
): Promise<void> {
  const { from, remoteJid, text, senderName, mediaBase64, mediaMime } = msg;

  if (!text.trim() && !mediaBase64) return;

  let lead = getLead(from);

  // Lead desconhecido mensagando diretamente → Ana assume (inbound)
  if (!lead) {
    lead = createLead(from, senderName, 'ANA_ACTIVE');
    console.log(`[handler] Novo lead inbound: ${senderName} (${from})`);
  }

  // Conversa já encerrada — ignorar
  if (lead.state === 'NOT_QUALIFIED' || lead.state === 'HUMAN_HANDOFF') {
    console.log(`[handler] Lead ${from} ignorado (estado: ${lead.state})`);
    return;
  }

  // Limite de segurança
  if (lead.messageCount >= MAX_MESSAGES) {
    console.warn(`[handler] Lead ${from} atingiu limite de mensagens`);
    return;
  }

  // Detectar pedido de humano
  if (wantsHuman(text) && !lead.handoffSent) {
    await triggerHandoff(lead, from, remoteJid, evolution);
    return;
  }

  // Adicionar mensagem ao histórico
  const userContent = mediaBase64 ? `[imagem] ${text}`.trim() : text;
  lead.messages.push({ role: 'user', content: userContent });
  lead.messageCount++;

  const systemPrompt = lead.state === 'VITOR_ACTIVE' ? VITOR_PROMPT : ANA_PROMPT;

  let response: string;
  try {
    response = await askGemini(systemPrompt, lead.messages, mediaBase64, mediaMime);
    console.log(`[handler] Resposta gerada para ${from} (${lead.state})`);
  } catch (err) {
    console.error('[handler] Erro ao chamar LLM:', err);
    // Avisa o lead em vez de deixar em silêncio
    await evolution.sendText(remoteJid, 'Desculpe, estou com uma instabilidade técnica agora. Tente novamente em alguns segundos! 🙏');
    return;
  }

  processStateTransition(lead, response);

  if (isHandoffResponse(response) && !lead.handoffSent) {
    await triggerHandoff(lead, from, remoteJid, evolution);
    return;
  }

  lead.messages.push({ role: 'model', content: response });
  saveLead(lead);

  await evolution.sendText(remoteJid, response);
}

// ─── Saída: Vitor inicia conversa outbound ───────────────────────────────────

export async function initiateOutbound(
  phone: string,
  businessName: string,
  evolution: EvolutionClient,
): Promise<void> {
  const existing = getLead(phone);
  if (existing) {
    console.log(`[outbound] ${phone} já existe (estado: ${existing.state}) — ignorando`);
    return;
  }

  const lead = createLead(phone, businessName, 'VITOR_ACTIVE');

  const seedHistory = [
    {
      role: 'user' as const,
      content: `[SISTEMA] Inicie a prospecção com o responsável da empresa "${businessName}". Gere apenas a primeira mensagem de abertura.`,
    },
  ];

  let opening: string;
  try {
    opening = await askGemini(VITOR_PROMPT, seedHistory);
  } catch (err) {
    console.error(`[outbound] Erro ao gerar abertura para ${phone}:`, err);
    return;
  }

  lead.messages.push({ role: 'model', content: opening });
  lead.messageCount++;
  saveLead(lead);

  await evolution.sendText(phone, opening);
  console.log(`[outbound] Vitor iniciou com ${businessName} (${phone})`);
}

// ─── Handoff para humano ─────────────────────────────────────────────────────

async function triggerHandoff(
  lead: Lead,
  from: string,
  remoteJid: string,
  evolution: EvolutionClient,
): Promise<void> {
  await evolution.sendText(remoteJid, 'Deixa eu chamar nosso especialista, um segundo.');

  if (CLOSER_PHONE) {
    const pain = lead.pain ?? 'não identificada ainda';
    const summary = [
      `🔔 *Novo lead para você fechar*`,
      ``,
      `*Empresa/Contato:* ${lead.name}`,
      `*Número:* ${from}`,
      `*Dor revelada:* ${pain}`,
      `*Mensagens trocadas:* ${lead.messageCount}`,
      `*Estado anterior:* ${lead.state}`,
      ``,
      `Responda diretamente nesse número.`,
    ].join('\n');

    await evolution.sendText(CLOSER_PHONE, summary);
    console.log(`[handoff] Notificação enviada ao closer sobre ${lead.name}`);
  } else {
    console.warn('[handoff] CLOSER_PHONE não configurado — notificação não enviada');
  }

  lead.state = 'HUMAN_HANDOFF';
  lead.handoffSent = true;
  saveLead(lead);
}

// ─── Helpers ─────────────────────────────────────────────────────────────────

function wantsHuman(text: string): boolean {
  const triggers = [
    'quero falar com humano',
    'falar com atendente',
    'falar com pessoa',
    'falar com o miguel',
    'falar com alguém',
    'atendente humano',
    'pessoa real',
  ];
  const lower = text.toLowerCase();
  return triggers.some((t) => lower.includes(t));
}

function isHandoffResponse(response: string): boolean {
  return response.toLowerCase().includes('deixa eu chamar o miguel');
}

function processStateTransition(lead: Lead, response: string): void {
  const lower = response.toLowerCase();

  if (lead.state === 'VITOR_ACTIVE') {
    if (lower.includes('deixa eu te conectar com a ana')) {
      lead.state = 'ANA_ACTIVE';
      console.log(`[state] ${lead.id}: VITOR_ACTIVE → ANA_ACTIVE`);
      return;
    }
    if (lower.includes('obrigado pelo seu tempo') || lower.includes('se mudar, pode chamar')) {
      lead.state = 'NOT_QUALIFIED';
      console.log(`[state] ${lead.id}: VITOR_ACTIVE → NOT_QUALIFIED`);
      return;
    }
  }

  if (lead.state === 'ANA_ACTIVE') {
    if (lower.includes('cal.com/zvision-automations')) {
      lead.state = 'QUALIFIED';
      console.log(`[state] ${lead.id}: ANA_ACTIVE → QUALIFIED`);
      return;
    }
    if (lower.includes('obrigada pelo seu tempo') || lower.includes('se um dia fizer sentido')) {
      lead.state = 'NOT_QUALIFIED';
      console.log(`[state] ${lead.id}: ANA_ACTIVE → NOT_QUALIFIED`);
      return;
    }
    extractPain(lead, response);
  }
}

function extractPain(lead: Lead, response: string): void {
  if (!lead.pain && lead.messages.length >= 2) {
    const lastUserMsg = [...lead.messages].reverse().find((m) => m.role === 'user');
    if (lastUserMsg && lastUserMsg.content.length > 10) {
      lead.pain = lastUserMsg.content;
    }
  }
}
