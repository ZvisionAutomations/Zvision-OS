# CSS Variables System — Squad Dev

Sistema de design tokens via CSS custom properties. Padrão obrigatório na Zvision.

## Definição dos Tokens (`:root`)

```css
:root {
  /* === CORES === */
  /* Brand */
  --color-primary: #6366F1;
  --color-primary-hover: #4F46E5;
  --color-primary-light: #E0E7FF;
  --color-secondary: #10B981;
  --color-secondary-hover: #059669;
  
  /* Neutros */
  --color-bg: #FFFFFF;
  --color-bg-subtle: #F9FAFB;
  --color-surface: #F3F4F6;
  --color-border: #E5E7EB;
  --color-border-strong: #D1D5DB;
  
  /* Texto */
  --color-text: #111827;
  --color-text-secondary: #6B7280;
  --color-text-muted: #9CA3AF;
  --color-text-inverse: #FFFFFF;
  
  /* Semânticas */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  --color-info: #3B82F6;
  
  /* Focus */
  --color-focus: #6366F1;
  --color-focus-ring: rgba(99, 102, 241, 0.3);

  /* === TIPOGRAFIA === */
  --font-family-base: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-family-mono: 'Fira Code', 'Cascadia Code', Consolas, monospace;
  
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  --font-size-5xl: 3rem;      /* 48px */
  
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;

  /* === ESPAÇAMENTO === */
  /* Base: 4px */
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
  --space-20: 5rem;     /* 80px */
  --space-24: 6rem;     /* 96px */

  /* === BORDAS === */
  --radius-sm: 0.25rem;  /* 4px */
  --radius-md: 0.5rem;   /* 8px */
  --radius-lg: 0.75rem;  /* 12px */
  --radius-xl: 1rem;     /* 16px */
  --radius-full: 9999px; /* pill */
  
  --border-width: 1px;
  --border-width-2: 2px;

  /* === SOMBRAS === */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);

  /* === TRANSIÇÕES === */
  --transition-fast: 150ms ease-out;
  --transition-base: 200ms ease-out;
  --transition-slow: 300ms ease-out;

  /* === LAYOUT === */
  --container-max: 1280px;
  --container-padding: var(--space-4);
  
  /* === Z-INDEX === */
  --z-base: 0;
  --z-above: 10;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-toast: 500;
}
```

## Dark Mode

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0F172A;
    --color-bg-subtle: #1E293B;
    --color-surface: #334155;
    --color-border: #334155;
    --color-border-strong: #475569;
    --color-text: #F1F5F9;
    --color-text-secondary: #94A3B8;
    --color-text-muted: #64748B;
  }
}
```

## Uso Correto

```css
/* CORRETO */
.button {
  background-color: var(--color-primary);
  color: var(--color-text-inverse);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  transition: background-color var(--transition-fast);
}

.button:hover {
  background-color: var(--color-primary-hover);
}

/* ERRADO — hardcoded */
.button {
  background-color: #6366F1; /* ❌ */
  padding: 12px 24px;        /* ❌ */
  border-radius: 8px;        /* ❌ */
}
```

## Container Padrão

```css
.container {
  width: 100%;
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: var(--container-padding);
}

@media (min-width: 640px) {
  .container {
    --container-padding: var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container {
    --container-padding: var(--space-8);
  }
}
```
