# ThaiBridge — Production Deployment Checklist

*Target: Launch thaibridge.asia · Status: Pre-launch*

---

## 1. Folder Cleanup

### Current Files

```
thaibridge-website/
├── index.html              ← Production
├── services.html           ← Production
├── process.html            ← Production
├── about.html              ← Production
├── contact.html            ← Production
├── brand-identity.html     ← Reference (keep, do not deploy)
├── icon-concepts.html      ← Reference (keep, do not deploy)
├── brand-dna.md            ← Internal doc (keep, do not deploy)
├── service-bible.md        ← Internal doc (keep, do not deploy)
├── service-bible/          ← Internal docs (keep, do not deploy)
├── CEO_Operating_System/   ← Internal docs (keep, do not deploy)
├── DEPLOYMENT.md           ← This file
└── .git/                   ← Version control
```

### Actions

- [ ] Create `/prod/` folder containing only files to deploy
- [ ] Production files: `index.html`, `services.html`, `process.html`, `about.html`, `contact.html`
- [ ] Internal docs stay in repo but NOT in prod folder
- [ ] Remove any `.DS_Store` files from prod folder
- [ ] Verify no credentials, API keys, or personal info in HTML files

**Command:**
```bash
mkdir -p prod
cp index.html services.html process.html about.html contact.html prod/
```

---

## 2. File Optimization

### HTML Minification

- [ ] Minify HTML (remove comments, whitespace) for production
- [ ] Current total: ~1,548 lines across 5 files
- [ ] Target: ~40% reduction through minification
- [ ] Tool: HTML Minifier (online) or `html-minifier` CLI

**Command:**
```bash
npm install -g html-minifier
html-minifier --collapse-whitespace --remove-comments --minify-css true --minify-js true index.html -o prod/index.html
```

### CSS Optimization

- [ ] All CSS is inline — no external stylesheets needed (good for performance)
- [ ] Verify no unused CSS rules
- [ ] Consider extracting shared CSS to one external file for better caching across pages
- [ ] Current approach (inline CSS on each page): simpler deployment, no build step, slightly larger HTML
- [ ] External CSS approach: smaller HTML, CSS cached after first page load, needs build step
- [ ] **Decision: Keep inline CSS for V1.0 launch.** Simplicity > micro-optimization at this stage.

### Font Loading

- [ ] Google Fonts (Inter) loaded from `fonts.googleapis.com`
- [ ] Preconnect hints already in place: `<link rel="preconnect" href="https://fonts.googleapis.com">`
- [ ] Consider self-hosting Inter for faster loading and no external dependency — TODO for V1.1

### JavaScript

- [ ] All JS is inline, minimal (~15 lines per page)
- [ ] No external dependencies — no npm, no frameworks
- [ ] IntersectionObserver used for scroll animations (native browser API, no polyfill needed for modern browsers)

---

## 3. Image Optimization

### Current State

- [ ] No external images used — all visuals are inline SVG
- [ ] Hero globe: SVG inline (~40 lines)
- [ ] Service icons: SVG inline (~4 lines each)
- [ ] Favicon: SVG data URI inline

### Actions

- [ ] SVG is already optimal — no raster images to compress
- [ ] If adding photos later (Phase 2): use WebP format, compress to < 100KB, use lazy loading

---

## 4. SEO Basics

### Meta Tags — Verify on ALL pages

| Tag | Status | Notes |
|-----|:------:|-------|
| `<title>` unique per page | ✅ | All 5 pages have unique titles with brand suffix |
| `<meta description>` | ✅ | All 5 pages |
| `<meta viewport>` | ✅ | All 5 pages |
| `og:title` | ✅ | All 5 pages |
| `og:description` | ✅ | All 5 pages |
| `og:type` | ✅ | All 5 pages |
| `og:url` | ✅ | All 5 pages — needs real domain after launch |
| `twitter:card` | ✅ | All 5 pages |
| `twitter:title` | ✅ | All 5 pages |
| `twitter:description` | ✅ | All 5 pages |

