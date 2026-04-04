# Knowledge Base: Component API Patterns

## Escopo
Referencia de padroes de API de componentes React — props design, composicao, variantes, acessibilidade built-in e versionamento.

---

## 1. Principios de API Design

### Minimal Surface Area
| Principio | Descricao |
|-----------|----------|
| Fewer props | Expor apenas o necessario |
| Sensible defaults | Valores default que funcionam para 80% dos casos |
| Progressive disclosure | API simples no basico, poderosa quando necessario |
| Composition over configuration | Preferir composicao a props complexas |
| Consistent naming | Mesmos nomes para mesmos conceitos |

### API Checklist
| Check | Criterio |
|-------|---------|
| Necessidade | Esse prop e realmente necessario? |
| Default | Tem um default razoavel? |
| Naming | O nome e claro e consistente? |
| Type safety | TypeScript type e preciso? |
| A11y | Acessibilidade e built-in? |
| Composability | Funciona bem com outros componentes? |

---

## 2. Prop Patterns

### Variant Pattern (CVA)
```typescript
import { cva, type VariantProps } from 'class-variance-authority';

const buttonVariants = cva(
  // Base classes
  'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2',
  {
    variants: {
      variant: {
        primary: 'bg-primary text-primary-foreground hover:bg-primary/90',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        outline: 'border border-input bg-background hover:bg-accent',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        sm: 'h-8 px-3 text-xs',
        md: 'h-10 px-4 text-sm',
        lg: 'h-12 px-6 text-base',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
);

type ButtonVariants = VariantProps<typeof buttonVariants>;
```

### Polymorphic Component (asChild)
```typescript
import { Slot } from '@radix-ui/react-slot';

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    ButtonVariants {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button';
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = 'Button';
```

### Compound Component Pattern
```typescript
// Compound components para composicao flexivel
const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('rounded-lg border bg-card', className)} {...props} />
  )
);

const CardHeader = React.forwardRef<HTMLDivElement, CardHeaderProps>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('flex flex-col space-y-1.5 p-6', className)} {...props} />
  )
);

const CardTitle = React.forwardRef<HTMLParagraphElement, CardTitleProps>(
  ({ className, ...props }, ref) => (
    <h3 ref={ref} className={cn('text-2xl font-semibold', className)} {...props} />
  )
);

const CardContent = React.forwardRef<HTMLDivElement, CardContentProps>(
  ({ className, ...props }, ref) => (
    <div ref={ref} className={cn('p-6 pt-0', className)} {...props} />
  )
);

// Uso:
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
  </CardHeader>
  <CardContent>Content</CardContent>
</Card>
```

### Render Props / Children as Function
```typescript
interface DataTableProps<T> {
  data: T[];
  columns: ColumnDef<T>[];
  renderEmpty?: () => React.ReactNode;
  renderRow?: (item: T, index: number) => React.ReactNode;
}
```

---

## 3. Accessibility Built-in

### ARIA por Default
```typescript
// Button com a11y built-in
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'destructive';
  loading?: boolean;
  disabled?: boolean;
}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ loading, disabled, children, ...props }, ref) => {
    return (
      <button
        ref={ref}
        disabled={disabled || loading}
        aria-disabled={disabled || loading}
        aria-busy={loading}
        {...props}
      >
        {loading && <Spinner aria-hidden="true" />}
        {loading ? <span className="sr-only">Loading...</span> : null}
        {children}
      </button>
    );
  }
);
```

### Focus Management Built-in
```typescript
// Dialog com focus trap automatico
const Dialog = ({ open, onClose, children }) => {
  const dialogRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (open) {
      // Trap focus inside dialog
      const focusableElements = dialogRef.current?.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      focusableElements?.[0]?.focus();
    }
  }, [open]);

  return (
    <div
      ref={dialogRef}
      role="dialog"
      aria-modal="true"
      aria-labelledby="dialog-title"
    >
      {children}
    </div>
  );
};
```

---

## 4. Prop Naming Conventions

### Padrao de Nomes
| Convencao | Exemplo | Anti-pattern |
|-----------|---------|-------------|
| Boolean: is/has prefix | `isOpen`, `hasError` | `open` (ambiguo) |
| Event: on prefix | `onChange`, `onSubmit` | `handleChange` |
| Render: render prefix | `renderHeader`, `renderEmpty` | `header` (conflito HTML) |
| Variant: nome descritivo | `variant="primary"` | `type="1"` |
| Size: scale semantica | `size="md"` | `size={40}` (magic number) |
| Children: React pattern | `children`, `asChild` | `content` (quando children funciona) |

