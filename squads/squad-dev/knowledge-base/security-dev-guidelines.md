# Security Dev Guidelines — Squad Dev

Diretrizes de segurança para desenvolvimento web. Obrigatório em todos os projetos.

## Regras Absolutas (violação = bloqueia deploy)

1. **Sem secrets em código** — API keys, senhas, tokens nunca em arquivos commitados
2. **Sem innerHTML com dados externos** — usar `textContent` ou sanitizar com DOMPurify
3. **Inputs sempre validados server-side** — validação client-side é UX, não segurança
4. **HTTPS em produção** — sem exceção, Vercel fornece automaticamente

## XSS Prevention

```javascript
// VULNERÁVEL
element.innerHTML = `<p>Olá, ${nomeDoUsuario}</p>`;

// SEGURO — textContent
element.textContent = nomeDoUsuario;

// SEGURO — criação programática de DOM
const p = document.createElement('p');
p.textContent = `Olá, ${nomeDoUsuario}`;
container.appendChild(p);

// SEGURO — template literal com escape manual
function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
element.innerHTML = `<p>Olá, ${escapeHtml(nomeDoUsuario)}</p>`;
```

## Secrets Management

```javascript
// ERRADO — secret no código
const API_KEY = 'sk-abc123def456';
fetch(`https://api.service.com/data?key=${API_KEY}`);

// CERTO — via variável de ambiente (servidor)
// api/handler.js (Vercel serverless function)
const API_KEY = process.env.SERVICE_API_KEY;
```

```bash
# Configurar no Vercel (nunca em .env commitado)
vercel env add SERVICE_API_KEY production
```

```
# .gitignore — SEMPRE incluir
.env
.env.local
.env.production
*.env
```

## Content Security Policy (CSP)

```json
// vercel.json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Content-Security-Policy",
          "value": "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' https://fonts.gstatic.com"
        }
      ]
    }
  ]
}
```

## Formulários Seguros

```javascript
// Validação dupla: client-side (UX) + server-side (segurança)

// Client-side — apenas para UX
function validarEmailClient(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Server-side — segurança real
export default function handler(req, res) {
  const { email } = req.body;
  
  // Sanitizar
  const emailLimpo = email?.toString().trim().toLowerCase();
  
  // Validar
  if (!emailLimpo || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailLimpo)) {
    return res.status(400).json({ error: 'Email inválido' });
  }
  
  // Limitar tamanho
  if (emailLimpo.length > 254) {
    return res.status(400).json({ error: 'Email muito longo' });
  }
  
  // Processar com email validado
}
```

## Verificação de Dependências

```bash
# Antes de qualquer deploy
npm audit

# Ver vulnerabilidades críticas
npm audit --audit-level=critical

# Atualizar pacotes com vulnerabilidades
npm audit fix

# Para vulnerabilidades que requerem major version bump
npm audit fix --force  # CUIDADO — pode quebrar API
```

## Checklist de Segurança Rápido

Antes de fazer `git push`:

- [ ] `git diff --staged` — nenhum secret visível
- [ ] `grep -r "API_KEY\|SECRET\|PASSWORD\|TOKEN" --include="*.js" --include="*.html" .` — nenhum resultado
- [ ] `npm audit` — nenhuma vulnerabilidade CRITICAL
- [ ] Formulários validam server-side
- [ ] `innerHTML` não usado com dados externos