### Missing SEO Elements to Add

- [ ] **favicon.ico** — fallback for older browsers (currently only SVG favicon)
- [ ] **robots.txt** — create and deploy to prod
- [ ] **sitemap.xml** — create and deploy to prod
- [ ] **Schema.org structured data** — Organization schema on homepage
- [ ] **Canonical URLs** — add `<link rel="canonical">` to each page
- [ ] **hreflang tags** — if multi-language in future (not needed for V1.0 English-only)
- [ ] **og:image** — social sharing image (create 1200×630px branded card)

### robots.txt

```
User-agent: *
Allow: /
Sitemap: https://thaibridge.asia/sitemap.xml
```

### sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://thaibridge.asia/</loc><priority>1.0</priority></url>
  <url><loc>https://thaibridge.asia/services.html</loc><priority>0.8</priority></url>
  <url><loc>https://thaibridge.asia/process.html</loc><priority>0.7</priority></url>
  <url><loc>https://thaibridge.asia/about.html</loc><priority>0.7</priority></url>
  <url><loc>https://thaibridge.asia/contact.html</loc><priority>0.8</priority></url>
</urlset>
```

### Schema.org — Organization (add to index.html `<head>`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "ThaiBridge",
  "url": "https://thaibridge.asia",
  "description": "Your local team in Thailand. No middlemen. No guesswork.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Bangkok",
    "addressCountry": "TH"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "contact@thaibridge.asia",
    "contactType": "customer service"
  }
}
</script>
```

---

## 5. Mobile Testing

### Test Matrix

| Device | Browser | Status |
|--------|---------|:------:|
| iPhone 15 (Safari) | iOS Safari | — |
| iPhone SE (Safari) | iOS Safari | — |
| Samsung Galaxy S24 | Chrome Android | — |
| iPad (Safari) | iOS Safari | — |
| MacBook Pro 14" | Chrome | ✅ Tested |
| MacBook Pro 14" | Safari | — |
| MacBook Pro 14" | Firefox | — |
| Windows 15" Laptop | Chrome | — |
| Windows 15" Laptop | Edge | — |

### Responsive Breakpoints

- [ ] 860px: Nav collapses, hero stacks, 2-column grids → 1-column
- [ ] 500px: Trust strip 5→2 columns, footer 2→1 column, contact grid 2→1 column
- [x] Both breakpoints defined in CSS — need real-device testing

### Mobile-Specific Checks

- [ ] All text readable without zooming
- [ ] Buttons large enough to tap (≥ 44px touch target — current btn padding 14px 28px = 44px height ✅)
- [ ] No horizontal scrolling on any page
- [ ] Nav menu functions correctly (links visible, CTA tappable)
- [ ] Hero globe SVG renders correctly
- [ ] Contact cards are tappable
- [ ] Footer links are tappable
- [ ] Page load time < 3 seconds on 4G

---

## 6. Browser Compatibility

### CSS Features Used — Compatibility Check

| Feature | Chrome | Safari | Firefox | Edge |
|---------|:------:|:------:|:-------:|:----:|
| CSS Grid | ✅ | ✅ | ✅ | ✅ |
| CSS Variables | ✅ | ✅ | ✅ | ✅ |
| `backdrop-filter` | ✅ | ✅ | ✅ | ✅ |
| `clamp()` | ✅ | ✅ | ✅ | ✅ |
| `aspect-ratio` | ✅ | ✅ | ✅ | ✅ |
| IntersectionObserver | ✅ | ✅ | ✅ | ✅ |
| SVG inline | ✅ | ✅ | ✅ | ✅ |
| `-webkit-backdrop-filter` | — | ✅ | — | — |
| `-webkit-font-smoothing` | — | ✅ | — | — |

### Known Issues

