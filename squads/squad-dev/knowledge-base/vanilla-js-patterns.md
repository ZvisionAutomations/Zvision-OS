# Vanilla JS Patterns — Squad Dev

Padrões de JavaScript sem frameworks. Stack padrão da Zvision.

## Módulos ES6

```javascript
// math.js
export function calcular(a, b) {
  return a + b;
}

export const PI = 3.14159;

// main.js
import { calcular, PI } from './math.js';
```

**Regra:** Sempre usar módulos nativos. Sem CommonJS (`require`) em frontend.

## Fetch API

```javascript
async function buscarDados(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Erro ao buscar dados:', error);
    throw error; // re-throw para o chamador tratar
  }
}
```

## Event Delegation

```javascript
// Ruim — event listener em cada item
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', handleClick);
});

// Bom — delegation no container
document.querySelector('.cards-container').addEventListener('click', (e) => {
  const card = e.target.closest('.card');
  if (card) handleClick(card);
});
```

## Manipulação de DOM Segura

```javascript
// NUNCA — XSS risk
element.innerHTML = userInput;

// SEMPRE — seguro
element.textContent = userInput;

// Para HTML confiável (não de usuário)
const fragment = document.createDocumentFragment();
// ... construir DOM programaticamente
```

## Estado sem Framework

```javascript
// Padrão simples de estado reativo
const state = {
  _data: { count: 0 },
  listeners: [],
  
  get(key) {
    return this._data[key];
  },
  
  set(key, value) {
    this._data[key] = value;
    this.listeners.forEach(fn => fn(this._data));
  },
  
  subscribe(fn) {
    this.listeners.push(fn);
    return () => {
      this.listeners = this.listeners.filter(l => l !== fn);
    };
  }
};
```

## Formulários

```javascript
// Validação e submit
const form = document.querySelector('#contact-form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const data = Object.fromEntries(new FormData(form));
  
  // Validação
  if (!data.email.includes('@')) {
    showError('email', 'Email inválido');
    return;
  }
  
  // Envio
  setLoading(true);
  try {
    await enviarFormulario(data);
    showSuccess();
    form.reset();
  } catch (error) {
    showError('form', 'Erro ao enviar. Tente novamente.');
  } finally {
    setLoading(false);
  }
});
```

## Intersection Observer (animações on-scroll)

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target); // para após primeira vez
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

## Debounce e Throttle

```javascript
// Debounce — espera parar de chamar
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

// Throttle — limita frequência
function throttle(fn, limit) {
  let lastCall = 0;
  return (...args) => {
    const now = Date.now();
    if (now - lastCall >= limit) {
      lastCall = now;
      fn(...args);
    }
  };
}

// Uso
window.addEventListener('resize', debounce(handleResize, 200));
window.addEventListener('scroll', throttle(handleScroll, 100));
```
