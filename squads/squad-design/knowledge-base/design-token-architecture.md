# Knowledge Base: Design Token Architecture

## Escopo
Referencia completa de arquitetura de design tokens — taxonomia de tres niveis, W3C DTCG spec, export pipeline e governanca.

---

## 1. Three-Tier Token Architecture

### Visao Geral
```
L1 Primitive → L2 Semantic → L3 Component
   (What)        (Why)         (Where)
```

| Tier | Nome | Papel | Exemplo |
|------|------|-------|---------|
| L1 | Primitive | Raw design values | `color.blue.500: #3B82F6` |
| L2 | Semantic | Intent/purpose mapping | `color.action.primary: {color.blue.500}` |
| L3 | Component | Component-specific | `button.primary.bg: {color.action.primary}` |

### Regras de Referencia
| Regra | Descricao |
|-------|----------|
| L3 → L2 | Component tokens SEMPRE referenciam semantic |
| L2 → L1 | Semantic tokens SEMPRE referenciam primitive |
| L3 → L1 | PROIBIDO — quebra a cadeia semantica |
| L1 → L1 | PROIBIDO — primitives sao valores finais |

---

## 2. W3C Design Token Community Group (DTCG) Spec

### Formato JSON
```json
{
  "$name": "Design Tokens",
  "$description": "Token collection following W3C DTCG spec",

  "color": {
    "blue": {
      "500": {
        "$type": "color",
        "$value": "#3B82F6",
        "$description": "Primary blue"
      }
    }
  },

  "spacing": {
    "4": {
      "$type": "dimension",
      "$value": "16px",
      "$description": "Standard spacing unit"
    }
  },

  "font": {
    "size": {
      "base": {
        "$type": "dimension",
        "$value": "16px"
      }
    },
    "weight": {
      "regular": {
        "$type": "fontWeight",
        "$value": 400
      }
    }
  },

  "duration": {
    "fast": {
      "$type": "duration",
      "$value": "150ms"
    }
  }
}
```

### Tipos DTCG Suportados
| $type | Valor | Exemplo |
|-------|-------|---------|
| color | Hex, RGB, HSL | `"#3B82F6"` |
| dimension | px, rem, em | `"16px"` |
| fontFamily | String | `"Inter, sans-serif"` |
| fontWeight | Number | `400` |
| duration | ms, s | `"200ms"` |
| cubicBezier | Array [4] | `[0.4, 0, 0.2, 1]` |
| number | Number | `1.5` |
| strokeStyle | String/Object | `"solid"` |
| border | Object | `{ color, width, style }` |
| transition | Object | `{ duration, delay, timingFunction }` |
| shadow | Object/Array | `{ color, offsetX, offsetY, blur, spread }` |
| gradient | Object | `{ type, stops }` |
| typography | Object | `{ fontFamily, fontSize, fontWeight, lineHeight, letterSpacing }` |

### Alias/Reference Syntax
```json
{
  "color": {
    "action": {
      "primary": {
        "$type": "color",
        "$value": "{color.blue.500}"
      }
    }
  }
}
```

---

## 3. L1 — Primitive Tokens

### Color Palette (11 Steps)
| Step | Lightness | Uso Tipico |
|------|----------|-----------|
| 50 | Lightest | Backgrounds, subtle tints |
| 100 | Very light | Hover backgrounds |
| 200 | Light | Active backgrounds, borders |
| 300 | Medium light | Disabled states |
| 400 | Medium | Icons secondary |
| 500 | Base | Primary brand, icons |
| 600 | Medium dark | Hover on dark elements |
| 700 | Dark | Active on dark elements |
| 800 | Very dark | Text secondary |
| 900 | Darkest | Text primary |
| 950 | Near black | High-contrast text |

### Palettes Obrigatorias
| Palette | Uso |
|---------|-----|
| Gray/Neutral | Backgrounds, text, borders |
| Brand Primary | Primary actions, links |
| Brand Secondary | Supporting elements |
| Success (Green) | Positive feedback |
| Warning (Amber) | Caution states |
| Error (Red) | Destructive, errors |
| Info (Blue) | Informational |

### Spacing Scale (4px Base)
```
0, 1(4px), 2(8px), 3(12px), 4(16px), 5(20px), 6(24px),
8(32px), 10(40px), 12(48px), 16(64px), 20(80px), 24(96px)
```

### Typography Primitives
| Token | Values |
|-------|--------|
| font.family.sans | `'Inter', system-ui, sans-serif` |
| font.family.mono | `'JetBrains Mono', monospace` |
| font.size.* | 12, 14, 16, 18, 20, 24, 30, 36, 48, 60px |
| font.weight.* | 400, 500, 600, 700 |
| font.lineHeight.* | tight(1.25), normal(1.5), relaxed(1.75) |
| font.letterSpacing.* | tight(-0.025em), normal(0), wide(0.025em) |

---

## 4. L2 — Semantic Tokens

