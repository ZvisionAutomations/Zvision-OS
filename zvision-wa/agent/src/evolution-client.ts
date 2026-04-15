import axios, { AxiosInstance } from 'axios';

interface SendTextBody {
  number: string;
  text: string;
}

interface ConnectResponse {
  base64?: string;
  qrcode?: string;
  code?: string;
}

interface ConnectionStateResponse {
  instance?: {
    state?: string;
  };
  state?: string;
}

export class EvolutionClient {
  private readonly http: AxiosInstance;
  private readonly instanceName: string;

  constructor(baseUrl: string, apiKey: string, instanceName: string) {
    this.instanceName = instanceName;
    this.http = axios.create({
      baseURL: baseUrl,
      headers: { apikey: apiKey },
      timeout: 10_000,
    });
  }

  async sendText(number: string, text: string): Promise<void> {
    const body: SendTextBody = { number, text };

    try {
      await this.http.post(`/message/sendText/${this.instanceName}`, body);
    } catch (err) {
      console.error('[EvolutionClient] Erro ao enviar mensagem:', toMessage(err));
      throw err;
    }
  }

  async getQRCode(): Promise<string> {
    try {
      const { data } = await this.http.get<ConnectResponse>(
        `/instance/connect/${this.instanceName}`,
      );
      const qr = data.base64 ?? data.qrcode ?? data.code;
      if (!qr) throw new Error('QR code não retornado pela API');
      return qr;
    } catch (err) {
      console.error('[EvolutionClient] Erro ao obter QR code:', toMessage(err));
      throw err;
    }
  }

  async getConnectionState(): Promise<string> {
    try {
      const { data } = await this.http.get<ConnectionStateResponse>(
        `/instance/connectionState/${this.instanceName}`,
      );
      return data.instance?.state ?? data.state ?? 'unknown';
    } catch (err) {
      console.error('[EvolutionClient] Erro ao obter estado da conexão:', toMessage(err));
      throw err;
    }
  }
}

function toMessage(err: unknown): string {
  if (err instanceof Error) return err.message;
  return String(err);
}
