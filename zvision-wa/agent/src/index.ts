import express, { Request, Response } from 'express';
import axios from 'axios';
import { healthRouter } from './health';
import { EvolutionClient } from './evolution-client';
import { handleMessage, initiateOutbound } from './handler';
import { transcribeAudio } from './audio';

const PORT = Number(process.env.PORT ?? 3400);
const EVOLUTION_BASE_URL = process.env.EVOLUTION_BASE_URL ?? 'http://evolution:8080';
const EVOLUTION_API_KEY = process.env.EVOLUTION_API_KEY ?? '';
const EVOLUTION_INSTANCE_NAME = process.env.EVOLUTION_INSTANCE_NAME ?? 'zvision-sdr';

const evolution = new EvolutionClient(EVOLUTION_BASE_URL, EVOLUTION_API_KEY, EVOLUTION_INSTANCE_NAME);

let lastQR: string | null = null;

const app = express();
app.use(express.json({ limit: '50mb' })); // mídia base64 pode ser grande
app.use(healthRouter);

// ─── Webhook principal ────────────────────────────────────────────────────────

app.post('/webhook', (req: Request, res: Response) => {
  const body = req.body as Record<string, unknown>;
  const event = (body.event as string | undefined) ?? '';

  if (event === 'QRCODE_UPDATED') {
    const data = body.data as { qrcode?: { base64?: string } } | undefined;
    lastQR = data?.qrcode?.base64 ?? null;
    console.log('[webhook] QR code atualizado.');
    res.sendStatus(200);
    return;
  }

  if (event === 'messages.upsert' || event === 'MESSAGES_UPSERT') {
    const data = body.data as Record<string, unknown> | undefined;

    if (!data) { res.sendStatus(200); return; }

    const key = data.key as { remoteJid?: string; fromMe?: boolean } | undefined;

    // Ignorar mensagens enviadas por nós
    if (key?.fromMe === true) { res.sendStatus(200); return; }

    const remoteJid = (key?.remoteJid as string) ?? '';

    // Ignorar grupos
    if (remoteJid.includes('@g.us')) { res.sendStatus(200); return; }

    // ID limpo = só dígitos (chave do lead)
    const from = remoteJid.replace(/@.+$/, '');
    const senderName = (data.pushName as string) ?? from;
    const messageType = (data.messageType as string) ?? '';
    const message = data.message as Record<string, unknown> | undefined;
    const mediaBase64 = (data.base64 as string | undefined) ?? '';

    // Responde 200 imediatamente — processamento é async
    res.sendStatus(200);

    if (!from) return;

    (async () => {
      try {
        // ── Áudio ───────────────────────────────────────────────────────────
        if (messageType === 'audioMessage') {
          if (!mediaBase64) {
            await evolution.sendText(remoteJid, 'Recebi seu áudio! Adicione a chave GROQ_API_KEY para eu transcrever, ou me escreva o que precisa. 😊');
            return;
          }
          const transcribed = await transcribeAudio(mediaBase64);
          if (!transcribed) {
            await evolution.sendText(remoteJid, 'Recebi seu áudio, mas não consegui transcrever agora. Pode me escrever? 😊');
            return;
          }
          console.log(`[webhook] Áudio transcrito de ${from}: "${transcribed.slice(0, 60)}"`);
          await handleMessage({ from, remoteJid, text: transcribed, senderName }, evolution);
          return;
        }

        // ── Imagem ──────────────────────────────────────────────────────────
        if (messageType === 'imageMessage') {
          const imgMsg = message?.imageMessage as Record<string, unknown> | undefined;
          const caption = (imgMsg?.caption as string) ?? '';
          const mime = ((imgMsg?.mimetype as string) ?? 'image/jpeg').split(';')[0];
          await handleMessage({
            from, remoteJid,
            text: caption || '[imagem]',
            senderName,
            mediaBase64: mediaBase64 || undefined,
            mediaMime: mime,
          }, evolution);
          return;
        }

        // ── Sticker ─────────────────────────────────────────────────────────
        if (messageType === 'stickerMessage') {
          await handleMessage({ from, remoteJid, text: '[sticker]', senderName }, evolution);
          return;
        }

        // ── Vídeo / Documento ───────────────────────────────────────────────
        if (messageType === 'videoMessage' || messageType === 'documentMessage') {
          await evolution.sendText(remoteJid, 'Recebi seu arquivo! Processo texto, áudio e imagens — pode me descrever o que precisa? 😊');
          return;
        }

        // ── Texto padrão ────────────────────────────────────────────────────
        const text =
          (message?.conversation as string) ??
          ((message?.extendedTextMessage as Record<string, unknown>)?.text as string) ??
          '';

        if (!text.trim()) return;

        await handleMessage({ from, remoteJid, text, senderName }, evolution);

      } catch (err) {
        console.error('[webhook] Erro ao processar mensagem:', err);
      }
    })();

    return;
  }

  res.sendStatus(200);
});

