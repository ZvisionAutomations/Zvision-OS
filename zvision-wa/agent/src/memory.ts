import * as fs from 'fs';
import * as path from 'path';

export type LeadState =
  | 'VITOR_ACTIVE'    // Vitor prospectando (outbound)
  | 'ANA_ACTIVE'      // Ana qualificando
  | 'QUALIFIED'       // Link enviado, aguardando fechamento
  | 'NOT_QUALIFIED'   // Sem fit — encerrado
  | 'HUMAN_HANDOFF';  // Escalado para humano

export interface ChatMessage {
  role: 'user' | 'model';
  content: string;
}

export interface Lead {
  id: string;           // número de telefone (sem @s.whatsapp.net)
  name: string;         // nome da empresa ou contato
  state: LeadState;
  pain?: string;        // dor revelada pelo lead (extraída pela Ana)
  messageCount: number;
  messages: ChatMessage[];
  handoffSent: boolean;
  createdAt: string;
  updatedAt: string;
}

const DATA_DIR = process.env.DATA_DIR ?? '/data/leads';

function ensureDir(): void {
  if (!fs.existsSync(DATA_DIR)) {
    fs.mkdirSync(DATA_DIR, { recursive: true });
  }
}

function leadPath(id: string): string {
  const safe = id.replace(/[^a-zA-Z0-9]/g, '_');
  return path.join(DATA_DIR, `${safe}.json`);
}

export function getLead(id: string): Lead | null {
  ensureDir();
  const p = leadPath(id);
  if (!fs.existsSync(p)) return null;
  try {
    return JSON.parse(fs.readFileSync(p, 'utf-8')) as Lead;
  } catch {
    return null;
  }
}

export function saveLead(lead: Lead): void {
  ensureDir();
  lead.updatedAt = new Date().toISOString();
  fs.writeFileSync(leadPath(lead.id), JSON.stringify(lead, null, 2));
}

export function createLead(id: string, name: string, state: LeadState): Lead {
  const lead: Lead = {
    id,
    name,
    state,
    messageCount: 0,
    messages: [],
    handoffSent: false,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
  saveLead(lead);
  return lead;
}
