// Bridge Zvision-OS v2.0
// Sistema nervoso central — roteamento inteligente entre squads e Claude Code
// Porta: 3333 | Zero dependências externas

'use strict';

const http = require('http');

const PORT = 3333;
const START_TIME = Date.now();

// ── SQUAD REGISTRY ──────────────────────────────────────────────────────────
// Extraído do squads/registry.yaml — keywords mapeadas para intent classifier

const SQUADS = [
  {
    id: 'squad-dev',
    name: 'Development Squad',
    invoke: null,
    description: 'Implementação, arquitetura, QA, DevOps',
    keywords: ['implementar', 'feature', 'código', 'bug', 'debug', 'refactor', 'migration', 'api', 'backend', 'frontend', 'component', 'função', 'classe', 'módulo', 'build', 'deploy', 'teste', 'test', 'develop', 'landing page', 'página', 'site', 'aplicação', 'app'],
  },
  {
    id: 'squad-cybersecurity',
    name: 'Cybersecurity Squad',
    invoke: '/cyber:agents:cyber-orqx',
    description: 'Segurança ofensiva e defensiva, pentest, compliance',
    keywords: ['segurança', 'security', 'audit', 'pentest', 'vulnerability', 'owasp', 'rls', 'compliance', 'hack', 'exploit', 'firewall', 'ssl', 'certificado', 'autenticação', 'autorização'],
  },
  {
    id: 'squad-copy',
    name: 'Copy Squad',
    invoke: '/copywriting:agents:copy-orqx',
    description: 'Copywriting persuasivo, headlines, conversão',
    keywords: ['copy', 'texto', 'headline', 'email', 'cta', 'persuasão', 'copywriting', 'escrita', 'mensagem', 'anúncio', 'script'],
  },
  {
    id: 'squad-design',
    name: 'Design Squad',
    invoke: '/digital-experience:agents:design-orqx',
    description: 'UI/UX, design systems, componentes, tokens',
    keywords: ['design', 'interface', 'ux', 'ui', 'componente', 'layout', 'visual', 'wireframe', 'protótipo', 'figma', 'design system', 'tokens', 'tipografia', 'cores', 'paleta'],
  },
  {
    id: 'squad-brand',
    name: 'Brand Squad',
    invoke: '/brand:agents:brand-orqx',
    description: 'Estratégia de marca, arquétipos, posicionamento',
    keywords: ['marca', 'branding', 'posicionamento', 'identidade', 'arquétipos', 'brand', 'logo', 'tom de voz', 'manifesto'],
  },
  {
    id: 'squad-paidmedia',
    name: 'Paid Media Squad',
    invoke: '/pm:agents:paidmedia-orqx',
    description: 'Tráfego pago, Meta Ads, Google Ads, otimização',
    keywords: ['tráfego', 'ads', 'campanha', 'meta', 'google', 'mídia paga', 'roi', 'facebook ads', 'google ads', 'instagram ads', 'criativos', 'cpm', 'cpc', 'roas'],
  },
  {
    id: 'squad-growth',
    name: 'Growth Squad',
    invoke: '/growth:agents:growth-orqx',
    description: 'Analytics, CRO, SEO, growth hacking',
    keywords: ['growth', 'cro', 'seo', 'analytics', 'conversão', 'funil', 'retenção', 'otimizar', 'taxa', 'bounce', 'tráfego orgânico', 'palavras-chave'],
  },
  {
    id: 'squad-research',
    name: 'Research Squad',
    invoke: '/research:agents:research-orqx',
    description: 'Market analysis, inteligência competitiva, analytics',
    keywords: ['dados', 'analytics', 'métricas', 'dashboard', 'relatório', 'kpi', 'pesquisa', 'mercado', 'competidor', 'benchmark', 'análise', 'estudo', 'survey'],
  },
  {
    id: 'squad-storytelling',
    name: 'Storytelling Squad',
    invoke: '/narrative:agents:storytelling-orqx',
    description: 'Narrativa, roteiros, frameworks de história',
    keywords: ['história', 'narrativa', 'storytelling', 'roteiro', 'pitch', 'apresentação', 'deck', 'keynote', 'story', 'jornada'],
  },
  {
    id: 'squad-commercial',
    name: 'Commercial Squad',
    invoke: '/commercial:agents:commercial-orqx',
    description: 'Pipeline comercial, ofertas, pricing, funil de vendas',
    keywords: ['oferta', 'pricing', 'venda', 'proposta', 'deal', 'receita', 'escala', 'pipeline', 'prospecção', 'lead', 'qualificação', 'comercial', 'cliente', 'contrato', 'negociação'],
  },
  {
    id: 'squad-council',
    name: 'Council / Advisory Board',
    invoke: '/council:agents:council-orqx',
    description: 'Conselheiros estratégicos (Dalio, Munger, Naval, Thiel, Reid Hoffman)',
    keywords: ['estratégia', 'decisão', 'investimento', 'risco', 'visão', 'longo prazo', 'conselho', 'advisory', 'mental model', 'framework estratégico'],
  },
  {
    id: 'squad-product',
    name: 'Product Squad',
    invoke: '/product:agents:product-orqx',
    description: 'Product discovery, roadmap, delivery, C-level virtual',
    keywords: ['executivo', 'ceo', 'cto', 'cmo', 'operação', 'empresa', 'produto', 'roadmap', 'discovery', 'prd', 'epic', 'sprint', 'backlog', 'prioridade'],
  },
  {
    id: 'squad-animations',
    name: 'Animations Squad',
    invoke: '/ca:agents:animations-orqx',
    description: 'Motion design, CSS animations, partículas, Three.js, shaders',
    keywords: ['animação', 'motion', '3d', 'partícula', 'transição', 'keyframe', 'spline', 'threejs', 'shader', 'gsap', 'lottie', 'scroll animation'],
  },
  {
    id: 'squad-cloning',
    name: 'Cloning Squad',
    invoke: '/SINAPSE:agents:cloning-orqx',
    description: 'Digital twins, clonagem cognitiva, mind synthesis',
    keywords: ['clone', 'persona', 'digital twin', 'voz', 'estilo', 'replicar', 'clonar', 'imitação', 'ghostwrite'],
  },
  {
    id: 'squad-finance',
    name: 'Finance Squad',
    invoke: '/finance:agents:finance-orqx',
    description: 'Budget, pricing, profitability analysis',
    keywords: ['financeiro', 'budget', 'custo', 'lucro', 'caixa', 'projeção', 'roi financeiro', 'p&l', 'fluxo de caixa', 'precificação'],
  },
  {
    id: 'squad-content',
    name: 'Content Squad',
    invoke: '/content:agents:content-orqx',
    description: 'Governança editorial, estratégia de conteúdo',
    keywords: ['conteúdo', 'editorial', 'blog', 'artigo', 'social', 'instagram', 'linkedin', 'twitter', 'post', 'calendário editorial'],
  },
  {
    id: 'squad-courses',
    name: 'Courses Squad',
    invoke: '/SINAPSE:agents:courses-orqx',
    description: 'Cursos, currículos, assessments, launch educacional',
    keywords: ['curso', 'treinamento', 'educação', 'aula', 'módulo', 'assessment', 'onboarding', 'lms', 'quiz', 'certificação'],
  },
  {
    id: 'squad-claude',
    name: 'Claude Code Mastery',
    invoke: '/claude:agents:claude-orqx',
    description: 'Claude Code avançado, MCP, hooks, skills',
    keywords: ['claude code', 'mcp', 'hook', 'skill', 'agent', 'workflow', 'automatizar', 'prompt', 'llm', 'ia', 'inteligência artificial', 'agent sdk'],
  },
  {
    id: 'advisory-board',
    name: 'Advisory Board',
    invoke: null,
    description: 'Board consultivo estratégico: Dalio, Naval, Munger, Thiel, Hoffman',
    keywords: ['visão', 'longo prazo', 'board', 'decisão estratégica', 'investimento', 'fundador', 'dalio', 'naval', 'munger', 'thiel', 'hoffman'],
  },
  {
    id: 'c-level-squad',
    name: 'C-Level Squad',
    invoke: null,
    description: 'Conselho executivo virtual: CEO, CTO, CMO, COO',
    keywords: ['ceo', 'cto', 'cmo', 'coo', 'executivo', 'c-level', 'liderança', 'empresa', 'estrutura organizacional'],
  },
  {
    id: 'hormozi-squad',
    name: 'Hormozi Squad',
    invoke: null,
    description: 'Ofertas irresistíveis, escala e aquisição de clientes (método Hormozi)',
    keywords: ['hormozi', 'oferta irresistível', 'leads', 'escala', 'retenção', 'pricing', 'modelo de negócio', 'aquisição', 'upsell', 'downsell'],
  },
  {
    id: 'movement',
    name: 'Movement Squad',
    invoke: null,
    description: 'Construção de movimentos, manifestos, identidade de causa',
    keywords: ['movimento', 'manifesto', 'impacto', 'causa', 'cultura', 'identidade de movimento', 'fenomenologia'],
  },
  {
    id: 'sop-factory',
    name: 'SOP Factory',
    invoke: null,
    description: 'Fábrica de SOPs, documentação de processos, padronização operacional',
    keywords: ['sop', 'processo', 'procedimento', 'documentação', 'manual', 'padronização', 'operacional', 'fábrica de sop'],
  },
];

