# Agent Generation Guide — De Perfil Cognitivo a Agent.md

> Como mapear um cognitive-profile.md para um agent.md de alta fidelidade
> seguindo SQUAD-CREATION-STANDARDS.

---

## Mapeamento Layer → Agent Section

| Cognitive Layer | Agent Section | Como mapear |
|----------------|--------------|------------|
| L1: Mental Models | `core_principles` | Top 5-6 models mais fortes viram principios |
| L2: Heuristics | `heuristics` | Cada heuristic vira trigger/action/rationale |
| L3: Workflows | `protocols` | Cada workflow vira protocol com steps |
| L4: Communication | `persona_profile` | Tom, greeting, signature, vocabulario |
| L5: Meta-patterns | `identity` | Core axiom define a identidade do agente |

---

## Passo a Passo

### 1. Persona Profile (de Layer 4)
```yaml
persona_profile:
  archetype: # Inferido da identidade (Strategist, Builder, Analyst, etc)
  real_person: true
  source_mind: "Nome da pessoa original"
  clone_tier: # 2 ou 3
  confidence_score: # Percentual
  communication:
    tone: # Extraido de Layer 4 (direto, informal, tecnico, etc)
    greeting_levels:
      minimal: "{icon} {agent-id} ready"
      named: "{icon} {Nome} ready — {catchphrase}"
      archetypal: "{icon} {Nome} — {tagline baseada em core axiom}"
    signature_closing: "— {Nome}, {action} {icon}"
```

### 2. Core Principles (de Layer 1)
Selecionar os 5-6 mental models mais fortes (recorrentes, alta confianca).
Cada um vira uma string concisa que captura a essencia do model.

**Criterio de selecao:**
- [DIRETO] ou [INFERIDO] apenas (nunca [HIPOTESE] como principio)
- Aparece em 3+ fontes
- E actionable (guia decisoes)

### 3. Heuristics (de Layer 2)
Converter cada heuristic extraida para o formato:
```yaml
- trigger: "Situacao que ativa a regra"
  action: >
    O que fazer (nas palavras/estilo da pessoa)
  rationale: "Por que (citacao ou inferencia da pessoa)"
```

**Regras:**
- Min 5 heuristics para Tier 2, 10 para Tier 3
- Rationale deve ser da pessoa, nao generico
- Se [HIPOTESE]: adicionar comentario `# [HIPOTESE]`

### 4. Protocols (de Layer 3)
Converter cada workflow extraido para:
```yaml
- name: "nome-do-processo"
  steps:
    - "Step 1: ..."
    - "Step 2: ..."
```

### 5. Commands
Derivar de capabilities do agente:
- Cada workflow principal vira um `*command`
- Adicionar `*help` e `*status` sempre
- Naming: verbos de acao (`*analyze`, `*create`, `*review`)

### 6. Identity (de Layer 5)
Core axiom + meta-patterns definem a `identity`:
```yaml
identity: >
  Descricao que captura a essencia de como essa pessoa pensa
  e opera. Baseado no core axiom e meta-patterns identificados.
```

---

## Quality Checklist

- [ ] `real_person: true` e `source_mind` preenchidos
- [ ] `clone_tier` e `confidence_score` corretos
- [ ] `core_principles` tem 5-6 itens de alta confianca
- [ ] `heuristics` tem min 5 (Tier 2) ou 10 (Tier 3)
- [ ] Cada heuristic tem trigger + action + rationale
- [ ] `protocols` refletem workflows reais da pessoa
- [ ] `communication.tone` reflete Layer 4
- [ ] Nenhum principio ou heuristic e generico/inventado
- [ ] Cross-squad handoffs definidos
- [ ] Formato segue SQUAD-CREATION-STANDARDS

---

## O Que NAO Fazer

- **Nao inventar heuristics** que soam boas mas nao foram extraidas
- **Nao generalizar** — manter especificidade do target
- **Nao embelezar** — se a pessoa e direta/crua, o agente tambem e
- **Nao misturar** conhecimento generico com extracoes do target
- **Nao ignorar gaps** — documentar o que falta em vez de preencher
