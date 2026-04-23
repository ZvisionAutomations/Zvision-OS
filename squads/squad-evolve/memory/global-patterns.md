---
name: global-patterns
type: evolve-memory
description: Padrões que funcionam consistentemente em todos os squads do Zvision-OS
---

# Global Patterns — O que funciona no Zvision-OS

## Padrões de Execução
- **YOLO + NSN combinados**: Remove fricção de confirmações e garante persistência em erros
- **PowerShell > bash/sed no Windows**: Replacements em massa mais confiáveis
- **Protocolo /pwf-brainstorm primeiro**: Evita retrabalho — planning sempre antes do código
- **Tasks para sessões longas**: Tracking explícito reduz drift de contexto

## Padrões de Routing
- **Squad match por keyword**: Funciona melhor que interpretação semântica aberta
- **Multi-squad para pedidos complexos**: Não forçar um squad onde dois são necessários
- **Skill específica no routing**: Incluir qual skill ativar elimina ambiguidade

## Padrões de Qualidade
- **Renaming antes de build**: Sempre limpar referências externas antes de construir
- **squad.yaml como fonte da verdade**: Mantém consistência entre registry e arquivos

## Atualizações
_Atualizar após cada sessão com novos padrões identificados._
