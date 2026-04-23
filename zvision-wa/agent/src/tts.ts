import { execFile } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';

const execFileAsync = promisify(execFile);

const TTS_ENABLED = process.env.TTS_ENABLED === 'true';
const TTS_VOICE = process.env.TTS_VOICE ?? 'pt-BR-FranciscaNeural';

export async function textToSpeech(text: string): Promise<string | null> {
  if (!TTS_ENABLED) return null;
  const cleaned = cleanForTTS(text);
  if (!cleaned) return null;

  const stamp = Date.now();
  const tmpMp3 = path.join(os.tmpdir(), `tts-${stamp}.mp3`);
  const tmpOgg = path.join(os.tmpdir(), `tts-${stamp}.ogg`);

  try {
    await execFileAsync('edge-tts', [
      '--voice', TTS_VOICE,
      '--text', cleaned,
      '--write-media', tmpMp3,
    ], { timeout: 15_000 });

    // Converte MP3 → OGG Opus (formato obrigatório para voz no WhatsApp)
    await execFileAsync('ffmpeg', [
      '-y', '-i', tmpMp3,
      '-c:a', 'libopus', '-b:a', '32k', '-vbr', 'on',
      tmpOgg,
    ], { timeout: 10_000 });

    return fs.readFileSync(tmpOgg).toString('base64');
  } catch (err) {
    console.error('[tts] Falha ao gerar áudio:', err);
    return null;
  } finally {
    for (const f of [tmpMp3, tmpOgg]) {
      try { if (fs.existsSync(f)) fs.unlinkSync(f); } catch { /* ignore */ }
    }
  }
}

// Remove markdown e emojis antes de sintetizar
function cleanForTTS(text: string): string {
  return text
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/_([^_]+)_/g, '$1')
    .replace(/[\u{1F300}-\u{1FFFF}\u{2600}-\u{27BF}]/gu, '')
    .replace(/\s+/g, ' ')
    .trim();
}
