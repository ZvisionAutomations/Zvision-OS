#!/bin/bash
# Zvision-OS — Start Script
# Sobe o Bridge de roteamento (porta 3333)
# O agente WhatsApp sobe separado via Docker (veja zvision-wa/)

set -e

ZVISION_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Iniciando Zvision-OS Bridge..."

# Verificar Node.js
if ! command -v node &>/dev/null; then
  echo "ERRO: Node.js não encontrado. Instale em https://nodejs.org (v18+)"
  exit 1
fi

NODE_VERSION=$(node -e "process.stdout.write(process.version.slice(1).split('.')[0])")
if [ "$NODE_VERSION" -lt 18 ]; then
  echo "ERRO: Node.js v18+ necessário. Versão atual: $(node -v)"
  exit 1
fi

# Instalar dependências se necessário
if [ ! -d "$ZVISION_DIR/node_modules" ]; then
  echo "Instalando dependências..."
  cd "$ZVISION_DIR" && npm install
fi

# Liberar porta 3333 se ocupada
if command -v lsof &>/dev/null; then
  lsof -ti:3333 | xargs kill -9 2>/dev/null || true
elif command -v fuser &>/dev/null; then
  fuser -k 3333/tcp 2>/dev/null || true
fi

# Subir Bridge
echo "Subindo Bridge (porta 3333)..."
node "$ZVISION_DIR/bridge/index.js"
