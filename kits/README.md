# Zvision AI Kits — Vertical Solutions

Kits pré-configurados de automação com IA para segmentos específicos.
Cada kit inclui 5 plugins prontos para deploy com n8n + WhatsApp + IA.

## Kits Disponíveis

| Kit | Segmento | Plugins | ROI Estimado |
|-----|----------|---------|--------------|
| [imobiliarias](imobiliarias/kit.yaml) | Imobiliárias & Corretores | 5 | 3-5x em 60 dias |
| [clinicas](clinicas/kit.yaml) | Clínicas & Consultórios | 5 | 2-4x em 30 dias |
| [juridico](juridico/kit.yaml) | Escritórios Jurídicos | 5 | 3-6x em 90 dias |

## Estrutura de um Kit

```
kits/{segmento}/
├── kit.yaml          — metadados, squad routing, MCPs necessários
└── plugins/          — 5 plugins com fluxo, integrações e agentes
    ├── plugin-1.md
    ├── plugin-2.md
    ├── plugin-3.md
    ├── plugin-4.md
    └── plugin-5.md
```

## Uso com Zvision-OS

Para ativar um kit em um projeto de cliente:

```
/client [Nome do Cliente]
/zvision kit imobiliarias    → carrega kit + roteia para squads corretos
/zvision kit clinicas        → carrega kit + roteia para squads corretos
/zvision kit juridico        → carrega kit + roteia para squads corretos
```

## Criar Novo Kit

Usar squad-forge:
```
/forge:agents:forge-chief
## Mission: criar-squad kit-{segmento}
```

---
_Zvision-OS v3.0 NEXUS — Vertical Kits_
