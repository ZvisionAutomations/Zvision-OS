# HTML Page Template — Squad Dev

Template base para páginas web da Zvision. Copiar e adaptar.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="[Descrição da página — máx. 160 caracteres]" />
  
  <!-- Open Graph -->
  <meta property="og:title" content="[Título da página]" />
  <meta property="og:description" content="[Descrição OG]" />
  <meta property="og:image" content="/assets/og-image.jpg" />
  <meta property="og:url" content="[URL da página]" />
  <meta property="og:type" content="website" />
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="[Título]" />
  <meta name="twitter:description" content="[Descrição]" />
  
  <title>[Título da Página] — Zvision</title>
  
  <!-- Preconnect para fonts externas -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  
  <!-- CSS -->
  <link rel="stylesheet" href="/css/styles.css" />
  
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg" />
</head>
<body>

  <!-- Skip link para acessibilidade -->
  <a href="#main-content" class="skip-link">Pular para o conteúdo principal</a>

  <!-- Header / Nav -->
  <header class="site-header" role="banner">
    <nav class="container" aria-label="Navegação principal">
      <a href="/" class="logo" aria-label="Zvision — Página inicial">
        <!-- Logo SVG ou img com alt -->
      </a>
      
      <button 
        class="nav-toggle" 
        aria-expanded="false" 
        aria-controls="nav-menu"
        aria-label="Abrir menu de navegação"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>
      
      <ul id="nav-menu" class="nav-menu" role="list">
        <li><a href="#sobre" class="nav-link">Sobre</a></li>
        <li><a href="#servicos" class="nav-link">Serviços</a></li>
        <li><a href="#contato" class="nav-link btn btn-primary">Contato</a></li>
      </ul>
    </nav>
  </header>

  <!-- Main Content -->
  <main id="main-content">

    <!-- Hero -->
    <section class="hero" aria-labelledby="hero-heading">
      <div class="container">
        <h1 id="hero-heading">[Headline principal]</h1>
        <p class="hero-subtitle">[Subheadline]</p>
        <a href="#contato" class="btn btn-primary btn-lg">
          [CTA Principal]
        </a>
      </div>
    </section>

    <!-- Seção de conteúdo -->
    <section class="section" aria-labelledby="section-heading">
      <div class="container">
        <h2 id="section-heading">[Título da seção]</h2>
        <!-- conteúdo -->
      </div>
    </section>

    <!-- Formulário de Contato -->
    <section id="contato" class="section contact-section" aria-labelledby="contact-heading">
      <div class="container">
        <h2 id="contact-heading">Entre em contato</h2>
        
        <form id="contact-form" novalidate>
          <div class="form-group">
            <label for="name">Nome</label>
            <input 
              type="text" 
              id="name" 
              name="name" 
              required 
              autocomplete="name"
              aria-describedby="name-error"
            />
            <span id="name-error" class="form-error" role="alert" hidden></span>
          </div>
          
          <div class="form-group">
            <label for="email">Email</label>
            <input 
              type="email" 
              id="email" 
              name="email" 
              required 
              autocomplete="email"
              aria-describedby="email-error"
            />
            <span id="email-error" class="form-error" role="alert" hidden></span>
          </div>
          
          <div class="form-group">
            <label for="message">Mensagem</label>
            <textarea 
              id="message" 
              name="message" 
              rows="4" 
              required
              aria-describedby="message-error"
            ></textarea>
            <span id="message-error" class="form-error" role="alert" hidden></span>
          </div>
          
          <button type="submit" class="btn btn-primary">
            <span class="btn-text">Enviar mensagem</span>
            <span class="btn-loading" hidden aria-hidden="true">Enviando...</span>
          </button>
        </form>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <p>&copy; <span id="current-year"></span> Zvision. Todos os direitos reservados.</p>
    </div>
  </footer>

  <!-- Scripts -->
  <script type="module" src="/js/main.js"></script>

</body>
</html>
```
