# SoleTasker Marketing Website — Canonical Redesign Direction

Last updated: 2026-09-08

This file is the canonical design/implementation handoff for the SoleTasker marketing-site redesign.

If another AI/dev session works on `soletasker-landing`, read this file **before changing design or copy**, then read `SEO_PRESERVATION.md`.

---

## 1. Repository safety and source of truth

There are two separate repositories:

### Marketing website

`osullivancal-collab/soletasker-landing`

- This is the marketing website.
- `main` is the functional source of truth.
- Preserve working navigation, Login behaviour, signup CTAs, legal routes, pricing route, use-cases route and existing production functionality unless a change is explicitly approved.
- Redesign work must be developed on an isolated branch / preview.
- **Do not merge redesign implementation to `main` without explicit approval from Callan.**

### Product app

`osullivancal-collab/soletasker-app`

- This is the actual SoleTasker application.
- The landing-site redesign must not casually modify the app repo.
- Verify marketed features against the real app before advertising them.

---

## 2. Current redesign status

Open draft PR #4: `Hero redesign preview`

Branch: `redesign/hero-v1`

This is an isolated hero experiment/review preview only. It is **not approved final design** and must not be merged simply because it exists.

Use it as implementation context, not as permission to lock that direction.

---

## 3. Product truth

SoleTasker is a **lightweight, phone-first, voice-first job and admin web app for Australian sole traders and small trade teams**.

The core promise is quick capture and simple follow-through:

- speak what needs doing
- create a task or reminder
- link work to a job
- assign a task to yourself, partner, admin or worker
- keep useful job information together
- reduce reliance on memory and scattered notes

SoleTasker is deliberately lighter than large field-service platforms such as ServiceM8.

### Do not invent capabilities

Do not claim or imply features that are not in the real app, including:

- full scheduling
- dispatch
- route optimisation
- full CRM
- accounting
- Xero integration
- automatic invoicing
- automatic certificate generation
- complex workforce management

If uncertain whether a feature exists, verify it against `soletasker-app` before adding it to marketing copy.

---

## 4. Real product capabilities that may be marketed

Use the real product as the visual and factual source.

Relevant V1 areas include:

- Voice Capture
- Tasks
- Reminders
- task priority
- task assignment
- My Day task planning
- Jobs
- job scope
- site notes
- unfinished items
- invoice notes
- certificate notes
- email notes
- photos / plans / documents
- Doc Scan / work-order capture
- client/job intake link
- review request workflow
- Future Work
- SWMS where applicable to the real app
- contact actions such as email / call / SMS / maps where implemented

Marketing wording must stay accurate to what the app actually does.

---

## 5. Primary audience

Primary:

- Australian electricians
- sole traders
- very small trade businesses
- owner + partner/admin/worker setups

Secondary examples may include:

- plumbers
- HVAC / air-conditioning technicians
- builders
- carpenters
- landscapers
- similar small trade operators

Avoid fake broad-enterprise positioning.

---

## 6. Positioning

The site should communicate:

**Lightweight job admin for tradies who do not want a heavy field-service system.**

The product is useful because it helps someone capture something quickly, attach it to the right job/workflow, assign it where needed and find it again later.

Voice is a major differentiator, but the website should not make SoleTasker look like a novelty voice-note app only.

The redesigned site should communicate both:

1. the **voice-first capture advantage**; and
2. the broader **job/admin organisation product**.

---

## 7. Copy direction

Move away from overly pain-heavy tradie copy and generic SaaS slogans.

### Preferred tone

- direct
- concise
- practical
- product-led
- confident without hype
- recognisably Australian without forced slang
- suitable for a serious small-business tool

### Avoid

- patronising tradie jokes
- fake humour
- "chaos" clichés
- excessive pain-point storytelling
- exaggerated time/money-saving claims
- generic AI language
- vague lines that could belong to any SaaS product
- long paragraphs explaining obvious UI

### Strong copy pattern

Short factual lines that show workflow and purpose, e.g. concepts like:

- speak it
- create it
- assign it
- link it to the job
- keep the details together
- see what still needs doing

These are direction, not mandatory final headlines.

### SEO requirement

Read `SEO_PRESERVATION.md` before rewriting page copy.

The redesign may become much more feature-rich and product-focused, but it must not accidentally remove the existing niche search signals around:

- voice to task
- tradies
- Australia / Australian
- tasks
- jobs
- reminders
- sole traders
- small teams

Preserve search intent, not old copy word-for-word.

---

## 8. Locked visual direction

The site should feel purpose-designed for SoleTasker, not like a generic AI SaaS template.

### Palette / identity

Use a cohesive SoleTasker system built around:

- distinctive SoleTasker blue
- deep navy
- cobalt
- teal
- white / light neutral backgrounds

The overall marketing site should lean **lighter**, even if dark product UI is shown inside device frames or selected sections.

### Signature visual motif

Use a large, soft **blue-to-teal flowing wave** / sweep as a recurring connective element through the page.

It should help sections feel like one designed experience rather than a stack of unrelated cards.

### Avoid visual "AI slop"

Do not default to:

- random floating gradient blobs
- excessive glassmorphism
- generic glowing AI orbs
- fake dashboards
- endless feature-card grids
- giant abstract 3D shapes unrelated to the product
- fake app UI that does not match SoleTasker