- [ ] `backdrop-filter` on very old Safari (≤ v13) — acceptable, degrades to solid background
- [ ] `aspect-ratio` on very old browsers — acceptable, nav and hero still functional without it
- [ ] IntersectionObserver — supported in all modern browsers. No polyfill needed.

### Testing Priority

1. Safari on iOS (primary audience: Chinese business owners — high iPhone usage)
2. Chrome on Android (secondary: Thai partners)
3. Chrome on desktop (CEO's own use)
4. Safari on macOS
5. Firefox on desktop
6. Edge on Windows

---

## 7. Domain Connection

### Current Domain
- Domain: `thaibridge.asia`
- Registrar: TODO
- DNS Provider: TODO

### DNS Configuration

- [ ] Point domain to hosting provider
- [ ] Configure CNAME or A record
- [ ] Set up `www.thaibridge.asia` → redirect to `thaibridge.asia` (or vice versa)
- [ ] SSL certificate: enable HTTPS (automatic with Cloudflare or hosting provider)
- [ ] Force HTTPS redirect

### Email Setup

- [ ] `contact@thaibridge.asia` — verify it's working
- [ ] Email forwarding to personal email (Gmail)
- [ ] SPF, DKIM records for email deliverability (if sending from domain)

---

## 8. Hosting Recommendation

### Option A: Cloudflare Pages (Recommended)

**Why:** Free. Fast CDN with Thailand edge node (Bangkok). Automatic HTTPS. Git-based deploy. Zero maintenance.

| Factor | Rating |
|--------|:------:|
| Cost | Free |
| Speed (Thailand) | Excellent — Bangkok edge node |
| HTTPS | Automatic |
| Deployment | Git push → auto deploy |
| Custom domain | Supported |
| Build step | Not required for static HTML |
| Limits | 500 builds/month, 1GB storage — more than enough |

**Setup:**
1. Connect GitHub/GitLab repo to Cloudflare Pages
2. Set build command: (none — static HTML)
3. Set output directory: `/prod` (or `/` if deploying from root)
4. Add custom domain: `thaibridge.asia`
5. Done.

### Option B: GitHub Pages

**Why:** Free. Simple. Good for static sites.

| Factor | Rating |
|--------|:------:|
| Cost | Free |
| Speed | Good — global CDN |
| HTTPS | Automatic with custom domain |
| Thailand edge | Not as strong as Cloudflare |
| Custom domain | Supported via CNAME |

### Option C: Vercel

**Why:** Excellent DX. Automatic HTTPS. Global CDN.

| Factor | Rating |
|--------|:------:|
| Cost | Free (Hobby tier) |
| Speed | Excellent |
| Thailand edge | No dedicated Bangkok edge (Singapore nearest) |

### Recommendation

**Cloudflare Pages** — best combination of price (free), Thailand performance (Bangkok edge node), and simplicity (git push to deploy).

---

## 9. Deployment Steps

### Step 1: Prepare Production Files
```bash
# Create production folder
mkdir -p prod

# Copy production HTML files
cp index.html services.html process.html about.html contact.html prod/

# Create robots.txt
cat > prod/robots.txt << 'EOF'
User-agent: *
Allow: /
Sitemap: https://thaibridge.asia/sitemap.xml
EOF

# Create sitemap.xml
cat > prod/sitemap.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://thaibridge.asia/</loc><priority>1.0</priority></url>
  <url><loc>https://thaibridge.asia/services.html</loc><priority>0.8</priority></url>
  <url><loc>https://thaibridge.asia/process.html</loc><priority>0.7</priority></url>
  <url><loc>https://thaibridge.asia/about.html</loc><priority>0.7</priority></url>
  <url><loc>https://thaibridge.asia/contact.html</loc><priority>0.8</priority></url>
</urlset>
EOF
```

### Step 2: Add SEO Elements
- [ ] Add Schema.org JSON-LD to `index.html` `<head>`
- [ ] Add canonical URLs to all 5 pages
- [ ] Add `og:image` meta tag to all pages (create image first)
- [ ] Create and add `favicon.ico` fallback

### Step 3: Test Locally
- [ ] Open all 5 pages locally in Chrome, Safari, Firefox
- [ ] Test all navigation links work
- [ ] Test all CTA buttons link correctly
- [ ] Test mobile viewport (Chrome DevTools device mode)
- [ ] Validate HTML (https://validator.w3.org/)

### Step 4: Deploy to Cloudflare Pages
- [ ] Push repo to GitHub/GitLab
- [ ] Connect Cloudflare Pages to repo
- [ ] Configure: output = `/prod`, no build command
- [ ] Add custom domain: `thaibridge.asia`
- [ ] Wait for DNS propagation (~5–60 minutes)

### Step 5: Post-Deploy Verification
- [ ] Visit `https://thaibridge.asia` — homepage loads
- [ ] Navigate all 5 pages — links work
- [ ] HTTPS active (padlock icon in browser)
- [ ] `https://thaibridge.asia/robots.txt` returns content
- [ ] `https://thaibridge.asia/sitemap.xml` returns XML
- [ ] Test on mobile device (actual phone, not simulator)
- [ ] Run Google PageSpeed Insights
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools

---

## 10. Launch Checklist

### Pre-Launch (Day Before)

- [ ] All 5 pages open without errors
- [ ] All navigation links verified
- [ ] All CTA buttons link correctly
- [ ] Mobile responsive on actual device
- [ ] Favicon displays in browser tab
- [ ] Meta tags verified on all pages
- [ ] robots.txt created
- [ ] sitemap.xml created
- [ ] Schema.org added to homepage
- [ ] Page load < 3 seconds
- [ ] HTTPS active
- [ ] `contact@thaibridge.asia` email working
- [ ] No placeholder text visible to users
- [ ] No TODO markers visible to users
- [ ] OG image created and linked

### Launch Day

- [ ] DNS propagated (verify with `dig thaibridge.asia` or browser)
- [ ] Homepage loads: `https://thaibridge.asia`
- [ ] All subpages load
- [ ] 404 page handled (custom or default)
- [ ] Google Analytics installed (or privacy-friendly alternative like Plausible)
- [ ] Submit sitemap to Google Search Console
- [ ] Request indexing in Google Search Console
- [ ] Test contact email: send test email to `contact@thaibridge.asia`
- [ ] Share with 1–2 trusted people for feedback before wider launch

### Post-Launch (Week 1)

- [ ] Monitor Google Search Console for crawl errors
- [ ] Check PageSpeed Insights score
- [ ] Fix any broken links or display issues
- [ ] Start LinkedIn company page content
- [ ] Prepare WeChat Official Account content
- [ ] Collect feedback from first visitors
- [ ] Plan V1.1 improvements

### Quick Wins After Launch

- [ ] Add Analytics (Google Analytics or Plausible)
- [ ] Create OG social sharing image (1200×630px)
- [ ] Set up email signature with ThaiBridge branding
- [ ] Create LinkedIn company page
- [ ] Register Google Business Profile (for local SEO in Bangkok)
- [ ] Set up uptime monitoring (free: Upptime or similar)

---

## Appendix: Production File Checklist

| File | Size (approx) | Minified | Notes |
|------|:------------:|:--------:|-------|
| `index.html` | ~35 KB | TODO | Homepage |
| `services.html` | ~22 KB | TODO | 5 service modules |
| `process.html` | ~17 KB | TODO | 4-step timeline |
| `about.html` | ~17 KB | TODO | Brand story + values |
| `contact.html` | ~15 KB | TODO | Contact cards + CTA |
| `robots.txt` | ~100 B | N/A | Crawl instructions |
| `sitemap.xml` | ~500 B | N/A | URL listing |
| **Total** | **~107 KB** | | Entire website |

---

*DEPLOYMENT.md · ThaiBridge Production Launch Checklist · V1.0*
*Target launch: TODO · Prepared: 2026-07-01*