// ─── QR Code ──────────────────────────────────────────────────────────────────

app.get('/qrcode', (_req: Request, res: Response) => {
  if (lastQR === null) {
    res.status(404).json({ error: 'QR code não disponível ainda.' });
    return;
  }
  res.json({ qrcode: lastQR });
});

// ─── Outbound: Vitor inicia conversa com um lead ──────────────────────────────

app.post('/outbound', async (req: Request, res: Response) => {
  const { phone, businessName } = req.body as { phone?: string; businessName?: string };

  if (!phone || !businessName) {
    res.status(400).json({ error: 'Campos obrigatórios: phone, businessName' });
    return;
  }

  try {
    await initiateOutbound(phone, businessName, evolution);
    res.json({ ok: true, message: `Vitor iniciou com ${businessName} (${phone})` });
  } catch (err) {
    console.error('[outbound] Erro:', err);
    res.status(500).json({ error: 'Erro ao iniciar conversa' });
  }
});

// ─── Outbound bulk: lista de leads ────────────────────────────────────────────

app.post('/outbound/bulk', (req: Request, res: Response) => {
  const { leads } = req.body as {
    leads?: { phone: string; businessName: string }[];
  };

  if (!leads?.length) {
    res.status(400).json({ error: 'Campo obrigatório: leads (array)' });
    return;
  }

  res.json({ ok: true, message: `Processando ${leads.length} leads em background...` });

  (async () => {
    for (const lead of leads) {
      try {
        await initiateOutbound(lead.phone, lead.businessName, evolution);
        await sleep(2500);
      } catch (err) {
        console.error(`[bulk] Erro para ${lead.phone}:`, err);
      }
    }
    console.log(`[bulk] Concluído: ${leads.length} leads processados`);
  })().catch((err: unknown) => console.error('[bulk] Erro geral:', err));
});

// ─── Init ─────────────────────────────────────────────────────────────────────

async function createInstance(): Promise<void> {
  try {
    await axios.post(
      `${EVOLUTION_BASE_URL}/instance/create`,
      { instanceName: EVOLUTION_INSTANCE_NAME, qrcode: true, integration: 'WHATSAPP-BAILEYS' },
      { headers: { apikey: EVOLUTION_API_KEY } },
    );
    console.log(`[init] Instância "${EVOLUTION_INSTANCE_NAME}" criada.`);
  } catch (err) {
    if (axios.isAxiosError(err)) {
      const status = err.response?.status;
      if (status === 400 || status === 403 || status === 409) {
        console.log('[init] Instância já existe, continuando...');
        return;
      }
    }
    console.error('[init] Erro ao criar instância:', toMessage(err));
    throw err;
  }
}

async function registerWebhook(): Promise<void> {
  try {
    await axios.post(
      `${EVOLUTION_BASE_URL}/webhook/set/${EVOLUTION_INSTANCE_NAME}`,
      {
        webhook: {
          enabled: true,
          url: `http://agent:${PORT}/webhook`,
          webhook_by_events: false,
          webhook_base64: true, // recebe mídia (áudio/imagem) como base64 no payload
          events: ['MESSAGES_UPSERT', 'CONNECTION_UPDATE', 'QRCODE_UPDATED'],
        },
      },
      { headers: { apikey: EVOLUTION_API_KEY } },
    );
    console.log('[init] Webhook registrado com sucesso.');
  } catch (err) {
    console.error('[init] Erro ao registrar webhook:', toMessage(err));
    throw err;
  }
}

async function bootstrap(): Promise<void> {
  await new Promise<void>((resolve) => {
    app.listen(PORT, () => {
      console.log(`[server] Zvision Agent rodando na porta ${PORT}`);
      resolve();
    });
  });

  try {
    await createInstance();
    await registerWebhook();
  } catch (err) {
    console.error('[fatal] Falha na inicialização com Evolution:', toMessage(err));
    process.exit(1);
  }
}

bootstrap();

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function toMessage(err: unknown): string {
  if (err instanceof Error) return err.message;
  return String(err);
}
