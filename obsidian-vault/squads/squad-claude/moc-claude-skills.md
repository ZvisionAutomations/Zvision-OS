---
name: moc-claude-skills
squad: squad-claude
type: moc
description: Biblioteca de skills do Claude Code — ativos, configuração e quando usar cada um
---
# Claude Skills

## Skills ativos no Zvision-OS
O [[config-engineer]] mantém o inventário de skills em `~/.claude/`:
[[psters-workflow]] (/pwf-*) para protocolo de desenvolvimento,
[[gstack]] (/review, /qa, /ship, /design-*) para qualidade de entrega,
[[highermind]] (/hm-*) para padrão de qualidade world-class,
[[brain-scott]] (/vault-*) para integração com o segundo cérebro.

## MCPs instalados
O [[mcp-integrator]] rastreia MCPs ativos em `.claude.json`:
playwright para automação de browser, desktop-commander para Docker,
github para operações de PR/issue, obsidian para acesso ao vault.
Ver [[moc-claude-mcps]] para configuração detalhada.

## Criação de novos skills
O [[skill-craftsman]] segue o processo: especificação em
[[obsidian-vault/specs/]] → implementação → teste → documentação aqui.
Nenhum skill é criado sem spec aprovada — mesmo para os skills
do próprio sistema de IA.

## Agentes e squads
O [[agent-forger]] documenta cada novo agente criado em
[[obsidian-vault/pessoas/]] com perfil completo de capacidades.
O [[unified-intelligence-stack]] tem a visão consolidada de tudo.
