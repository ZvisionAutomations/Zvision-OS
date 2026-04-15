# Research Brief — SOP Factory

## Domínio
Documentação de processos operacionais para agência de automação com IA em pré-lançamento.

## Frameworks de Referência

### ISO 9001 — Estrutura de Documentação de Processos
- Componentes obrigatórios: objetivo, escopo, responsável, procedimento, registros
- Critério de qualidade: qualquer colaborador treinado deve conseguir executar sem orientação adicional

### SOP Padrão do Setor (Agency Operations)
- Frontmatter de metadados (versão, status, data, responsável)
- Visão macro em tabela (fases, responsáveis, prazos, outputs)
- Detalhamento execucional nos pontos críticos
- Critérios de aceitação por fase (go/no-go)
- Histórico de versões

### Obsidian Knowledge Management
- Frontmatter YAML para indexação e busca
- Callouts (`> [!WARNING]`, `> [!TIP]`, `> [!NOTE]`) para destacar informações críticas
- Checkboxes (`- [ ]`) para itens de validação e checklists executáveis
- Wikilinks (`[[outro-doc]]`) para conexões entre documentos
- Tags no frontmatter para categorização e filtragem

## Vocabulário Profissional

### Sempre usar
- **SOP** (Standard Operating Procedure / Procedimento Operacional Padrão)
- **Gatilho** — o que inicia o processo
- **Output** — entregável concreto de cada fase
- **Responsável** — papel dono da execução (nunca nome pessoal)
- **Ponto de decisão / Gate** — go/no-go explícito no fluxo
- **Critério de conclusão** — como saber que a fase terminou
- **Staging** — ambiente de testes pré-produção
- **Go-live** — ativação em produção
- **Escalação** — acionamento de nível superior quando etapa bloqueia

### Nunca usar
- "Geralmente" ou "normalmente" em passos obrigatórios (ambiguidade)
- "O responsável deverá" (passivo + ambíguo — usar imperativo direto)
- "Etc." em listas de processos (incompletude disfarçada)
- Nomes de pessoas como responsáveis (não sobrevive à rotatividade)

## Boas Práticas Chave

1. **Nível híbrido (80/20):** tabela de visão macro + detalhe só nos pontos críticos — onboarding e qualidade mais detalhados; entregas mais compactas
2. **Output por fase como critério de conclusão:** mais confiável que prazo
3. **Callouts Obsidian para alertas:** `> [!WARNING]` em etapas críticas, `> [!TIP]` em boas práticas
4. **Checkboxes em itens de validação:** documentos funcionam como listas de tarefas ativas no Obsidian
5. **Versionamento no frontmatter + tabela de histórico:** rastreabilidade sem git
6. **Papéis funcionais, não pessoais:** "Engenheiro de Automação", não "João"

## Contexto da Zvision Automation
- Stack: Vanilla HTML/CSS/JS, Vercel, Node.js, WSL2
- Serviços: chatbots IA, automação CRM/pipeline, integrações de sistemas, dashboards automatizados
- Modelo: managed service contínuo (não entrega pontual)
- Tom: técnico, direto, estética cyber/tático, orientado a resultado
- Público dos SOPs: Miguel (fundador) + time futuro — legível para novos colaboradores