### Props Proibidas
| Anti-pattern | Problema | Alternativa |
|-------------|---------|------------|
| `style` prop | Quebra design system | `className` com CN |
| `color` (string livre) | Valores arbitrarios | `variant` com opcoes |
| Nested objects | API complexa | Compound components |
| `type` generico | Conflito com HTML attr | `variant` |
| Boolean overload | `primary && !secondary` | Union type variant |

---

## 5. TypeScript Patterns

### Discriminated Unions
```typescript
// Melhor que props opcionais confusas
type AlertProps =
  | { variant: 'success'; action?: string; onAction?: () => void }
  | { variant: 'error'; retry?: boolean; onRetry?: () => void }
  | { variant: 'warning'; dismissable?: boolean }
  | { variant: 'info' };
```

### Strict Event Handlers
```typescript
interface InputProps {
  onChange: (value: string) => void;  // Simplified
  // NOT: onChange: React.ChangeEventHandler<HTMLInputElement>
  // Reason: consumer doesn't need to know implementation detail
}
```

### Generic Components
```typescript
interface SelectProps<T extends string> {
  value: T;
  onChange: (value: T) => void;
  options: { value: T; label: string }[];
}

// Usage: <Select<'sm' | 'md' | 'lg'> value="md" ... />
```

---

## 6. Composition Patterns

### Slot Pattern
```typescript
// Permite override de qualquer parte do componente
interface AlertProps {
  icon?: React.ReactNode;     // Slot: custom icon
  title: string;
  description?: string;
  action?: React.ReactNode;   // Slot: custom action
}

const Alert = ({ icon, title, description, action }: AlertProps) => (
  <div role="alert">
    {icon && <div className="alert-icon">{icon}</div>}
    <div>
      <h4>{title}</h4>
      {description && <p>{description}</p>}
    </div>
    {action && <div className="alert-action">{action}</div>}
  </div>
);
```

### Provider Pattern
```typescript
// Context para configuracao global
const ThemeProvider = ({ theme, children }) => (
  <ThemeContext.Provider value={theme}>
    {children}
  </ThemeContext.Provider>
);

// Components leem do context automaticamente
const Button = () => {
  const theme = useTheme(); // Reads from provider
  // ...
};
```

---

## 7. Versionamento de API

### SemVer para Componentes
| Mudanca | Version Bump | Exemplo |
|---------|-------------|---------|
| New optional prop | MINOR | Add `loading` prop |
| New variant option | MINOR | Add `ghost` variant |
| Default change | MINOR (com cuidado) | Change default size |
| Rename prop | MAJOR | `isOpen` → `open` |
| Remove prop | MAJOR | Remove `color` prop |
| Change prop type | MAJOR | `size: string` → `size: enum` |
| Remove variant | MAJOR | Remove `flat` variant |

### Deprecation Process
```typescript
interface ButtonProps {
  /** @deprecated Use `variant` instead. Will be removed in v3.0 */
  color?: 'primary' | 'secondary';
  variant?: 'primary' | 'secondary' | 'ghost';
}

const Button = ({ color, variant, ...props }: ButtonProps) => {
  if (color && !variant) {
    console.warn('Button: `color` prop is deprecated. Use `variant` instead.');
    variant = color;
  }
  // ...
};
```

---

## 8. Component Quality Checklist

| Criterio | Verificacao |
|----------|-----------|
| TypeScript strict | Todas as props tipadas, sem `any` |
| forwardRef | Sim, para composicao |
| displayName | Definido para DevTools |
| className merge | Usa `cn()` para merge |
| Default props | Sensible defaults definidos |
| A11y built-in | ARIA attributes, keyboard, focus |
| Dark mode | Funciona em ambos os temas |
| Responsive | Adapta a todos os breakpoints |
| Loading state | Suporta loading quando aplicavel |
| Error state | Suporta error quando aplicavel |
| Documentation | Storybook stories completas |
| Tests | Unit + a11y + visual regression |

---

## Referencias
- shadcn/ui — Component patterns reference
- Radix UI — Primitive component APIs
- React Aria (Adobe) — Accessible component hooks
- CVA documentation — Variant management
