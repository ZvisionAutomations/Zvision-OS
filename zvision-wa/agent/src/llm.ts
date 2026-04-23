import axios from 'axios';
import type { ChatMessage } from './memory';

// ─── Configuração de providers ────────────────────────────────────────────────

const GROQ_API_KEY       = process.env.GROQ_API_KEY      ?? '';
const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY ?? '';

const GROQ_URL       = 'https://api.groq.com/openai/v1/chat/completions';
const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';

// Groq — grátis, excelente instruction-following, 14.400 req/dia
const GROQ_MODELS = [
  'llama-3.3-70b-versatile',
  'llama-3.1-8b-instant',
];

// OpenRouter — fallback, único com vision (imagens)
const OPENROUTER_MODELS = [
  'google/gemma-4-31b-it:free',
  'google/gemma-4-26b-a4b-it:free',
  'meta-llama/llama-3.3-70b-instruct:free',
];

const VISION_MODELS_OR = new Set([
  'google/gemma-4-31b-it:free',
  'google/gemma-4-26b-a4b-it:free',
]);

// ─── Função principal ─────────────────────────────────────────────────────────

export async function askLLM(
  systemPrompt: string,
  history: ChatMessage[],
  imageBase64?: string,
  imageMime?: string,
): Promise<string> {
  // Com imagem → vai direto para OpenRouter (Groq não tem vision)
  if (imageBase64) {
    return callOpenRouter(systemPrompt, history, imageBase64, imageMime);
  }

  // Sem imagem → tenta Groq primeiro
  if (GROQ_API_KEY) {
    try {
      return await callGroq(systemPrompt, history);
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      console.warn(`[llm] Groq falhou (${msg}), caindo para OpenRouter...`);
    }
  }

  return callOpenRouter(systemPrompt, history);
}

// ─── Groq ─────────────────────────────────────────────────────────────────────

async function callGroq(
  systemPrompt: string,
  history: ChatMessage[],
): Promise<string> {
  if (!GROQ_API_KEY) throw new Error('GROQ_API_KEY não configurada');

  const messages = buildMessages(systemPrompt, history);
  const headers = {
    Authorization: `Bearer ${GROQ_API_KEY}`,
    'Content-Type': 'application/json',
  };

  for (const model of GROQ_MODELS) {
    try {
      const { data } = await axios.post(
        GROQ_URL,
        { model, messages, temperature: 0.65, max_tokens: 300, top_p: 0.9 },
        { headers, timeout: 30_000 },
      );
      const text = data?.choices?.[0]?.message?.content as string | undefined;
      if (!text) throw new Error('resposta vazia');
      console.log(`[llm] Groq/${model}`);
      return text.trim();
    } catch (err) {
      const status = axios.isAxiosError(err) ? err.response?.status : null;
      if (status === 429 || status === 503) {
        console.warn(`[llm] Groq/${model} → ${status}, próximo em 2s...`);
        await sleep(2_000);
        continue;
      }
      throw err;
    }
  }
  throw new Error('Groq: todos os modelos falharam');
}

// ─── OpenRouter ───────────────────────────────────────────────────────────────

async function callOpenRouter(
  systemPrompt: string,
  history: ChatMessage[],
  imageBase64?: string,
  imageMime?: string,
): Promise<string> {
  if (!OPENROUTER_API_KEY) throw new Error('OPENROUTER_API_KEY não configurada');

  const headers = {
    Authorization: `Bearer ${OPENROUTER_API_KEY}`,
    'Content-Type': 'application/json',
    'HTTP-Referer': 'https://github.com/ZvisionAutomations/Zvision-OS',
    'X-Title': 'Zvision Agents',
  };

  const models = imageBase64
    ? OPENROUTER_MODELS.filter((m) => VISION_MODELS_OR.has(m))
    : OPENROUTER_MODELS;

  for (const model of models) {
    const messages = buildMessages(systemPrompt, history, imageBase64, imageMime);
    try {
      const { data } = await axios.post(
        OPENROUTER_URL,
        { model, messages, temperature: 0.65, max_tokens: 300, top_p: 0.9 },
        { headers, timeout: 30_000 },
      );
      const text = data?.choices?.[0]?.message?.content as string | undefined;
      if (!text) throw new Error('resposta vazia');
      console.log(`[llm] OpenRouter/${model}`);
      return text.trim();
    } catch (err) {
      const status = axios.isAxiosError(err) ? err.response?.status : null;
      const raw = JSON.stringify(axios.isAxiosError(err) ? err.response?.data : err);
      if (status === 429 || status === 503) { await sleep(5_000); continue; }
      if (status === 404) { continue; }
      if (status === 400 && raw.includes('instruction is not enabled')) { continue; }
      throw new Error(`OpenRouter/${model}: HTTP ${status} — ${raw}`);
    }
  }
  throw new Error('OpenRouter: todos os modelos falharam');
}

// ─── Helpers ──────────────────────────────────────────────────────────────────

function buildMessages(
  systemPrompt: string,
  history: ChatMessage[],
  imageBase64?: string,
  imageMime?: string,
): unknown[] {
  const msgs: unknown[] = [{ role: 'system', content: systemPrompt }];
  const histMsgs = history.map((m, i) => {
    const role = m.role === 'model' ? 'assistant' : 'user';
    if (imageBase64 && role === 'user' && i === history.length - 1) {
      return {
        role,
        content: [
          { type: 'text', text: m.content || '[imagem]' },
          { type: 'image_url', image_url: { url: `data:${imageMime ?? 'image/jpeg'};base64,${imageBase64}` } },
        ],
      };
    }
    return { role, content: m.content };
  });
  return [...msgs, ...histMsgs];
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