// Squads legados (aliases de nomes antigos → squads canônicos ativos)
// Nota: hormozi-squad, advisory-board, c-level-squad, movement e sop-factory
// são agora squads canônicos — removidos do legacy map.
const LEGACY_MAP = {
  'brand-squad':          'squad-brand',
  'copy-squad':           'squad-copy',
  'design-squad':         'squad-design',
  'cybersecurity':        'squad-cybersecurity',
  'data-squad':           'squad-research',
  'storytelling':         'squad-storytelling',
  'claude-code-mastery':  'squad-claude',
};

// ── INTENT CLASSIFIER ────────────────────────────────────────────────────────

function classifyIntent(task) {
  if (!task || typeof task !== 'string') return null;

  const normalized = task.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

  const scores = SQUADS.map((squad) => {
    const keywordScore = squad.keywords.reduce((acc, kw) => {
      const kwNorm = kw.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
      // Peso proporcional ao tamanho da keyword: keywords mais longas/específicas valem mais
      return normalized.includes(kwNorm) ? acc + kwNorm.length : acc;
    }, 0);
    return { squad, score: keywordScore };
  });

  scores.sort((a, b) => b.score - a.score);
  const best = scores[0];

  // Retorna null se nenhuma keyword bateu (squad-dev como fallback na camada acima)
  return best.score > 0 ? best.squad : null;
}

