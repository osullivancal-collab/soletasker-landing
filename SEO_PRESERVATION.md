# SoleTasker SEO Preservation Guardrail

Last audited: 2026-09-08
Source of truth audited: `main` at `9b9d77ac9603b434e123d480bf3823bbccaaca35`

## Purpose

Use this file during every SoleTasker marketing-site redesign. The design, hierarchy and sales copy may change substantially, but existing search intent must not disappear by accident.

**Rule: preserve search intent, not old wording.**

## Current search snapshot

On 2026-09-08, a current web search for **`voice to task for tradies`** returned SoleTasker as the first relevant result reviewed in this audit. Ranking varies by user, location and device, so this is not a guaranteed universal position, but it is strong enough to treat the query as protected intent.

## Tier 1 protected intent

Do not remove or heavily dilute these concepts from the homepage/site:

- `voice to task`
- `tradies`
- `Australian` / `Australia`
- `voice-first`
- `tasks`
- `jobs`
- `reminders`
- `sole traders`
- `small teams`

The exact phrase **`voice to task for tradies`** or a natural grammatical equivalent must remain in an SEO-significant visible location after the redesign.

## Tier 2 expansion intent

Keep these represented naturally where they truthfully describe the product:

- voice notes app for tradies
- tradie task management software
- lightweight job management
- hands-free job management
- voice capture
- job notes
- assign tasks / team assignment
- electricians
- plumbers
- builders
- HVAC / air conditioning
- carpenters
- landscapers
- photos
- certificates / certs
- invoice notes
- client intake / job intake
- Australian tradies

Do not keyword-stuff.

---

# Homepage `/`

## Strongly protected page title

Current:

```html
<title>SoleTasker — Voice to Task App for Tradies Australia</title>
```

For the first redesigned release, prefer keeping this exact title. If it changes later, the replacement should still include:

- SoleTasker
- Voice to Task
- Tradies
- Australia/Australian

Do not replace it with a vague brand-only title.

## Meta description

Current:

```html
<meta name="description" content="Say it once. Jobs, invoices, certs and reminders — captured instantly. Nothing forgotten. Built by tradies for tradies."/>
```

This wording may improve. The replacement should clearly retain product category + audience and naturally include useful concepts such as voice, tasks, tradies, Australia and jobs.

## Canonical and social metadata

Current homepage includes:

```html
<meta property="og:title" content="SoleTasker — Voice to Task for Tradies"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="https://soletasker.com.au"/>
<link rel="canonical" href="https://soletasker.com.au"/>
<meta property="og:image" content="https://soletasker.com.au/og-image.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="SoleTasker — Voice to Task for Tradies"/>
```

Preserve equivalent valid metadata.

### Existing issue

The repo root does not currently contain `og-image.png` although the homepage references it. Fix this during redesign by adding a real asset or changing the metadata to a real deployed image.

## Hero semantic requirements

Current visible hero signals include:

- `Voice-first · Phone-first`
- `LIGHTWEIGHT JOB MANAGEMENT FOR SOLE TRADERS AND SMALL TEAMS.`
- supporting text covering mic/voice, task, reminder, job linking, assignment, notes, photos and certs

The H1 **may change**. It does not need to retain the old wording.

But the redesigned above-the-fold copy must still answer:

1. What is SoleTasker?
2. Who is it for?

A vague hero such as `Run your business without the chaos` is not enough unless nearby visible text restores voice/tasks/jobs + tradies/sole traders/small trade teams.

## Visible category description

Keep at least one crawlable visible paragraph that naturally connects:

`SoleTasker` + `Australian` + `voice-to-task` + `tradies/tradespeople` + relevant trade examples.

Do not hide the only explicit product-category wording solely inside metadata/schema.

---

# Homepage FAQ and long-tail intent

The current homepage FAQ covers valuable search intents. Preserve equivalent visible coverage for at least these topics where still accurate:

1. voice notes app for tradies in Australia
2. voice to structured tasks for electricians/plumbers/builders
3. hands-free job management on site
4. simple tradie task-management software for small operators
5. invoice/certificate notes using voice
6. tracking jobs and forgotten tasks
7. client/job intake links
8. Google review requests
9. Future Work
10. SWMS
11. pricing/free trial

The exact wording is not protected. Product truth is.

---

# Structured data

The homepage currently contains `FAQPage` JSON-LD with search-oriented questions such as:

- `What is the best voice notes app for tradies in Australia?`
- `How does voice to structured tasks work for electricians, plumbers, and builders?`
- `Is there a hands-free job management app I can use on site?`
- `What is the simplest tradie task management software for small operators?`

Do not accidentally drop structured data during a full HTML rewrite.

If FAQ JSON-LD remains:

- schema answers must match visible page answers;
- do not include claims absent from or contradicted by visible copy;
- schema must describe real product functionality only;
- do not preserve unsupported statistics just for keywords.

## Use Cases schema warning

`use-cases.html` currently includes old numerical claims such as `6-10 hours a week` and `$400-$800 a month` in FAQ schema.

Those numbers are **not SEO-protected**. Remove or replace them unless properly sourced and supported by the visible page. Preserve the topic, not the unsupported statistic.

---

# Protected URLs

Do not change these public URLs without a deliberate redirect plan:

- `/`
- `/pricing`
- `/use-cases`
- `/privacy`
- `/terms`

Current Vercel routing includes:

- `/pricing` -> `/pricing.html`
- `/use-cases` -> `/use-cases.html`
- fallback -> `/index.html`

If the implementation changes framework/file structure, the public URLs must still resolve.

If a public URL is replaced, add a permanent redirect to the most relevant replacement. Do not leave indexed URLs as 404s.

