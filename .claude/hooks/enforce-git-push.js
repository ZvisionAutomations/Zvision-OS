#!/usr/bin/env node
/**
 * SINAPSE Git Push Authority Hook
 * Artigo IX — Safe Collaboration
 * Apenas Miguel (humano) ou @devops pode fazer push
 */

const input = JSON.parse(process.argv[2] || '{}');
const toolName = input.tool_name || '';
const toolInput = input.tool_input || {};

if (toolName === 'Bash') {
  const cmd = (toolInput.command || '').toLowerCase();

  if (cmd.includes('git push') && cmd.includes('--force')) {
    console.error(JSON.stringify({
      decision: 'block',
      reason: '⛔ FORCE PUSH BLOQUEADO — Artigo IX da Constitution\n' +
              'Force push requer aprovação explícita de Miguel.\n' +
              'Use git push sem --force ou solicite autorização.'
    }));
    process.exit(1);
  }
}

console.log(JSON.stringify({ decision: 'allow' }));
process.exit(0);