### Color Semantics
| Token | Light Mode | Dark Mode | Uso |
|-------|-----------|-----------|-----|
| bg.primary | white | gray.950 | Page background |
| bg.secondary | gray.50 | gray.900 | Section background |
| bg.tertiary | gray.100 | gray.800 | Card background |
| fg.primary | gray.900 | gray.50 | Primary text |
| fg.secondary | gray.600 | gray.400 | Secondary text |
| fg.muted | gray.400 | gray.500 | Placeholder, disabled |
| action.primary | blue.600 | blue.400 | Primary CTAs |
| action.primary.hover | blue.700 | blue.300 | Hover state |
| border.default | gray.200 | gray.700 | Default borders |
| border.strong | gray.300 | gray.600 | Emphasized borders |
| feedback.success | green.600 | green.400 | Success messages |
| feedback.error | red.600 | red.400 | Error messages |
| feedback.warning | amber.600 | amber.400 | Warning messages |

### Spacing Semantics
| Token | Value | Uso |
|-------|-------|-----|
| spacing.component.xs | space.1 (4px) | Inline gaps |
| spacing.component.sm | space.2 (8px) | Related elements |
| spacing.component.md | space.4 (16px) | Component padding |
| spacing.component.lg | space.6 (24px) | Card padding |
| spacing.section.sm | space.8 (32px) | Small sections |
| spacing.section.md | space.12 (48px) | Medium sections |
| spacing.section.lg | space.16 (64px) | Large sections |
| spacing.page | space.20 (80px) | Page sections |

---

## 5. L3 — Component Tokens

### Button Example
```json
{
  "button": {
    "primary": {
      "bg": { "$value": "{color.action.primary}" },
      "bg-hover": { "$value": "{color.action.primary.hover}" },
      "fg": { "$value": "{color.on-action.primary}" },
      "border-radius": { "$value": "{radius.md}" },
      "padding-x": { "$value": "{spacing.component.md}" },
      "padding-y": { "$value": "{spacing.component.sm}" },
      "font-size": { "$value": "{font.size.sm}" },
      "font-weight": { "$value": "{font.weight.medium}" }
    },
    "size": {
      "sm": {
        "height": { "$value": "32px" },
        "padding-x": { "$value": "{spacing.component.sm}" },
        "font-size": { "$value": "{font.size.xs}" }
      },
      "md": {
        "height": { "$value": "40px" },
        "padding-x": { "$value": "{spacing.component.md}" },
        "font-size": { "$value": "{font.size.sm}" }
      },
      "lg": {
        "height": { "$value": "48px" },
        "padding-x": { "$value": "{spacing.component.lg}" },
        "font-size": { "$value": "{font.size.base}" }
      }
    }
  }
}
```

---

## 6. Export Pipeline (Style Dictionary)

### Configuracao
```javascript
// style-dictionary.config.js
module.exports = {
  source: ['tokens/**/*.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      buildPath: 'dist/css/',
      files: [{
        destination: 'tokens.css',
        format: 'css/variables',
        options: { outputReferences: true }
      }]
    },
    typescript: {
      transformGroup: 'js',
      buildPath: 'dist/ts/',
      files: [{
        destination: 'tokens.ts',
        format: 'javascript/es6'
      }]
    },
    tailwind: {
      transformGroup: 'js',
      buildPath: 'dist/tailwind/',
      files: [{
        destination: 'theme.js',
        format: 'javascript/module-flat'
      }]
    }
  }
};
```

### Output Formats
| Formato | Arquivo | Consumer |
|---------|---------|---------|
| CSS Custom Properties | tokens.css | Browser runtime |
| TypeScript constants | tokens.ts | Type-safe JS |
| SCSS variables | _tokens.scss | Legacy SCSS |
| JSON flat | tokens.json | Tool integration |
| Tailwind theme | theme.js | tailwind.config.js |

---

## 7. Multi-Brand Theming

### Arquitetura
```
tokens/
├── core/           ← L3 (shared across all brands)
│   ├── button.json
│   └── input.json
├── semantic/       ← L2 (shared structure, may vary)
│   ├── colors.json
│   └── spacing.json
└── brands/         ← L1 (unique per brand)
    ├── brand-a/
    │   ├── colors.json
    │   └── typography.json
    └── brand-b/
        ├── colors.json
        └── typography.json
```

### Regra de Ouro
> L3 e compartilhado. L2 e estruturalmente identico. Apenas L1 varia por marca.

---

## 8. Token Governance

### Lifecycle
```
Proposal → Review → Alpha → Beta → Stable → Deprecated → Removed
```

| Stage | Regra |
|-------|-------|
| Proposal | RFC com justificativa |
| Review | Design + Dev approval |
| Alpha | Uso interno, pode mudar |
| Beta | Uso em produção limitado |
| Stable | Fully supported, SemVer |
| Deprecated | 2 minor versions notice |
| Removed | Next major version |

### Naming Convention
| Regra | Exemplo |
|-------|---------|
| kebab-case | `color-action-primary` |
| Category first | `color.`, `spacing.`, `font.` |
| No abbreviations | `background` not `bg` in token name |
| Descriptive | `color.feedback.error` not `color.red` |

---

## Referencias
- W3C Design Token Community Group Spec (2nd Editors Draft)
- Style Dictionary documentation
- Tokens Studio documentation
- Nathan Curtis — Token taxonomy articles
