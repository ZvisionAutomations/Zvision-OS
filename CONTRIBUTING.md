# Contributing to Zvision-OS

Obrigado pelo interesse em contribuir! Zvision-OS é um framework de código aberto para transformar o Claude Code em uma plataforma de automação completa.

## Como Contribuir

### 1. Reportar Bugs

Abra uma [Issue](https://github.com/ZvisionAutomations/zvision-OS/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. atual
- Versão do Claude Code e sistema operacional

### 2. Propor Novas Features

Antes de implementar, abra uma Issue com:
- Caso de uso concreto
- Qual squad/domínio seria afetado
- Proposta de implementação (opcional)

### 3. Contribuir com Código

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/SEU-USER/zvision-OS.git
cd zvision-OS

# 3. Crie uma branch para sua feature
git checkout -b feat/nome-da-feature

# 4. Faça suas mudanças
# 5. Commit com mensagem descritiva
git commit -m "feat(squad-copy): adiciona agente de copy para email cold"

# 6. Push e abra um PR
git push origin feat/nome-da-feature
```

### 4. Contribuir com Novos Agentes

A estrutura básica de um agente está em `squads/_template-memory.md`.

Cada agente deve ter:
- **Frontmatter YAML** com `tags`, `aliases`
- **Descrição clara** de para que serve e como usar
- **Persona definida** com nome, role, expertise
- **Comandos/tasks** mapeados para arquivos em `squads/{squad}/tasks/`

### 5. Contribuir com Novos Squads

Para adicionar um squad:
1. Crie `squads/squad-{nome}/` com a estrutura padrão
2. Adicione `squad.yaml` com metadados
3. Registre em `squads/registry.yaml`
4. Adicione entrada no `CLAUDE.md` na tabela de squads

## Estrutura de Squads

```
squads/squad-{nome}/
├── squad.yaml              — metadados e configuração
├── README.md               — documentação do squad
├── agents/                 — agentes especializados
│   ├── {nome}-orqx.md      — orquestrador principal
│   └── {especialista}.md   — agentes especialistas
├── tasks/                  — tarefas executáveis
├── workflows/              — workflows multi-agente
├── knowledge-base/         — bases de conhecimento
└── checklists/             — checklists de qualidade
```

## Convenções

### Commits
Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(squad-design): adiciona agente de design system
fix(bridge): corrige roteamento de intent para squad-copy
docs(readme): atualiza seção de início rápido
chore(gitignore): adiciona .paperclip ao ignore
```

### Agentes
- Nome do arquivo: `kebab-case.md`
- Nome do agente (persona): PascalCase ou nome próprio
- IDs: `kebab-case`
- Sempre incluir `whenToUse` no YAML

### Segurança
- Nunca inclua credenciais, tokens ou chaves reais
- Use placeholders como `sua-chave-aqui` em exemplos
- O Token Guardian Hook bloqueia commits com secrets detectados

## Código de Conduta

- Seja respeitoso e construtivo
- Foque em soluções, não em problemas
- Contribuições de todos os níveis são bem-vindas

## Dúvidas?

Abra uma Issue com a label `question` ou entre em contato em zvisionforb2b@gmail.com.
