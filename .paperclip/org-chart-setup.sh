#!/bin/bash
# Paperclip Org Chart Setup — Zvision Automations
# Executar no WSL2 quando Paperclip estiver online: bash .paperclip/org-chart-setup.sh

PAPERCLIP="http://localhost:3100"

# Verifica saúde
if ! curl -s $PAPERCLIP/health > /dev/null 2>&1; then
  echo "❌ Paperclip offline. Inicie com: ~/start-zvision.sh"
  exit 1
fi

echo "✅ Paperclip online. Configurando org chart..."

# Empresa
curl -s -X POST $PAPERCLIP/api/companies \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Zvision Automations",
    "mission": "Agência de automação de processos e IA. Transformar operações manuais em sistemas inteligentes. Pré-lançamento — primeiro cliente em 30 dias.",
    "values": ["world-class quality", "spec-driven development", "documentation-first", "zero mediocrity"],
    "stage": "pre-launch"
  }' | jq '.' 2>/dev/null || echo "Empresa criada"

# Board (Miguel)
curl -s -X POST $PAPERCLIP/api/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Miguel — Board",
    "role": "Founder & Board",
    "description": "Aprova specs, decide direção estratégica, autoriza deploys em produção",
    "adapterType": "human",
    "capabilities": ["approve-specs", "approve-strategy", "authorize-deploys"]
  }' | jq '.' 2>/dev/null && echo "✅ Board registrado"

# CEO
curl -s -X POST $PAPERCLIP/api/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Zvision CEO",
    "role": "Chief Executive Officer",
    "description": "Valida direção estratégica, aprova features de alto impacto, delega para squads especializados",
    "adapterType": "http",
    "endpoint": "http://localhost:3300/execute",
    "adapterConfig": {
      "squad": "squad-c-level",
      "agent": "clevel-orqx",
      "model": "claude-sonnet-4-20250514"
    }
  }' | jq '.' 2>/dev/null && echo "✅ CEO registrado"

# CTO
curl -s -X POST $PAPERCLIP/api/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Zvision CTO",
    "role": "Chief Technology Officer",
    "description": "Aprova arquitetura técnica, valida specs de desenvolvimento, autoriza merges",
    "adapterType": "http",
    "endpoint": "http://localhost:3300/execute",
    "adapterConfig": {
      "squad": "squad-dev",
      "agent": "architect",
      "model": "claude-sonnet-4-20250514"
    }
  }' | jq '.' 2>/dev/null && echo "✅ CTO registrado"

# CMO
curl -s -X POST $PAPERCLIP/api/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Zvision CMO",
    "role": "Chief Marketing Officer",
    "description": "Supervisiona copy, brand, tráfego e growth. Aprova materiais de marketing.",
    "adapterType": "http",
    "endpoint": "http://localhost:3300/execute",
    "adapterConfig": {
      "squad": "squad-commercial",
      "agent": "commercial-orqx",
      "model": "claude-sonnet-4-20250514"
    }
  }' | jq '.' 2>/dev/null && echo "✅ CMO registrado"

# CSO
curl -s -X POST $PAPERCLIP/api/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Zvision CSO",
    "role": "Chief Security Officer",
    "description": "Aprova deploys em produção, audita segurança, valida RLS e headers",
    "adapterType": "http",
    "endpoint": "http://localhost:3300/execute",
    "adapterConfig": {
      "squad": "squad-cybersecurity",
      "agent": "cyber-orqx",
      "model": "claude-sonnet-4-20250514"
    }
  }' | jq '.' 2>/dev/null && echo "✅ CSO registrado"

echo ""
echo "Org chart final:"
curl -s $PAPERCLIP/api/agents | jq '[.[] | {name, role}]' 2>/dev/null
echo "✅ Setup completo."
