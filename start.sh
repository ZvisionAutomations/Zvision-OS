#!/bin/bash
echo "Iniciando Zvision-OS..."

ZVISION_DIR="$(cd "$(dirname "$0")" && pwd)"
PAPERCLIP_DATA="$ZVISION_DIR/.paperclip"

# Kill processos anteriores nas portas
echo "Limpando portas..."
powershell -Command "
  @(3333, 3100) | ForEach-Object {
    \$port = \$_
    \$pid = (netstat -ano | Select-String \":\$port \" | Select-String 'LISTENING') -replace '.*\\s+(\\d+)$','$1'
    if (\$pid) { Stop-Process -Id \$pid -Force -ErrorAction SilentlyContinue; Write-Host \"Porta \$port liberada\" }
  }
" 2>/dev/null

sleep 1

# Subir Paperclip
echo "Subindo Paperclip (porta 3100)..."
cd "$ZVISION_DIR"
npx paperclipai run --data-dir "$PAPERCLIP_DATA" &
PAPERCLIP_PID=$!
sleep 15

# Verificar Paperclip
if curl -s http://localhost:3100/health > /dev/null 2>&1; then
  echo "Paperclip online"
  PAPERCLIP_OK=true
else
  echo "AVISO: Paperclip nao respondeu (Node.js v24 incompatibilidade conhecida)"
  echo "Bridge operará em modo standalone (classify-only)"
  PAPERCLIP_OK=false
fi

# Subir Bridge
echo "Subindo Bridge (porta 3333)..."
node "$ZVISION_DIR/bridge/index.js" &
BRIDGE_PID=$!
sleep 2

# Verificar Bridge
if curl -s http://localhost:3333/status > /dev/null 2>&1; then
  echo "Bridge online"
else
  echo "ERRO: Bridge falhou"
  exit 1
fi

echo ""
echo "=========================================="
echo "   Zvision-OS -- SISTEMA OPERACIONAL      "
echo ""
if [ "$PAPERCLIP_OK" = true ]; then
  echo "   Paperclip:  http://localhost:3100  OK  "
else
  echo "   Paperclip:  OFFLINE (fix Node version) "
fi
echo "   Bridge:     http://localhost:3333  OK  "
echo "   Squads:     23 canonicos               "
echo "=========================================="
echo ""
echo "Teste rapido:"
echo "  curl http://localhost:3333/status"
echo "  curl -X POST http://localhost:3333/task -H 'Content-Type: application/json' -d '{\"task\": \"criar proposta comercial\"}'"
