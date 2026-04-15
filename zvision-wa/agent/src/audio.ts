const GROQ_API_KEY = process.env.GROQ_API_KEY ?? '';
const GROQ_WHISPER_URL = 'https://api.groq.com/openai/v1/audio/transcriptions';

/**
 * Transcreve áudio base64 (OGG/Opus do WhatsApp) usando Groq Whisper.
 * Retorna null se a chave não estiver configurada ou a transcrição falhar.
 *
 * Nota: Groq Whisper é apenas transcrição de áudio — não é o modelo de chat.
 * Plano gratuito: até 2 horas de áudio por dia.
 */
export async function transcribeAudio(base64Audio: string): Promise<string | null> {
  if (!GROQ_API_KEY) {
    console.warn('[audio] GROQ_API_KEY não configurada — transcrição indisponível');
    return null;
  }

  try {
    const buffer = Buffer.from(base64Audio, 'base64');
    const form = new FormData();
    form.append('file', new Blob([buffer], { type: 'audio/ogg' }), 'audio.ogg');
    form.append('model', 'whisper-large-v3-turbo');
    form.append('language', 'pt');
    form.append('response_format', 'text');

    const res = await fetch(GROQ_WHISPER_URL, {
      method: 'POST',
      headers: { Authorization: `Bearer ${GROQ_API_KEY}` },
      body: form,
    });

    if (!res.ok) {
      const errorText = await res.text();
      console.error(`[audio] Groq Whisper erro ${res.status}: ${errorText}`);
      return null;
    }

    // response_format=text retorna texto puro
    const text = await res.text();
    const transcribed = text.trim();
    if (transcribed) {
      console.log(`[audio] Transcrito: "${transcribed.slice(0, 60)}..."`);
    }
    return transcribed || null;

  } catch (err) {
    console.error('[audio] Erro na transcrição:', err instanceof Error ? err.message : err);
    return null;
  }
}
