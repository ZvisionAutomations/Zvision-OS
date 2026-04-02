---
name: "write-checklist-quality"
description: "Escreve o Checklist de Qualidade Pré-Entrega em Markdown para Obsidian"
inputFile: "squads/sop-factory/output/process-maps.md"
outputFile: "squads/sop-factory/output/sops/checklist-qualidade-preentrega.md"
---

# Task: Escrever Checklist de Qualidade Pré-Entrega

## Processo

1. Carregar o mapa do processo "Checklist de Qualidade Pré-Entrega" de `process-maps.md`
2. Carregar tom e contexto da Zvision de `_opensquad/_memory/company.md`

3. Escrever o documento `checklist-qualidade-preentrega.md` com estrutura de checklist executável:
   - Frontmatter YAML completo
   - Resumo executivo (uso, quem executa, critério de aprovação: 100% obrigatórios)
   - Blocos temáticos de verificação com distinção `[OBRIGATÓRIO]` / `[OPCIONAL]`
   - Checkboxes para todos os itens
   - Callouts `> [!WARNING]` para blocos críticos
   - Seção de assinatura/aprovação no final
   - Tabela de histórico de versões

4. Salvar em `squads/sop-factory/output/sops/checklist-qualidade-preentrega.md`

## Estrutura de Blocos

Organizar em blocos temáticos relevantes para entrega de automação/agente de IA:
- Funcionalidade (testes com dados reais, cenários de erro, integrações)
- Documentação (SOP atualizado, changelog, credenciais documentadas)
- Segurança (acessos revisados, dados sensíveis protegidos)
- Comunicação com cliente (demo agendada, material de handoff pronto)
- Go-live (monitoramento ativo, plano de rollback definido)

Frontmatter:
```yaml
título: Checklist — Qualidade Pré-Entrega
tipo: checklist
versão: 1.0
data: [hoje]
status: ativo
tags: [operacoes, qualidade, checklist, entrega]
```

## Quality Criteria

- [ ] Frontmatter YAML completo
- [ ] Distinção [OBRIGATÓRIO] / [OPCIONAL] em todos os itens
- [ ] Checkboxes em todos os itens
- [ ] Pelo menos 1 callout [!WARNING]
- [ ] Seção de aprovação/assinatura
- [ ] Tabela de histórico de versões

## Veto Conditions

- Documento sem frontmatter YAML
- Itens sem distinção OBRIGATÓRIO/OPCIONAL
- Uso de em dashes (—) no texto corrido
