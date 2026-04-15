import axios from 'axios';
import type { ChatMessage } from './memory';

const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY ?? '';
const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';

// Modelos com fallback em ordem de preferência (IDs validados via API OpenRouter)
// Vision-capable: gemma-4-31b, gemma-4-26b-a4b
// Text-only: llama-3.3-70b, nemotron-120b, nemotron-30b, arcee, minimax
const MODELS = [
  'google/gemma-4-31b-it:free',
  'google/gemma-4-26b-a4b-it:free',
  'meta-llama/llama-3.3-70b-instruct:free',
  'nvidia/nemotron-3-super-120b-a12b:free',
  'nvidia/nemotron-3-nano-30b-a3b:free',
  'arcee-ai/trinity-large-preview:free',
  'minimax/minimax-m2.5:free',
];

const VISION_MODELS = new Set([
  'google/gemma-4-31b-it:free',
  'google/gemma-4-26b-a4b-it:free',
]);

export async function askGemini(
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

  // Quando há imagem, prioriza vision models no início da lista
  const models = imageBase64
    ? [...MODELS].sort((a, b) =>
        VISION_MODELS.has(b) && !VISION_MODELS.has(a) ? 1 : 0,
      )
    : MODELS;

  for (const model of models) {
    // Modelos text-only não conseguem processar imagens — pula para o próximo vision
    if (imageBase64 && !VISION_MODELS.has(model)) continue;

    const messages = buildMessages(systemPrompt, history, imageBase64, imageMime);

    try {
      const { data } = await axios.post(
        OPENROUTER_URL,
        { model, messages, temperature: 0.65, max_tokens: 300, top_p: 0.9 },
        { headers, timeout: 30_000 },
      );

      const text = data?.choices?.[0]?.message?.content as string | undefined;
      if (!text) throw new Error('resposta vazia');
      console.log(`[llm] respondeu via ${model}`);
      return text.trim();

    } catch (err) {
      const status = axios.isAxiosError(err) ? err.response?.status : null;
      const rawMsg = JSON.stringify(axios.isAxiosError(err) ? err.response?.data : err);

      if (status === 429 || status === 503) {
        console.warn(`[llm] ${model} → ${status} (rate limit), tentando próximo em 5s...`);
        await sleep(5_000);
        continue;
      }

      if (status === 404) {
        console.warn(`[llm] ${model} → 404 (indisponível), pulando...`);
        continue;
      }

      if (status === 400 && rawMsg.includes('instruction is not enabled')) {
        console.warn(`[llm] ${model} → não suporta system prompt, pulando...`);
        continue;
      }

      const msg = axios.isAxiosError(err)
        ? `HTTP ${err.response?.status} — ${rawMsg}`
        : String(err);
      throw new Error(`LLM error (${model}): ${msg}`);
    }
  }

  throw new Error('LLM: todos os modelos falharam');
}

function buildMessages(
  systemPrompt: string,
  history: ChatMessage[],
  imageBase64?: string,
  imageMime?: string,
): unknown[] {
  const msgs: unknown[] = [{ role: 'system', content: systemPrompt }];

  const histMsgs = history.map((m, i) => {
    const role = m.role === 'model' ? 'assistant' : 'user';

    // Injeta imagem na última mensagem do usuário
    if (imageBase64 && role === 'user' && i === history.length - 1) {
      return {
        role,
        content: [
          { type: 'text', text: m.content || '[imagem]' },
          {
            type: 'image_url',
            image_url: {
              url: `data:${imageMime ?? 'image/jpeg'};base64,${imageBase64}`,
            },
          },
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
