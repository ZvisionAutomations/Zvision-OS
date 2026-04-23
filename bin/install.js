#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const VERSION = '2.0.0';
const PACKAGE_ROOT = path.resolve(__dirname, '..');
const TARGET = process.cwd();
const IS_IN_REPO = path.resolve(TARGET) === path.resolve(PACKAGE_ROOT);

// ANSI colors
const bold = (s) => `\x1b[1m${s}\x1b[0m`;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const cyan = (s) => `\x1b[36m${s}\x1b[0m`;
const dim = (s) => `\x1b[2m${s}\x1b[0m`;
const red = (s) => `\x1b[31m${s}\x1b[0m`;

function log(msg = '') {
  process.stdout.write(msg + '\n');
}

function banner() {
  log('');
  log('╔══════════════════════════════════════════════╗');
  log('║  ' + bold('ZVISION-OS v' + VERSION) + ' — Instalador              ║');
  log('║  23 squads · 300+ agentes · 1.400+ tasks    ║');
  log('║  Powered by Claude Code                     ║');
  log('╚══════════════════════════════════════════════╝');
  log('');
}

function checkNode() {
  const major = parseInt(process.versions.node.split('.')[0], 10);
  if (major < 18) {
    log(red(`ERRO: Node.js v18+ necessário. Versão atual: v${process.versions.node}`));
    log('Instale em https://nodejs.org');
    process.exit(1);
  }
}

function step(label) {
  log(cyan('→') + ' ' + label);
}

function ok(label) {
  log(green('  ✓') + ' ' + dim(label));
}

function copyDir(src, dest) {
  if (!fs.existsSync(src)) return;
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function copyIfMissing(src, dest) {
  if (fs.existsSync(dest)) return false;
  const srcFull = path.join(PACKAGE_ROOT, src);
  if (!fs.existsSync(srcFull)) return false;
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  if (fs.statSync(srcFull).isDirectory()) {
    copyDir(srcFull, dest);
  } else {
    fs.copyFileSync(srcFull, dest);
  }
  return true;
}

function installFresh() {
  const files = [
    ['.claude', path.join(TARGET, '.claude')],
    ['squads', path.join(TARGET, 'squads')],
    ['bridge', path.join(TARGET, 'bridge')],
    ['kits', path.join(TARGET, 'kits')],
    ['obsidian-vault', path.join(TARGET, 'obsidian-vault')],
    ['CLAUDE.md', path.join(TARGET, 'CLAUDE.md')],
    ['CONSTITUTION.md', path.join(TARGET, 'CONSTITUTION.md')],
    ['SECURITY.md', path.join(TARGET, 'SECURITY.md')],
    ['CONTRIBUTING.md', path.join(TARGET, 'CONTRIBUTING.md')],
    ['start.sh', path.join(TARGET, 'start.sh')],
    ['.mcp.json.example', path.join(TARGET, '.mcp.json.example')],
    ['.gitignore', path.join(TARGET, '.gitignore')],
    ['package.json', path.join(TARGET, 'package.json')],
  ];

  step('Copiando framework...');
  for (const [src, dest] of files) {
    const copied = copyIfMissing(src, dest);
    if (copied) ok(path.basename(src));
  }

  step('Criando .mcp.json a partir do template...');
  const mcpTarget = path.join(TARGET, '.mcp.json');
  const mcpExample = path.join(TARGET, '.mcp.json.example');
  if (!fs.existsSync(mcpTarget) && fs.existsSync(mcpExample)) {
    fs.copyFileSync(mcpExample, mcpTarget);
    ok('.mcp.json criado (configure suas chaves de API)');
  }

  step('Instalando dependências...');
  execSync('npm install', { cwd: TARGET, stdio: 'inherit' });
}

function configureExisting() {
  step('Configurando instalação existente...');

  const mcpTarget = path.join(TARGET, '.mcp.json');
  const mcpExample = path.join(TARGET, '.mcp.json.example');
  if (!fs.existsSync(mcpTarget) && fs.existsSync(mcpExample)) {
    fs.copyFileSync(mcpExample, mcpTarget);
    ok('.mcp.json criado (configure suas chaves de API)');
  } else if (fs.existsSync(mcpTarget)) {
    ok('.mcp.json já existe');
  }

  const nodeModules = path.join(TARGET, 'node_modules');
  if (!fs.existsSync(nodeModules)) {
    step('Instalando dependências...');
    execSync('npm install', { cwd: TARGET, stdio: 'inherit' });
  } else {
    ok('dependências já instaladas');
  }
}

function showSuccess() {
  log('');
  log('╔══════════════════════════════════════════════╗');
  log('║  ' + green('✓ Zvision-OS instalado com sucesso!') + '        ║');
  log('╚══════════════════════════════════════════════╝');
  log('');
  log(bold('Próximos passos:'));
  log('');
  log('  1. ' + bold('Configure suas credenciais'));
  log(dim('     edite .mcp.json com suas chaves de API'));
  log('');
  log('  2. ' + bold('Suba o Bridge de roteamento'));
  log(dim('     ./start.sh'));
  log('');
  log('  3. ' + bold('Abra o Claude Code na pasta e invoque'));
  log(dim('     /zvision [o que você precisa fazer]'));
  log('');
  log(dim('  Documentação → https://github.com/ZvisionAutomations/zvision-OS'));
  log('');
}

function showHelp() {
  log('');
  log(bold('Zvision-OS v' + VERSION));
  log('');
  log('Uso:');
  log('  npx github:ZvisionAutomations/zvision-OS        ' + dim('instala no diretório atual'));
  log('  npx github:ZvisionAutomations/zvision-OS help   ' + dim('exibe esta ajuda'));
  log('');
  log('O que é instalado:');
  log('  .claude/       ' + dim('Squads SINAPSE, regras, hooks e skills'));
  log('  squads/        ' + dim('23 squads com agentes, tasks, KBs e workflows'));
  log('  bridge/        ' + dim('Servidor de roteamento inteligente (porta 3333)'));
  log('  kits/          ' + dim('Automações pré-montadas por segmento de mercado'));
  log('  CLAUDE.md      ' + dim('Configuração central lida pelo Claude Code'));
  log('  CONSTITUTION.md ' + dim('Governança formal do framework'));
  log('');
}

function main() {
  const args = process.argv.slice(2);
  const cmd = args[0] || 'install';

  banner();
  checkNode();

  if (cmd === 'help' || cmd === '--help' || cmd === '-h') {
    showHelp();
    return;
  }

  if (cmd === '--version' || cmd === '-v') {
    log(`zvision-os v${VERSION}`);
    return;
  }

  if (IS_IN_REPO) {
    log(bold('Modo: configurar instalação local'));
    log(dim(`  Diretório: ${TARGET}`));
    log('');
    configureExisting();
  } else {
    log(bold('Modo: instalar Zvision-OS'));
    log(dim(`  Destino: ${TARGET}`));
    log('');
    installFresh();
  }

  showSuccess();
}

main();