Canonical URLs should use the public clean paths, not `.html`, preview, or Vercel domains.

---

# Pricing `/pricing`

Current title:

```html
<title>Pricing — SoleTasker</title>
```

Current description:

```html
<meta name="description" content="SoleTasker pricing. One plan at $29/month ex GST for Australian tradies. 7 days free, no card needed. Voice to task, job tracking, invoices, certs."/>
```

Current canonical:

```html
<link rel="canonical" href="https://soletasker.com.au/pricing"/>
```

Pricing content should remain crawlable text and continue to cover, if still commercially correct:

- SoleTasker
- $29/month ex GST
- 7-day free trial
- no card required
- Australian tradies
- voice-to-task/product category

Billing, trial and GST wording must match the actual product and legal terms.

---

# Use Cases `/use-cases`

Current title:

```html
<title>Use Cases — SoleTasker Voice to Task for Australian Tradies</title>
```

Current description:

```html
<meta name="description" content="See exactly how SoleTasker works. Speak on site, get tasks, job notes, invoices and certs drafted instantly. Built for Australian electricians, plumbers, builders and tradies."/>
```

Current canonical:

```html
<link rel="canonical" href="https://soletasker.com.au/use-cases"/>
```

Keep natural references to relevant real use cases and audiences, especially:

- electricians
- plumbers
- air conditioning / HVAC
- builders
- carpenters
- landscapers
- voice capture on site/in the van
- tasks
- job notes
- reminders
- assignment

Do not preserve stale/unsupported claims merely because they contain keywords.

---

# Legal pages

Keep `/privacy` and `/terms` accessible and internally linked.

Current titles:

- `Privacy Policy — SoleTasker`
- `Terms of Service — SoleTasker`

The current legal files do not define canonicals. Adding correct canonicals during the redesign is allowed and desirable.

---

# Internal-link guardrails

Retain crawlable `<a href>` links between core marketing pages.

Minimum expected links:

- Homepage -> Pricing
- Homepage -> Use Cases
- Homepage/footer -> Privacy
- Homepage/footer -> Terms
- Pricing -> Homepage
- Use Cases -> Homepage
- Use Cases -> Pricing

Do not replace important navigation with JavaScript-only click handlers that have no real `href`.

Signup/login buttons may point to the app, but marketing pages must still link to one another.

---

# Technical SEO issues found — improve, do not preserve

1. No `robots.txt` is present in the repository root.
2. No `sitemap.xml` is present in the repository root.
3. `og-image.png` is referenced by the homepage but is not present in the current repo root.
4. Use Cases structured data contains old unsupported numerical claims.
5. Privacy and Terms currently have no canonical tags.
6. Essential SEO copy must stay in crawlable HTML; do not move it only into screenshots, image mockups, canvas, or hidden interaction states.

These are improvement opportunities, not ranking assets.

---

# Redesign acceptance checklist

Before any redesigned branch is merged to production:

- [ ] Homepage title still carries `Voice to Task`, `Tradies`, and Australia/Australian intent.
- [ ] Homepage has one clear crawlable H1.
- [ ] Above-the-fold visible copy says what SoleTasker does and who it serves.
- [ ] `voice to task for tradies` intent remains visible somewhere meaningful.
- [ ] Australia/Australian remains associated with product/audience.
- [ ] Voice, tasks, jobs and reminders remain represented in visible text.
- [ ] Sole traders/small teams remain represented.
- [ ] One visible paragraph explains SoleTasker as an Australian voice-to-task product for tradies/tradespeople.
- [ ] Core FAQ/search intents remain represented.
- [ ] FAQ schema, if present, matches visible copy.
- [ ] `/pricing` resolves and retains a correct canonical.
- [ ] `/use-cases` resolves and retains a correct canonical.
- [ ] `/privacy` resolves.
- [ ] `/terms` resolves.
- [ ] No indexed URL is removed without a permanent redirect.
- [ ] Internal links use real `href` values.
- [ ] Social metadata remains valid.
- [ ] OG image URL points to a real deployed asset.
- [ ] Pricing/trial/GST wording matches actual billing.
- [ ] Unsupported statistics are not carried forward merely for SEO.
- [ ] Mobile and desktop expose the same essential semantic text.

## Recommended additions before launch

- [ ] Add `robots.txt`.
- [ ] Add `sitemap.xml` for `/`, `/pricing`, `/use-cases`, `/privacy`, `/terms` as appropriate.
- [ ] Add canonical tags to legal pages.
- [ ] Validate structured data after redesign.
- [ ] Verify no accidental `noindex`, `nofollow` or robots blocking.
- [ ] Check deployed titles/descriptions.
- [ ] Crawl internal links for 404s/broken routes.

---

# Post-redesign monitoring

For 4-6 weeks after a substantial production redesign, monitor rather than repeatedly rewriting copy based on daily movement.

Priority query:

- `voice to task for tradies`

Secondary query groups:

- voice notes app for tradies Australia
- tradie task management software Australia
- voice task app for electricians/plumbers
- lightweight job management for sole traders
- voice capture job notes tradies

Before launch, record the baseline in Google Search Console if available. After Google recrawls the new site, compare impressions, clicks, average position and indexed pages.

Do not judge SEO solely from one manual Google search because results vary by location, history, device and data centre.

---

# Locked redesign principle

The new SoleTasker website may become more product-focused, feature-rich and visually sophisticated.

**It must not become generic SaaS copy at the cost of the niche search language already identifying SoleTasker as an Australian voice-to-task product for tradies.**

Design freedom: high.
Copy freedom: high.
SEO intent removal: requires an explicit decision, not an accidental redesign side effect.
