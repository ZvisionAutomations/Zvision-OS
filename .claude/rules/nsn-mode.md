---
paths: **/*
---

# NSN Mode — Never Say Never

> **GLOBAL:** Esta regra se aplica a TODOS os squads, TODOS os agentes, em TODAS as situações.

## Princípio

Nenhum agente, squad ou orquestrador pode responder "não consigo", "não é possível" ou
"isso não funciona" sem antes ter tentado **no mínimo 3 alternativas**.

## Protocolo de Execução

### Quando encontrar um obstáculo:

1. **Tentativa 1:** Abordagem direta com Tool/método primário
2. **Tentativa 2:** Alternativa com Tool/método secundário
3. **Tentativa 3:** Abordagem criativa ou workaround documentado
4. **Ciclos 4-5:** Se ainda bloqueado, documentar as 3 tentativas e escalar com contexto completo
5. **Ciclo 5+:** Escalar para o usuário com: o que foi tentado, o que falhou, por quê, e o que seria necessário para resolver

### O que NÃO é aceitável:

- Parar no primeiro erro sem diagnóstico
- Responder "isso não é possível" sem ter tentado alternativas
- Escalar sem documentar o que foi tentado
- Usar "a ferramenta não suporta" como resposta final sem verificar alternativas

### O que é aceitável (escalar com contexto):

```
Tentei 3 abordagens:
1. [Tool A / método A] → falhou porque [motivo específico]
2. [Tool B / método B] → falhou porque [motivo específico]
3. [Alternativa C] → falhou porque [motivo específico]

Para resolver isso seria necessário: [o que falta]
Recomendo: [próxima ação para o usuário]
```

## Máximo de Ciclos

- **5 ciclos** por obstáculo antes de escalar obrigatoriamente
- Cada ciclo deve usar uma abordagem diferente
- Ciclos repetindo a mesma abordagem não contam

## Aplicação por Domínio

| Domínio | Exemplos de alternativas |
|---------|--------------------------|
| Tool falhou | Tentar tool alternativa, tentar via Bash, tentar via MCP |
| API indisponível | Retry, usar cache, usar API alternativa, modo offline |
| Arquivo não encontrado | Buscar por pattern, buscar em paths alternativos, recriar |
| Permissão negada | Verificar path, usar caminho alternativo, pedir ao usuário |
| Código não compila | Verificar sintaxe, verificar dependências, simplificar abordagem |

## Exceções

NSN Mode NÃO se aplica a:
- Ações irreversíveis e destrutivas (rm -rf, drop table, force push em main) — estas requerem confirmação explícita do usuário
- Violações de segurança — nunca persistir para contornar proteções de segurança
- Instruções explícitas do usuário para parar
