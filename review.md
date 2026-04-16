# Me Gusta Sucre — Source of Truth
> Last updated: 2026-04-16 | Session: Full text/address review — school address corrected to Audiencia #97 across all pages; clases.html cross-sell redesigned; contacto.html redesigned (WhatsApp-only, 3-brand cards); index.html brand order fixed (School first); merchandising.html Unsplash photos

This document is the **authoritative source of truth** for the project. Any AI reading this must use it to understand the brand structure, visual system, page architecture, and pending work before making any changes.

---

## 1. Business Structure — CRITICAL

Three sub-brands under the Me Gusta Sucre umbrella. They are **operationally and physically separate**.

| Sub-brand | Location | Address | Notes |
|:---|:---|:---|:---|
| **Me Gusta Inn** | Boutique guesthouse | La Paz #571, Sucre | Separate building from Café/School |
| **Me Gusta Café** | Coffee shop | Bolivar #603, Sucre | Same building as School, two separate street entrances |
| **Me Gusta Spanish School** | Language school | Audiencia #97, Sucre | Same building as Café, two separate street entrances |

**Key rules derived from this structure:**
- NEVER say the café is "downstairs" or "next to" the inn — it is at a different address.
- Breakfast for inn guests is served **at the inn** (La Paz #571), not at the café.
- The school is the **primary business**. The inn and café are complementary.
- Cross-selling between brands is encouraged but must be accurate about locations.

---

## 2. Visual Identity

### 2.1 Me Gusta Sucre / Inn (Turismo, Hospedaje, Actividades)
**Aesthetic:** "Wanderlush / Premium Travel App" — ultra clean, highly structured.
- **Global brand colors:** White `#fafafa` / `#fff`, Carbon `#111` / `#000`, Red accent `#c9252d`
- **Inn-specific colors (hospedaje.html):** Navy `#0a1628`, Blue accent `#2563eb`, Light blue `#93c5fd`
- **UI components:**
  - Bento Grids: `grid`, border-radius `32px–40px`, edge-to-edge images
  - Clean cards: white/navy background, `box-shadow: 0 12px 40px rgba(10,22,40,0.18)`
  - Glassmorphism pills: `backdrop-filter:blur(12px)` + `background:rgba(255,255,255,0.1)` + `border:1px solid rgba(255,255,255,0.2)`
  - Spacing: generous `gap-8` to `gap-12`, padding `100px 0` per section
- **Pages:** `index.html`, `actividades.html`, `hospedaje.html`, `merchandising.html`, `contacto.html`

### 2.2 Me Gusta Spanish School
**Aesthetic:** Vibrant, youthful, institutional.
- **Colors:** Coral `#FF3B6B`, Teal `#2ECEC4`, Dark Teal `#0f2122` / `#0d2626`
- **Logo:** `images/logos/logo-me-gusta-spanish.png` (horizontal PNG, use `height:auto`)
- **Favicon:** `imagenes/favicon-clases.svg` (chat bubbles icon)
- **Page:** `clases.html` (uses inline `<style>` overrides)

### 2.3 Me Gusta Café
**Aesthetic:** Artisanal, organic, botanical.
- **Colors:** Sage Green `#5aaa6a`, Brown `#8b4513`, Espresso Dark `#2c1a0e`
- **Logo:** `images/logos/me-gusta-cafe.png` (the correct logo — circular with coffee cups)
  - Also available but NOT the main logo: `me-gusta-cafe.svg`, `me-gusta-cafe-logo.svg`
- **Buttons:** `.cafe-btn-primary` (brown) and `.cafe-btn-outline` (green)
- **Page:** `cafe.html` (uses inline `<style>` overrides in `<head>`)

---

## 3. Typography
- **Serif / Headlines:** `Fraunces` (Google Fonts) — used for all H1/H2/H3, brand names, stats
- **Sans-serif / Body:** `Plus Jakarta Sans` — used for body text, labels, buttons, eyebrows
- **Handwritten accent:** `Sacramento` — used sparingly for romantic/poetic lines

---

## 4. Page Status

| File | Brand | Status | Summary |
|:---|:---|:---|:---|
| `index.html` | Sucre (Red) | Complete | Hero + polaroid school section + Me Gusta Collection bento + footer |
| `clases.html` | School (Coral/Teal) | Complete | Custom navbar, hero with stats, cross-sell Inn banner |
| `cafe.html` | Café (Green/Brown) | Complete | Full menu embedded. Needs real prices in Bs. |
| `actividades.html` | Sucre (Red) | Complete | Wanderlush bento grid. School cross-sell banner. |
| `hospedaje.html` | Inn (Navy/Blue) | **Complete** | Full Wanderlush bento redesign. Leaflet map with verified OSM/Apple Maps coordinates. Popups on click, only Inn has permanent label. |
| `merchandising.html` | Sucre (Red) | Complete | Placeholder e-commerce. Needs real prices. |
| `contacto.html` | Sucre (Red) | Complete | Both phones listed. Webhook not connected. |

---

## 5. hospedaje.html — Full Architecture

**Color scheme:** Navy `#0a1628` (cards, dark sections), Blue `#2563eb` (CTAs, accents), Light blue `#93c5fd` (text on dark), White `#fff` (light sections).

### Section flow (top to bottom):

| Section | Background | Notes |
|:---|:---|:---|
| Announcement Bar | Red `#c9252d` | Promotes Spanish School → `clases.html` |
| Navbar | Transparent → white on scroll | `nav-active` on "Stay" link |
| **Hero** | Navy overlay on photo | `id="book"`, `min-h-screen`, letterbox bars, location glassmorphism tag (La Paz #571), stats bar, two CTAs: "See Our Rooms" → `#rooms`, "Explore More" → `#discover` |
| **Rooms** | White `#fff` | `id="rooms"`, 3-col bento grid, 4 room types (see below) |
| **Amenidades** | Light gray `#f4f4f4` | 10 cards in 5-col grid. Row 1 (5 cards): white. Row 2 (5 cards): navy. |
| **Galeria** | Navy `#0a1628` | Bento 3-col: large left (row-span-2) + 4 right. Class: `fade-up inn-gallery-grid` (single class attr — fixed bug) |
| **Reviews** | White `#fff` | 3 cards alternating navy/white/navy. ALL ARE PLACEHOLDER — need real guest reviews. |
| **Ubicacion** | Light gray `#f4f4f4` | `id="location"`. Interactive Leaflet.js map with custom category markers + 4-col POI grid (History, Culture, Food, Transport). |
| **Cross-sell** | White `#fff` | `id="discover"`. Two equal cards: Café (dark espresso bg) + School (dark teal bg). Each has its own logo. |
| **Final CTA** | Espresso dark `#1a120a` | Me Gusta Inn branding (Navy/Blue), "Book Your Stay Today", circular pill logo, two buttons: WhatsApp (Primary) + Contact Us (Secondary). |
| Footer | Dark `#111111` | Standard 4-col footer. Do NOT rebuild — reuse existing. |

### Room types (3-col bento):

| Room | Grid | Price | Bathroom | Key features |
|:---|:---|:---|:---|:---|
| Suite Colonial | span 2 | $65* | Private | King bed, balcony, "Best Room" badge |
| Patio Room | 1 col | $45* | Private | Double bed, patio view |
| Standard Room | 1 col | $35* | Shared | Twin/double, local decor |
| Shared Dorm | span 2 | $18* | Shared | 6-bed, bunk beds, kitchenette, personal locker |

*Prices are visual placeholders only — do NOT treat them as real. Real prices in Bs have not been authorized for display. Do not replace them until the user explicitly provides confirmed prices.

**Breakfast rule:** All rooms include "Breakfast at the Inn" — served at La Paz #571. Never reference the café for breakfast.

### Logo assets used:
- Café card: `images/logos/me-gusta-cafe.png`
- School card: `images/logos/logo-me-gusta-spanish.png`

---

## 6. Addresses Reference (verified 2026-04-16)

| Business | Correct Address | Phone | Email |
|:---|:---|:---|:---|
| Me Gusta Inn | La Paz #571, Sucre | +591 734 25725 | info@megustasucre.com |
| Me Gusta Café | Bolivar #603, Sucre | — | info@megustasucre.com |
| Me Gusta Spanish School | **Audiencia #97**, Sucre | +591 734 00447 | info@megustaspanish.com |
| Café hours | Mon–Sat 8:00am – 8:00pm | — | — |

**Address rule:** The Café and School share the same physical building but have different street entrances and different street addresses: Café = Bolivar #603, School = Audiencia #97. NEVER show "Bolivar #603" when referring to the school, and vice versa.

---

## 7. Pending Tasks

### High Priority (blocks deployment)
- [ ] **Real photos:** Replace ALL Unsplash/Picsum placeholders in all pages. This is the final step before launch.
- [ ] **Real room prices:** Confirm prices in Bs or USD for hospedaje.html rooms.
- [ ] **Real guest reviews:** Replace Sophie/Thomas/Anna (invented) with real Booking.com or Google reviews.
- [ ] **Webhook:** contacto.html contact is now WhatsApp-only — no form/webhook needed unless a form is re-added.

### Medium Priority
- [ ] **Café prices:** `cafe.html` needs exact prices in Bolivianos (Bs).
- [ ] **Merch prices:** `merchandising.html` needs real USD or Bs pricing.
- [ ] **E-commerce flow:** Define checkout path for merch (Gumroad / Shopify Lite / WhatsApp redirect).

### Low Priority
- [ ] **Inn coordinates:** Exact GPS for La Paz #571 not yet confirmed in Google Maps. Inn marker in `hospedaje.html` is an estimate — verify and update `setView` and `innMarker` coords once confirmed.
- [ ] **Google Maps embed (contacto.html):** Now shows "La Paz #571" with correct center. Replace placeholder place ID `0x0:0x0` with real Google Maps place ID once confirmed.
- [ ] **OG tags:** Add `og:title` and `og:description` per page (currently only `og:image` is set).

---

## 8. Rules for AI Agents

### Visual rules
- **NEVER** use default browser colors. Use `#c9252d` (red), `#0a1628` (navy), `#2563eb` (blue), or neutral elegants like `#f4f4f4`.
- **DO NOT break Wanderlush structure:** Cards must have `border-radius: 32px–40px`, diffuse shadows, generous spacing `gap-8` to `gap-12`.
- **NEVER use emojis** anywhere — not in HTML, labels, descriptions, or strips. Use plain text or SVG icons.
- **Reuse existing navbar and footer.** They are verified, responsive, and unified across pages. Do not rebuild from scratch.

### Content rules
- Breakfast at the inn is served **at the inn** — never say "at the café" or "downstairs".
- The Café and School share a building at Bolivar #603 but are separate businesses with separate entrances.
- The Inn is at La Paz #571 — a completely separate location.
- All page content is in **English** (`lang="en"`). Do not mix Spanish in the content.

### Architecture rules
- When adding cross-sell content for the school or café in other pages, use the **compact dual-card pattern** from `hospedaje.html #discover` — not full cloned sections.
- The school cross-sell in `actividades.html` uses a different pattern (panoramic banner) — do not change it without user approval.
- Eyebrow text (`.eyebrow` class) defaults to red `#c9252d`. On Inn pages, override to `style="color:#2563eb"`.
- When a section has both a `fade-up` animation class and a named layout class, put them in a **single `class` attribute** to avoid the second one overriding the first.
- **`clases.html` address exception:** The Spanish School address in `clases.html` may still read `Audiencia #97`. Do NOT change it without explicit user confirmation — it may be intentional for the school's context.
