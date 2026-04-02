# Domain Framework — Documentação de Processos Operacionais

## Framework de Mapeamento de Processos (Mário Mapeamento)

### Estrutura de um Processo Bem Mapeado

```
PROCESSO: {Nome}
├── Gatilho: o que inicia o processo
├── Input: o que precisa existir para começar
├── Output final: o resultado ao término
└── Fases:
    ├── Fase 1: {Nome}
    │   ├── Objetivo: o que deve ser alcançado
    │   ├── Responsável: papel funcional
    │   ├── Passos: lista numerada de ações
    │   ├── Ferramentas: plataformas/sistemas usados
    │   ├── Output: o que é produzido ao final
    │   └── Ponto de decisão: condição go/no-go
    ├── Fase 2: ...
    └── ...
```

### Os 4 Processos Core da Zvision

#### 1. Onboarding de Cliente
- **Gatilho:** Contrato assinado + primeiro pagamento confirmado
- **Fases típicas:** Kick-off → Mapeamento técnico → Configuração → Validação → Go-live
- **Crítico:** Fase 1 (Kick-off) e Fase 4 (Validação) — maior risco de retrabalho

#### 2. Entrega de Automação
- **Gatilho:** Story/escopo aprovado + acesso às ferramentas do cliente confirmado
- **Fases típicas:** Spec técnica → Desenvolvimento → Testes → Aprovação cliente → Deploy
- **Crítico:** Spec técnica (evita retrabalho) e Deploy (irreversível)

#### 3. Entrega de Agente de IA
- **Gatilho:** Requisitos de comportamento documentados + base de conhecimento disponível
- **Fases típicas:** Design de comportamento → Treinamento/configuração → Testes de edge cases → Validação com cliente → Ativação
- **Crítico:** Testes de edge cases (agentes falham em situações não previstas) e Ativação

#### 4. Checklist de Qualidade Pré-Entrega
- **Gatilho:** Qualquer entrega prestes a ir para o cliente
- **Estrutura:** Blocos por categoria (funcionalidade, performance, segurança, documentação, comunicação)
- **Crítico:** 100% dos itens obrigatórios — não há aprovação parcial

---

## Framework de Escrita de SOPs (Sofia SOP)

### Estrutura Híbrida por Documento

```markdown
---
frontmatter YAML (título, tipo, versão, data, status, tags)
---

# Título do SOP

> Resumo executivo (3 linhas: objetivo + gatilho + output)

## Visão Geral (tabela de fases)
| Fase | Nome | Responsável | Prazo | Output |

## Fase N: {Nome} — [CRÍTICO ou padrão]
> [!WARNING] ou > [!TIP] se aplicável

### N.N Passo
- Responsável: ...
- Ferramenta: ...
- Output: ...
- [ ] Checklist de validação

## Histórico de Versões
| Versão | Data | Autor | Mudanças |
```

### Regras de Nível de Detalhe (Híbrido)

| Tipo de Fase | Nível | Formato |
|---|---|---|
| Fase crítica (onboarding, quality gate) | Alto | Passo a passo com checklist + callouts |
| Fase padrão | Médio | Lista numerada com responsável e output |
| Fase simples/administrativa | Baixo | Lista de bullets |

---

## Framework de Revisão (Renata Revisão)

### 5 Dimensões de Avaliação

| Dimensão | Peso | Critério de 10/10 |
|---|---|---|
| Completude | Alta | Todos os passos, responsáveis, outputs e ferramentas presentes |
| Clareza operacional | Alta | Qualquer colaborador executa sem pedir ajuda |
| Precisão contextual | Média | Usa terminologia, ferramentas e papéis reais da Zvision |
| Formatação Obsidian | Média | Frontmatter, callouts, checkboxes, wikilinks corretos |
| Acionabilidade | Alta | Passos executáveis imediatamente, sem gaps |

### Regra de Aprovação
- **APROVADO:** média >= 7 E nenhuma dimensão < 4
- **REVISÃO NECESSÁRIA:** média < 7 OU qualquer dimensão < 4