// ── CONTEXT COMPRESSOR ───────────────────────────────────────────────────────
// Gera contexto comprimido do squad para economizar tokens no Claude Code

function compressContext(squad, task) {
  const lines = [
    `Squad: ${squad.name} (${squad.id})`,
    `Invoke: ${squad.invoke || 'direto via Claude Code'}`,
    `Especialidade: ${squad.description}`,
    `Task recebida: ${task}`,
    `Keywords match: ${squad.keywords.slice(0, 5).join(', ')}`,
  ];

  const context = lines.join('\n');

  // Estimativa: contexto completo seria ~3500 tokens (definições de squad + persona)
  // Contexto comprimido: ~90 tokens
  const FULL_TOKENS_EST = 3500;
  const compressed_tokens = Math.ceil(context.length / 4);
  const tokens_saved = FULL_TOKENS_EST - compressed_tokens;

  return { context, tokens_saved };
}

// ── LOGGER ESTRUTURADO ───────────────────────────────────────────────────────

function log(method, path, status, extra) {
  const ts = new Date().toISOString();
  const base = `[${ts}] ${method} ${path} → ${status}`;
  console.log(extra ? `${base} | ${extra}` : base);
}

// ── RESPONSE HELPERS ─────────────────────────────────────────────────────────

function sendJSON(res, statusCode, data) {
  const body = JSON.stringify(data, null, 2);
  res.writeHead(statusCode, {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body),
  });
  res.end(body);
}

function send405(res, path) {
  sendJSON(res, 405, { error: 'Method Not Allowed' });
  log('???', path, 405);
}

function send404(res, path) {
  sendJSON(res, 404, { error: 'Not Found', available: ['/status', '/squads', '/task', '/dispatch'] });
  log('???', path, 404);
}

// ── HANDLERS ─────────────────────────────────────────────────────────────────

function handleStatus(req, res) {
  if (req.method !== 'GET') return send405(res, '/status');

  const memUsage = process.memoryUsage();
  const data = {
    bridge: 'online',
    version: '2.0.0',
    timestamp: new Date().toISOString(),
    uptime_ms: Date.now() - START_TIME,
    port: PORT,
    squads: {
      total: SQUADS.length,
      list: SQUADS.map((s) => ({ id: s.id, name: s.name })),
    },
    memory: {
      rss_mb: (memUsage.rss / 1024 / 1024).toFixed(2),
      heap_used_mb: (memUsage.heapUsed / 1024 / 1024).toFixed(2),
      heap_total_mb: (memUsage.heapTotal / 1024 / 1024).toFixed(2),
    },
  };

  sendJSON(res, 200, data);
  log('GET', '/status', 200, `${SQUADS.length} squads`);
}