---

## 9. Hero direction

The hero should be product-first and immediately explain what SoleTasker is.

### Hero needs

- clear purpose/category
- clear audience
- voice-first differentiator
- strong real product visual
- primary signup CTA
- secondary "See how it works"-style CTA

### Product visual

Prefer a phone/device presentation using **real SoleTasker product UI**, not a fabricated dashboard.

The hero may use a compact voice-capture visual rather than showing a giant duplicated full app screen.

### Light/dark mockup toggle

A preferred interaction is a small sun/moon control associated with the hero phone/device.

**Important:** the toggle changes only the product UI shown inside the device/mockup.

It should **not** turn the entire marketing website between light and dark themes.

This keeps the marketing site visually consistent while showing both app appearances if useful.

---

## 10. Real screenshots and mock data

Use real app screens wherever possible.

If screenshots/mockups need demonstration data, make the data believable for an Australian electrician/tradie.

Examples:

- real-looking electrician tasks
- job addresses/suburbs such as Richmond rather than irrelevant demo locations
- plausible site notes
- plausible assignment names/roles

Do not invent product controls or functionality merely to make a screenshot look fuller.

Home and Tasks should not be presented as if they are the same experience when their product roles differ.

---

## 11. Feature/story priorities

The redesigned site should explain the actual workflow rather than dumping a list of features.

Strong content areas include:

### Voice capture

Speak what needs doing rather than stopping to type everything.

### Tasks + assignment

Create a task and assign it to yourself, partner, admin or worker.

### Jobs

Keep important job information connected to the job.

### Notes / photos / documents / outputs

Keep useful records together, including photos, cert notes, invoice notes and job notes where supported.

### My Day / what needs attention

Show how tasks can be brought into a daily view without pretending SoleTasker is a scheduling/dispatch system.

### Doc Scan

Give document scanning / work-order intake a dedicated, accurate feature treatment.

### Job intake link

Show the actual flow:

- copy/share intake link
- client submits details
- job/request arrives in SoleTasker

Avoid duplicating this story in several sections.

### Review request

Explain the lightweight review-request workflow accurately.

---

## 12. Suggested page structure

The exact composition may evolve, but a strong homepage should cover roughly:

1. Hero
2. How it works / voice-to-action workflow
3. Jobs + tasks + assignment
4. Daily organisation / My Day
5. Job details / notes / photos / outputs
6. Doc Scan
7. Job intake link
8. Trust / security where factual
9. Pricing
10. FAQ
11. Final CTA
12. Footer / legal

Do not force every topic into a card. Use varied editorial/product layouts, full-width moments, cropped app views and connected wave transitions.

---

## 13. CTA behaviour

Current intended behaviour:

### Login

Login should continue to send users to the SoleTasker app login entry point.

### Get Started / Start Free Trial

Signup-intent CTAs should go to:

`/signup`

The marketing site must not accidentally revert these CTAs to a generic app login route.

### Trial/pricing truth

Current launch model:

- AUD $29/month + GST
- 7-day free trial
- no card required to start trial
- no automatic charge at the end of the free trial
- user subscribes manually when required

Website pricing/trial language must remain aligned with the production billing implementation and legal copy.

---

## 14. Desktop and mobile

This is a responsive website redesign, not a desktop-only concept.

Every major section must be intentionally designed for:

- iPhone/mobile
- tablet where relevant
- desktop

Do not simply stack desktop cards on mobile and call it complete.

Phone-first does not mean desktop should look like an enlarged mobile screen.

---

## 15. Motion and interaction

Motion should clarify the product, not decorate it endlessly.

Good uses:

- subtle waveform movement
- product-state transitions
- controlled section reveals
- phone mockup light/dark UI switch
- simple interactive workflow demonstrations

Avoid autoplay motion that makes the page feel noisy or reduces readability/performance.

---

## 16. SEO + design relationship

The redesign is explicitly allowed to change:

- hero headline
- body copy
- section order
- visual system
- component architecture
- screenshots
- interaction model

But it must preserve the important SEO intent documented in `SEO_PRESERVATION.md`.

Do not solve SEO by keyword stuffing the hero.

Use clear product copy throughout the page so both humans and search engines understand what SoleTasker is.

---

## 17. Implementation standard

This is real implementation work.

Do not deliver inspiration cards, moodboards or static image mockups as the primary result when coding has been requested.

Expected output for redesign work:

- coded
- responsive
- interactive where useful
- isolated branch
- previewable
- functional links preserved
- no app-repo collateral changes
- no merge without explicit approval

Before presenting a preview, check mobile and desktop and verify there are no obvious console/runtime/layout errors.

---

## 18. Approval rule

A preview is not approval.

A draft PR is not approval.

A design direction discussed in chat is not permission to merge production code.

**Only merge redesign implementation after Callan explicitly approves it.**

Documentation-only guardrails may be merged when explicitly requested so other AI/dev sessions can read the same source of truth.

---

## 19. What another AI/dev should read first

For any future SoleTasker landing-site redesign session:

1. `REDESIGN_DIRECTION.md`
2. `SEO_PRESERVATION.md`
3. current `main`
4. current open redesign PRs/branches
5. `soletasker-app` only as needed to verify product truth/screens/features

Do not assume an older chat or stale branch is more authoritative than these current repo sources.
