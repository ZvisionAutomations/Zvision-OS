#!/bin/bash
# Zvision-OS — Start Script
# Sobe: Paperclip (3100) + Bridge (3333)
# EvolutionAPI + agent sobem via Docker Desktop separado

echo "🚀 Iniciando Zvision-OS..."

ZVISION_DIR="$(cd "$(dirname "$0")" && pwd)"

# Paperclip (ajuste o caminho conforme sua instalação)
# npx paperclipai run --data-dir "$ZVISION_DIR/.paperclip" &
# sleep 3

# Bridge
cd "$ZVISION_DIR/bridge"
node index.js &

echo "✅ Paperclip: http://localhost:3100"
echo "✅ Bridge:    http://localhost:3333"
echo ""
echo "Para o agente WA: cd zvision-wa && docker compose up"