function handleSquads(req, res) {
  if (req.method !== 'GET') return send405(res, '/squads');

  const data = {
    total: SQUADS.length,
    squads: SQUADS.map((s) => ({
      id: s.id,
      name: s.name,
      invoke: s.invoke,
      description: s.description,
      keywords: s.keywords,
      status: 'active',
    })),
    legacy_map: LEGACY_MAP,
  };

  sendJSON(res, 200, data);
  log('GET', '/squads', 200, `${SQUADS.length} squads`);
}

function handleTask(req, res) {
  if (req.method !== 'POST') return send405(res, '/task');

  let body = '';
  req.on('data', (chunk) => { body += chunk; });
  req.on('end', () => {
    let parsed;
    try {
      parsed = JSON.parse(body);
    } catch (_) {
      sendJSON(res, 400, { error: 'Invalid JSON body' });
      log('POST', '/task', 400, 'invalid JSON');
      return;
    }

    const task = parsed.task;
    if (!task || typeof task !== 'string' || !task.trim()) {
      sendJSON(res, 400, { error: 'Campo "task" é obrigatório e deve ser uma string não vazia' });
      log('POST', '/task', 400, 'missing task field');
      return;
    }

    let squad = classifyIntent(task.trim());

    // Fallback para squad-dev quando nenhuma keyword bate
    if (!squad) {
      squad = SQUADS.find((s) => s.id === 'squad-dev');
    }

    const { context, tokens_saved } = compressContext(squad, task.trim());

    const data = {
      squad: squad.id,
      squad_name: squad.name,
      invoke: squad.invoke,
      context,
      tokens_saved,
      task_received: task.trim(),
      timestamp: new Date().toISOString(),
    };

    sendJSON(res, 200, data);
    log('POST', '/task', 200, `→ ${squad.id} | saved ~${tokens_saved} tokens`);
  });
}

// ── DISPATCH ─────────────────────────────────────────────────────────────────
// Classifica intent e retorna squad + invoke command
// Alias para /task — compatibilidade com integrações existentes

function handleDispatch(req, res) {
  if (req.method !== 'POST') return send405(res, '/dispatch');

  let body = '';
  req.on('data', (chunk) => { body += chunk; });
  req.on('end', () => {
    let parsed;
    try {
      parsed = JSON.parse(body);
    } catch (_) {
      sendJSON(res, 400, { error: 'Invalid JSON body' });
      log('POST', '/dispatch', 400, 'invalid JSON');
      return;
    }

    const task = parsed.task;
    if (!task || typeof task !== 'string' || !task.trim()) {
      sendJSON(res, 400, { error: 'Campo "task" é obrigatório' });
      log('POST', '/dispatch', 400, 'missing task field');
      return;
    }

    let squad = classifyIntent(task.trim());
    if (!squad) squad = SQUADS.find((s) => s.id === 'squad-dev');

    const { context } = compressContext(squad, task.trim());

    const result = {
      dispatched: true,
      squad: squad.id,
      squad_name: squad.name,
      invoke: squad.invoke,
      description: squad.description,
      context_compressed: context,
      task_received: task.trim(),
      timestamp: new Date().toISOString(),
    };

    sendJSON(res, 200, result);
    log('POST', '/dispatch', 200, `→ ${squad.id} | invoke: ${squad.invoke || 'manual'}`);
  });
}

// ── ROUTER ───────────────────────────────────────────────────────────────────

function router(req, res) {
  const url = req.url.split('?')[0]; // ignora query strings

  if (url === '/status')    return handleStatus(req, res);
  if (url === '/squads')    return handleSquads(req, res);
  if (url === '/task')      return handleTask(req, res);
  if (url === '/dispatch')  return handleDispatch(req, res);

  send404(res, url);
}

// ── BOOT ─────────────────────────────────────────────────────────────────────

const server = http.createServer(router);

server.listen(PORT, () => {
  console.log(`
╔══════════════════════════════════════════╗
║   Bridge Zvision-OS v2.1 — online        ║
║   http://localhost:${PORT}                  ║
║                                          ║
║   GET  /status   → health + squads       ║
║   GET  /squads   → registry completo     ║
║   POST /task     → intent classifier     ║
║   POST /dispatch → classify + invoke cmd ║
╚══════════════════════════════════════════╝
`);
  log('SYS', 'boot', 200, `porta ${PORT} | ${SQUADS.length} squads carregados`);
});

server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`\n❌ Porta ${PORT} já está em uso. Finalize o processo na porta e tente novamente.\n`);
  } else {
    console.error('❌ Erro no servidor:', err.message);
  }
  process.exit(1);
});

module.exports = server;
