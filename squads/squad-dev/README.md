# Dev Squad — Desenvolvimento de Software World-Class

Squad de desenvolvimento da Zvision. Implementa sites, landing pages, features,
componentes e APIs com Vanilla HTML/CSS/JS, Node.js e Vercel.

## Stack

- **Frontend:** Vanilla HTML5, CSS3 (custom properties), JavaScript ES6+
- **Backend:** Node.js
- **Deploy:** Vercel
- **Ambiente:** WSL2 Ubuntu-Antigravity

## Agentes

| Agente | Nome | Papel |
|--------|------|-------|
| `@dev-orqx` | Forge Prime ⚙️ | Orquestrador — delega ao especialista certo |
| `@architect` | Blueprint 🏗️ | Arquitetura, tech stack, estrutura |
| `@developer` | Coder 💻 | Implementação HTML/CSS/JS/Node |
| `@quality-gate` | Sentinel 🔍 | QA, code review, testes |
| `@devops` | Pipeline 🚀 | Git, deploy Vercel, CI/CD |
| `@ux-engineer` | Pixel 🎨 | UI pixel-perfect, design system |
| `@security-dev` | Shield 🛡️ | Segurança, OWASP Top 10 |

## Como Invocar

```
/dev:agents:dev-orqx
```

## Regras Inegociáveis

- Zero TypeScript `any`
- Apenas CSS variables — nunca valores crus de cor
- Nunca commita sem `/hm-engineer`
- @security-dev revisa antes de qualquer deploy
- Todo código passa pelo @quality-gate antes de ser considerado pronto

## Workflows

1. **feature-build-cycle** — Brief → Arquitetura → Implementação → QA → Security → Deploy
2. **bug-fix-cycle** — Diagnóstico → Fix → Teste → Deploy
3. **deploy-cycle** — Review → Build → Vercel → Verificação pós-deploy

## Conexões

- **Recebe de:** squad-design (specs visuais), squad-cybersecurity (auditorias), squad-product (stories)
- **Entrega para:** squad-design (código implementado), squad-cybersecurity (código para audit), squad-growth (landing pages)
