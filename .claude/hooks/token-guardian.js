#!/usr/bin/env node
/**
 * Token Guardian Hook
 * Artigo X — Security & Data Protection
 * Bloqueia commits com secrets hardcoded
 */

const input = JSON.parse(process.argv[2] || '{}');
const toolName = input.tool_name || '';
const toolInput = input.tool_input || {};

const SECRET_PATTERNS = [
  /SUPABASE_SERVICE_ROLE_KEY\s*=\s*['"]ey/i,
  /GEMINI_API_KEY\s*=\s*['"]AI/i,
  /ghp_[a-zA-Z0-9]{36}/,        // GitHub token
  /sk-ant-[a-zA-Z0-9-]{90,}/,   // Anthropic key
  /ip_sk_[a-zA-Z0-9]{20,}/,     // InsightfulPipe
];

if (['Write', 'Edit', 'MultiEdit'].includes(toolName)) {
  const content = JSON.stringify(toolInput);

  for (const pattern of SECRET_PATTERNS) {
    if (pattern.test(content)) {
      console.error(JSON.stringify({
        decision: 'block',
        reason: '⛔ TOKEN GUARDIAN — Artigo X da Constitution\n' +
                'Secret detectado no conteúdo do arquivo.\n' +
                'Use variáveis de ambiente (.env) — nunca hardcode secrets.\n' +
                'Adicione o arquivo ao .gitignore antes de continuar.'
      }));
      process.exit(1);
    }
  }
}

console.log(JSON.stringify({ decision: 'allow' }));
process.exit(0);
