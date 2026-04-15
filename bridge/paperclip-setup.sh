#!/bin/bash
# Paperclip Setup — Zvision Squads
# Executar APÓS Paperclip estar rodando em http://localhost:3100
# Requer: npx paperclipai company/agent commands

PAPERCLIP_DATA="C:/Users/Lenovo/Documents/zvision-OS/.paperclip"

echo "Verificando Paperclip..."
if ! curl -s http://localhost:3100/health > /dev/null; then
  echo "ERRO: Paperclip nao esta rodando. Execute 'paperclipai run' primeiro."
  exit 1
fi
echo "Paperclip online."

echo ""
echo "Criando empresa Zvision..."
npx paperclipai company create \
  --name "Zvision" \
  --goal "Agencia de automacao que entrega projetos completos para clientes usando squads de IA especializados" \
  --data-dir "$PAPERCLIP_DATA"

echo ""
echo "Registrando squads prioritarios..."

# 1. squad-commercial
npx paperclipai agent create \
  --company "Zvision" \
  --name "Commercial Squad" \
  --role "Pipeline comercial, prospeccao, qualificacao de leads e estruturacao de propostas" \
  --invoke "/commercial:agents:commercial-orqx" \
  --data-dir "$PAPERCLIP_DATA"

# 2. squad-copy
npx paperclipai agent create \
  --company "Zvision" \
  --name "Copy Squad" \
  --role "Producao de copy persuasivo, headlines, email marketing e scripts para clientes" \
  --invoke "/copywriting:agents:copy-orqx" \
  --data-dir "$PAPERCLIP_DATA"

# 3. squad-content
npx paperclipai agent create \
  --company "Zvision" \
  --name "Content Squad" \
  --role "Estrategia editorial, calendario de conteudo, producao para redes sociais e blog" \
  --invoke "/content:agents:content-orqx" \
  --data-dir "$PAPERCLIP_DATA"

# 4. hormozi-squad
npx paperclipai agent create \
  --company "Zvision" \
  --name "Hormozi Squad" \
  --role "Criacao de ofertas irresistiveis, modelo de aquisicao, pricing e escala baseado no metodo Hormozi" \
  --invoke "null" \
  --data-dir "$PAPERCLIP_DATA"

# 5. advisory-board
npx paperclipai agent create \
  --company "Zvision" \
  --name "Advisory Board" \
  --role "Conselho consultivo estrategico com Ray Dalio, Charlie Munger, Naval Ravikant, Peter Thiel, Reid Hoffman" \
  --invoke "null" \
  --data-dir "$PAPERCLIP_DATA"

echo ""
echo "Setup concluido. Verificar em http://localhost:3100"
