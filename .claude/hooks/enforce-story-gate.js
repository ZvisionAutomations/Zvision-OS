#!/usr/bin/env node
/**
 * SINAPSE Story Gate Hook
 * Bloqueia implementação sem spec aprovada
 * Artigo III da Constitution — NON-NEGOTIABLE
 */

const input = JSON.parse(process.argv[2] || '{}');
const toolName = input.tool_name || '';
const toolInput = input.tool_input || {};

// Ferramentas que modificam código
const CODE_TOOLS = ['Write', 'Edit', 'MultiEdit', 'Bash'];

// Palavras que indicam implementação (não planejamento)
const IMPL_KEYWORDS = [
  'implement', 'implementa', 'criar', 'create', 'adicionar', 'add',
  'desenvolver', 'develop', 'build', 'construir', 'codificar'
];

// Palavras que indicam que spec já foi aprovada
const SPEC_MARKERS = [
  'spec-', 'story-', 'spec aprovada', 'story validada',
  '/pwf-work-plan', '/work-plan', 'phase', 'fase'
];

if (CODE_TOOLS.includes(toolName)) {
  const context = JSON.stringify(toolInput).toLowerCase();
  const hasImplIntent = IMPL_KEYWORDS.some(kw => context.includes(kw));
  const hasSpec = SPEC_MARKERS.some(marker => context.includes(marker));

  if (hasImplIntent && !hasSpec) {
    console.error(JSON.stringify({
      decision: 'block',
      reason: '⛔ STORY GATE ATIVO — Artigo III da Constitution\n' +
              'Nenhum código pode ser escrito sem spec aprovada.\n\n' +
              'Fluxo obrigatório:\n' +
              '1. /pwf-brainstorm — define a ideia e constraints\n' +
              '2. /pwf-plan — converte em fases executáveis\n' +
              '3. @product-lead *validate — valida a story\n' +
              '4. /pwf-work-plan — executa uma fase por vez\n\n' +
              'Comece com: /pwf-brainstorm'
    }));
    process.exit(1);
  }
}

// Permite continuar
console.log(JSON.stringify({ decision: 'allow' }));
process.exit(0);
