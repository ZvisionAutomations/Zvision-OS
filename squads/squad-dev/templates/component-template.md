# Component Template — Squad Dev

Template para componentes reutilizáveis (HTML + CSS + JS).

## Estrutura de Componente

### HTML
```html
<!-- Card Component -->
<article class="card" data-component="card">
  <div class="card__image">
    <img src="[url]" alt="[Descrição da imagem]" loading="lazy" width="400" height="250" />
  </div>
  <div class="card__body">
    <h3 class="card__title">[Título do card]</h3>
    <p class="card__description">[Descrição]</p>
    <a href="[url]" class="card__link btn btn-secondary">
      [CTA]
    </a>
  </div>
</article>
```

### CSS (usando variáveis)
```css
/* card.css */
.card {
  background-color: var(--color-bg);
  border: var(--border-width) solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: box-shadow var(--transition-base), transform var(--transition-base);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card__image img {
  width: 100%;
  height: auto;
  display: block;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.card__body {
  padding: var(--space-6);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.card__title {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-semibold);
  color: var(--color-text);
  line-height: var(--line-height-tight);
}

.card__description {
  font-size: var(--font-size-base);
  color: var(--color-text-secondary);
  line-height: var(--line-height-relaxed);
}

.card__link {
  margin-top: auto; /* Push para baixo do flex container */
  align-self: flex-start;
}
```

### JavaScript (inicialização de componente)
```javascript
// components/card.js
export function initCards(container = document) {
  const cards = container.querySelectorAll('[data-component="card"]');
  
  cards.forEach(card => {
    // Tornar card inteiro clicável sem quebrar acessibilidade
    const link = card.querySelector('.card__link');
    if (!link) return;
    
    card.style.cursor = 'pointer';
    card.addEventListener('click', (e) => {
      // Se clicou no link diretamente, deixar o comportamento padrão
      if (e.target.closest('.card__link')) return;
      link.click();
    });
  });
}

// main.js
import { initCards } from './components/card.js';
initCards();
```

## Padrão de Nomenclatura CSS (BEM simplificado)

```
.bloco { }              /* Componente */
.bloco__elemento { }    /* Parte do componente */
.bloco--modificador { } /* Variante do componente */

Exemplos:
.card { }
.card__title { }
.card__body { }
.card--featured { }     /* Variante em destaque */
.card--compact { }      /* Variante compacta */
```

## Variantes via CSS Custom Properties

```css
/* Variante padrão */
.card {
  --card-bg: var(--color-bg);
  --card-border: var(--color-border);
  --card-padding: var(--space-6);
  
  background-color: var(--card-bg);
  border-color: var(--card-border);
  padding: var(--card-padding);
}

/* Variante destaque */
.card--featured {
  --card-bg: var(--color-primary-light);
  --card-border: var(--color-primary);
}

/* Variante compacta */
.card--compact {
  --card-padding: var(--space-4);
}
```
