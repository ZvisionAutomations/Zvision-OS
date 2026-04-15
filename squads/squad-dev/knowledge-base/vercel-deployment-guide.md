# Vercel Deployment Guide — Squad Dev

Guia de deploy para projetos Zvision no Vercel.

## Setup Inicial

### 1. Instalar Vercel CLI (WSL2)
```bash
npm install -g vercel
vercel login
```

### 2. Conectar projeto
```bash
cd /mnt/c/Users/Lenovo/Documents/[nome-projeto]
vercel
# Seguir wizard: link to existing project ou criar novo
```

### 3. Estrutura para sites estáticos
```
projeto/
├── index.html        # Página principal
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── assets/
│   └── images/
└── vercel.json       # Configurações de deploy (opcional)
```

## vercel.json (configurações comuns)

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    },
    {
      "source": "/assets/(.*)",
      "headers": [
        { "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }
      ]
    }
  ],
  "redirects": [
    { "source": "/old-page", "destination": "/new-page", "permanent": true }
  ]
}
```

## Deploy Manual

```bash
# Preview deploy (não afeta produção)
vercel

# Deploy para produção
vercel --prod

# Ver status de deploys
vercel ls

# Ver logs de um deploy
vercel logs [url-do-deploy]
```

## Variáveis de Ambiente

```bash
# Adicionar via CLI
vercel env add NOME_DA_VARIAVEL production

# Listar variáveis
vercel env ls

# Remover variável
vercel env rm NOME_DA_VARIAVEL
```

**NUNCA colocar secrets em:**
- `.env` commitado
- `vercel.json`
- Qualquer arquivo de código

## Domínio Customizado

```bash
# Adicionar domínio
vercel domains add meu-dominio.com

# Verificar status DNS
vercel domains inspect meu-dominio.com
```

## Node.js Functions (API Routes)

```
projeto/
├── api/
│   ├── contact.js    # POST /api/contact
│   └── health.js     # GET /api/health
└── index.html
```

```javascript
// api/contact.js
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }
  
  const { name, email, message } = req.body;
  
  // Validação server-side
  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Email inválido' });
  }
  
  // Lógica de negócio aqui
  
  res.status(200).json({ success: true });
}
```

## Troubleshooting Comum

| Problema | Causa | Solução |
|---------|-------|---------|
| Deploy falhou | Build error | Verificar `vercel logs` |
| Variável não carrega | Não redeployada após add | `vercel --prod` novamente |
| 404 em rotas | SPA sem redirects | Adicionar redirect em vercel.json |
| Headers CORS | Configuração ausente | Adicionar em vercel.json headers |
| Build lento | Assets grandes | Otimizar imagens, lazy loading |
