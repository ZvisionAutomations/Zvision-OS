# Knowledge Base: SEO Technical Reference

## Core Web Vitals (2026)
| Metric | Good | Needs Improvement | Poor | What It Measures |
|--------|------|-------------------|------|-----------------|
| LCP | < 2.5s | 2.5s - 4.0s | > 4.0s | Loading performance |
| INP | < 200ms | 200ms - 500ms | > 500ms | Interactivity |
| CLS | < 0.1 | 0.1 - 0.25 | > 0.25 | Visual stability |

## On-Page SEO Checklist

### Title Tag
- Length: 50-60 characters
- Primary keyword near beginning
- Brand name at end (optional)
- Unique per page
- Compelling for CTR

### Meta Description
- Length: 150-160 characters
- Include primary keyword naturally
- Include call-to-action
- Unique per page
- Match search intent

### Headings
- One H1 per page (primary keyword)
- H2s for main sections (secondary keywords)
- H3s for subsections
- Logical hierarchy (never skip levels)
- Descriptive, not generic

### URL Structure
- Short and descriptive
- Include primary keyword
- Lowercase, hyphens between words
- No special characters or parameters
- Flat hierarchy preferred (/category/page)

## Schema.org / Structured Data

### Essential Schema Types
| Type | Use Case | Rich Result |
|------|---------|-------------|
| Article | Blog posts, news | Article rich result |
| Product | E-commerce products | Product snippet, price |
| FAQ | FAQ sections | FAQ accordion in SERP |
| HowTo | Tutorials, guides | Step-by-step in SERP |
| BreadcrumbList | Navigation path | Breadcrumb trail |
| Organization | Company info | Knowledge panel |
| LocalBusiness | Local businesses | Local pack |
| Review | Product/service reviews | Star ratings |
| Event | Events, webinars | Event listing |
| VideoObject | Video content | Video carousel |

### JSON-LD Template
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "description": "Article description",
  "image": "https://example.com/image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Company Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2026-03-13",
  "dateModified": "2026-03-13"
}
</script>
```

## Technical SEO

### Crawlability
| Check | Implementation |
|-------|---------------|
| robots.txt | Allow important pages, block admin/internal |
| XML Sitemap | All indexable pages, < 50K URLs per file |
| Sitemap index | Link multiple sitemaps if needed |
| Internal linking | Every page reachable within 3 clicks |
| Crawl budget | Prioritize important pages |
| Canonical tags | Self-referencing on all pages |

### Indexation
| Check | Implementation |
|-------|---------------|
| Index coverage | Monitor in Search Console |
| Noindex tags | Only on pages that shouldn't be indexed |
| Thin content | Min 300 words for indexable pages |
| Duplicate content | Canonicals, consolidation |
| Pagination | rel="next/prev" or infinite scroll |
| Hreflang | For multi-language sites |

### Site Architecture
```
Homepage (most authority)
├── Category 1 (pillar page)
│   ├── Subcategory 1a
│   │   ├── Article 1a-1
│   │   └── Article 1a-2
│   └── Subcategory 1b
├── Category 2 (pillar page)
│   ├── Article 2-1
│   └── Article 2-2
└── Supporting Pages
    ├── About
    ├── Contact
    └── FAQ
```

## Topic Clusters (SEO Content Strategy)

### Structure
```
PILLAR PAGE (broad topic, 3000+ words)
    │
    ├── Cluster Article 1 (specific subtopic, 1500+ words)
    ├── Cluster Article 2 (specific subtopic)
    ├── Cluster Article 3 (specific subtopic)
    ├── Cluster Article 4 (specific subtopic)
    └── Cluster Article 5 (specific subtopic)

All cluster articles link TO pillar and FROM pillar.
Cluster articles may interlink with each other.
```

### Keyword Intent Types
| Intent | Signal Words | Content Type | Funnel Stage |
|--------|-------------|-------------|-------------|
| Informational | how, what, why, guide | Blog, guide, video | Awareness |
| Navigational | [brand name], login | Homepage, product page | — |
| Commercial | best, review, comparison | Comparison, review | Consideration |
| Transactional | buy, price, discount, near me | Product, pricing page | Decision |

## E-E-A-T (Google Quality Guidelines)

### Experience
- First-hand experience with topic
- Original photos/videos
- Personal anecdotes and case studies

### Expertise
- Author credentials visible
- Author bio with qualifications
- Topical authority (many related articles)

### Authoritativeness
- Backlinks from authoritative sources
- Citations and references
- Industry recognition

### Trustworthiness
- HTTPS
- Clear contact information
- Privacy policy, terms of service
- Accurate, up-to-date content
- Transparent editorial process

## Link Building Strategies
| Strategy | Difficulty | Impact | Scalability |
|---------|-----------|--------|------------|
| Original research/data | High | Very High | Low |
| Guest posting | Medium | Medium | Medium |
| Broken link building | Medium | Medium | Medium |
| Digital PR | High | Very High | Low |
| Resource page outreach | Low | Medium | Medium |
| HARO/journalist queries | Low | High | Medium |
| Skyscraper technique | Medium | High | Low |
| Infographics | Medium | Medium | Low |
| Partnerships | Medium | High | Low |

## SEO Tools Reference
| Category | Tools |
|----------|-------|
| All-in-one | Ahrefs, SEMrush, Moz Pro |
| Technical | Screaming Frog, Sitebulb, DeepCrawl |
| Keywords | Ahrefs Keywords Explorer, Google Keyword Planner |
| Content | Surfer SEO, Clearscope, MarketMuse |
| Speed | PageSpeed Insights, GTmetrix, WebPageTest |
| Rank tracking | Ahrefs Rank Tracker, SERPWatcher |
| Schema | Schema.org validator, Rich Results Test |
| Free | Google Search Console, Google Analytics 4 |
