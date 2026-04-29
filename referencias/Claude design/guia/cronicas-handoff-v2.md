# Handoff — Las Crónicas Redesign + Eliminación Practical Tips
### guia.html · Me Gusta Sucre · Abril 2026

---

## Resumen de cambios

1. **Eliminar** sección `#tips` (Practical Tips — 4 cards oscuras)
2. **Reemplazar** sección `#cronicas` con lista editorial numerada (5 artículos)
3. **Nuevo artículo 01** "Todo lo que necesitas saber" absorbe la info práctica

---

## CSS — añadir en `style.css`

```css
/* ── Blog Section (Las Crónicas) ── */
.blog-section {
  padding: 120px 0 140px;
  background: #fdf6ec;
  border-top: 1px solid #e8dfd0;
}
.blog-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 48px;
}
.blog-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 40px;
  margin-bottom: 64px;
  padding-bottom: 40px;
  border-bottom: 1px solid #e8dfd0;
}
.blog-eyebrow {
  font-size: 11px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #c9252d; margin-bottom: 14px;
}
.blog-title {
  font-family: 'Fraunces', serif;
  font-size: clamp(2.8rem, 4vw, 4rem);
  font-weight: 800; color: #111; line-height: 1.05;
}
.blog-title em { color: #c9252d; font-style: italic; }
.blog-sub {
  font-size: 15px; color: #888;
  max-width: 320px; line-height: 1.8; padding-bottom: 6px;
}

/* ── Article list rows ── */
.article-list { display: flex; flex-direction: column; }

.article-row {
  display: grid;
  grid-template-columns: 72px 260px 1fr 100px;
  align-items: stretch;
  text-decoration: none;
  border-top: 1px solid #e8dfd0;
  transition: background 0.2s;
  min-height: 160px;
}
.article-row:last-child { border-bottom: 1px solid #e8dfd0; }
.article-row:hover { background: #fff; }
.article-row.dark-row { background: #111; }
.article-row.dark-row:hover { background: #1a1a1a; }

.art-num {
  display: flex; align-items: center; justify-content: center;
  font-family: 'Fraunces', serif; font-size: 3.5rem; font-weight: 800;
  color: rgba(0,0,0,0.07); border-right: 1px solid #e8dfd0;
}
.dark-row .art-num {
  color: rgba(255,255,255,0.06);
  border-right-color: rgba(255,255,255,0.07);
}

.art-img {
  position: relative; overflow: hidden;
  border-right: 1px solid #e8dfd0;
}
.art-img img {
  width: 100%; height: 100%; object-fit: cover;
  transition: transform 0.7s cubic-bezier(0.25,0.46,0.45,0.94);
}
.article-row:hover .art-img img { transform: scale(1.05); }
.dark-row .art-img img { opacity: 0.55; }

.art-body {
  padding: 28px 36px;
  display: flex; flex-direction: column; justify-content: center;
  border-right: 1px solid #e8dfd0;
}
.dark-row .art-body { border-right-color: rgba(255,255,255,0.07); }

.art-tag {
  font-size: 9px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #c9252d; margin-bottom: 10px;
}
.art-title {
  font-family: 'Fraunces', serif;
  font-size: 1.45rem; font-weight: 800;
  color: #111; line-height: 1.15; margin-bottom: 10px;
}
.dark-row .art-title { color: #fff; }

.art-desc {
  font-size: 13.5px; color: #777; line-height: 1.8;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.dark-row .art-desc { color: rgba(255,255,255,0.4); }

.art-arrow {
  display: flex; align-items: center; justify-content: center;
  font-size: 22px; color: #e8dfd0;
  transition: color 0.2s, transform 0.2s;
}
.article-row:hover .art-arrow { color: #c9252d; transform: translateX(4px); }
.dark-row .art-arrow { color: rgba(255,255,255,0.1); }
.dark-row:hover .art-arrow { color: #c9252d; }

/* Responsive */
@media (max-width: 900px) {
  .blog-inner { padding: 0 24px; }
  .blog-header { flex-direction: column; align-items: flex-start; gap: 20px; }
  .article-row { grid-template-columns: 48px 140px 1fr 56px; min-height: 130px; }
  .art-num { font-size: 2.5rem; }
  .art-body { padding: 20px; }
  .art-title { font-size: 1.15rem; }
}
@media (max-width: 600px) {
  .article-row { grid-template-columns: 1fr; min-height: auto; }
  .art-num, .art-arrow { display: none; }
  .art-img { height: 200px; border-right: none; }
  .art-body { border-right: none; }
}
```

---

## HTML — cambios en guia.html

### PASO 1: Eliminar sección #tips completa

```html
<!-- ELIMINAR DESDE AQUÍ -->
<section id="tips" style="padding:100px 0;background:#111">
  ...
</section>
<!-- HASTA AQUÍ -->
```

### PASO 2: Reemplazar sección #cronicas completa

```html
<!-- ═══ LAS CRÓNICAS ════════════════════════════════════ -->
<section id="cronicas" class="blog-section">
  <div class="blog-inner">

    <div class="blog-header">
      <div>
        <p class="blog-eyebrow" data-i18n="guia.cronEyebrow">Las Crónicas</p>
        <h2 class="blog-title">
          El <em data-i18n="guia.cronAccent">Blog</em><br>
          <span data-i18n="guia.cronTitle">de Sucre</span>
        </h2>
      </div>
      <p class="blog-sub" data-i18n="guia.cronSub">Fifteen years in Sucre teach you things no algorithm knows. Here we share them.</p>
    </div>

    <div class="article-list">

      <!-- 01 Todo lo que necesitas saber — dark -->
      <div class="article-row dark-row modal-card"
        data-modal-tag="Practical Info"
        data-modal-desc="Altitude: 2,810m — gentle enough to acclimatize in a day. Take it slow the first 24 hours. Currency: Boliviano (Bs). 1 USD ≈ 6.91 Bs. ATMs in the historic center. Cash is king on weekends. Transport: the historic center is entirely walkable. Taxis cost Bs 3–5 — always agree before you get in. Climate: May–October is the dry season — clear skies every day. Safety: Sucre is one of Bolivia's safest cities. Bring sunscreen (the altitude sun is intense), a light jacket for evenings, and comfortable walking shoes."
        data-modal-maps="https://wa.me/59173425725?text=Hello!+I+have+a+practical+question+about+visiting+Sucre."
        data-modal-cta-label="Ask us anything →">
        <div class="art-num">01</div>
        <div class="art-img">
          <img src="https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=600&fm=webp&q=78" alt="El Manual del Viajero" loading="lazy" />
        </div>
        <div class="art-body">
          <p class="art-tag" data-i18n="guia.cron5Tag">El Manual</p>
          <h3 class="art-title" data-i18n="guia.cron5Title">Todo lo que necesitas saber antes de llegar</h3>
          <p class="art-desc" data-i18n="guia.cron5Desc">Altitud, moneda, transporte, clima, seguridad. Lo práctico — sin relleno.</p>
        </div>
        <div class="art-arrow">→</div>
      </div>

      <!-- 02 Pequeños Viajeros -->
      <div class="article-row modal-card"
        data-modal-tag="Families & Kids"
        data-modal-desc="Sucre is one of South America's most family-friendly cities: safe, compact, and full of things that make children forget they're traveling. The Parque Cretácico alone is worth the trip — life-size dinosaur models, 5,000 real footprints on a near-vertical cliff, and a museum that explains 68 million years to a 7-year-old. Plaza 25 de Mayo has pigeons, ice cream vendors, and space to run. At 2,810m the altitude is gentle enough to acclimatize within a day."
        data-modal-maps="https://wa.me/59173425725?text=Hello!+I+read+your+article+about+traveling+with+kids+in+Sucre."
        data-modal-cta-label="Ask us anything →">
        <div class="art-num">02</div>
        <div class="art-img">
          <img src="imagenes/wikipedia/cal_orcko.webp" alt="Pequeños Viajeros Sucre" loading="lazy" />
        </div>
        <div class="art-body">
          <p class="art-tag" data-i18n="guia.cron2Pill">Families & Kids</p>
          <h3 class="art-title" data-i18n="guia.cron2Title">Pequeños Viajeros</h3>
          <p class="art-desc" data-i18n="guia.cron2Sub">Dinosaurs, safe cobblestones, and a pace children can follow. Why Sucre works brilliantly for families.</p>
        </div>
        <div class="art-arrow">→</div>
      </div>

      <!-- 03 10 Insider Tips -->
      <div class="article-row modal-card"
        data-modal-tag="Local Secrets"
        data-modal-desc="After 15 years here, a few things we know for certain: the best salteñas are gone by 10am; taxis cost Bs 3–5, always agree before you get in; cash is king (ATMs run out on weekends). The USFX Law Faculty courtyard is the best free hidden gem in the city. Sucre's ají is unlike any other Bolivian chili — ask for it by name. For sunset, skip the main plaza and go to San Felipe Neri's rooftop or La Recoleta. Give yourself one slow first day. If something isn't in this guide, just ask us on WhatsApp."
        data-modal-maps="https://wa.me/59173425725?text=Hello!+I+read+your+Insider+Tips+and+have+a+question."
        data-modal-cta-label="Ask us anything →">
        <div class="art-num">03</div>
        <div class="art-img">
          <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&fm=webp&q=78" alt="10 Insider Tips" loading="lazy" />
        </div>
        <div class="art-body">
          <p class="art-tag" data-i18n="guia.cron4Pill">Local Secrets</p>
          <h3 class="art-title" data-i18n="guia.cron4Title">10 Insider Tips</h3>
          <p class="art-desc" data-i18n="guia.cron4Sub">Fifteen years in Sucre teach you things no algorithm knows. The ten that will actually change your trip.</p>
        </div>
        <div class="art-arrow">→</div>
      </div>

      <!-- 04 Tradiciones de Domingo -->
      <div class="article-row modal-card"
        data-modal-tag="Markets & Culture"
        data-modal-desc="Sunday in Sucre moves at a different speed. It starts with salteñas — the best ones from street vendors near Mercado Central, gone by 10am. Then comes the Tarabuco market, 65km away: Yampara and Jalq'a communities gathering every Sunday to trade textiles, food, and crafts. Take the first shared van from the terminal at 7am. Back in the city by early afternoon, families fill the plaza. By 3pm, restaurants serve mondongo — the slow-cooked Sunday stew."
        data-modal-maps="https://wa.me/59173425725?text=Hello!+I+have+a+question+about+the+Sunday+market+in+Tarabuco."
        data-modal-cta-label="Ask us about Sunday plans →">
        <div class="art-num">04</div>
        <div class="art-img">
          <img src="imagenes/wikipedia/tarabuco.webp" alt="Tradiciones de Domingo" loading="lazy" />
        </div>
        <div class="art-body">
          <p class="art-tag" data-i18n="guia.cron3Pill">Markets & Culture</p>
          <h3 class="art-title" data-i18n="guia.cron3Title">Tradiciones de Domingo</h3>
          <p class="art-desc" data-i18n="guia.cron3Sub">Salteñas before 10am, Tarabuco by van, and mondongo at 3pm. Sunday in Sucre has a rhythm all its own.</p>
        </div>
        <div class="art-arrow">→</div>
      </div>

      <!-- 05 Sucre After Dark -->
      <div class="article-row modal-card"
        data-modal-tag="Evening Culture"
        data-modal-desc="When the sun sets behind the Recoleta, Sucre shifts gears. The area around Plaza San Francisco comes alive after 9pm with live peña music — charango, quena, voices carrying across colonial walls. Casa de la Cultura hosts free cultural events most weekends. Bar Florin and the spots near Calle Ravelo are where students and expats mix until late. The walk home through lit cobblestones at midnight, with the cathedral glowing white in the cold Andean air, is its own kind of nightlife."
        data-modal-maps="https://wa.me/59173425725?text=Hello!+I+read+your+article+about+Sucre+After+Dark."
        data-modal-cta-label="Ask us anything →">
        <div class="art-num">05</div>
        <div class="art-img">
          <img src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600&fm=webp&q=78" alt="Sucre After Dark" loading="lazy" />
        </div>
        <div class="art-body">
          <p class="art-tag" data-i18n="guia.cron1Pill">Evening Culture</p>
          <h3 class="art-title" data-i18n="guia.cron1Title">Sucre After Dark</h3>
          <p class="art-desc" data-i18n="guia.cron1Sub">Peña music, lit cobblestones, and a cultural scene that moves at student pace. The city doesn't sleep early.</p>
        </div>
        <div class="art-arrow">→</div>
      </div>

    </div>
  </div>
</section>
```

---

## i18n — keys nuevas en `translations.js`

Añadir en EN / ES / FR:

```
guia.cron5Tag    → "El Manual" (igual en los 3)
guia.cron5Title  → "Everything you need to know before you arrive"
                   "Todo lo que necesitas saber antes de llegar"
                   "Tout ce que vous devez savoir avant d'arriver"
guia.cron5Desc   → "Altitude, currency, transport, weather, safety. The practical stuff — no filler."
                   "Altitud, moneda, transporte, clima, seguridad. Lo práctico — sin relleno."
                   "Altitude, monnaie, transport, météo, sécurité. L'essentiel — sans rembourrage."
```

---

## Notas

- Las filas usan `class="article-row modal-card"` — el modal existente (`#editorial-modal`) las captura automáticamente via `.modal-card`.
- El `id="tips"` desaparece. Si hay links `href="#tips"` en el capítulo nav o en otra sección, actualizarlos a `href="#cronicas"`.
- El artículo 01 usa `dark-row` (fondo `#111`) para destacar visualmente la info práctica.
- La imagen del artículo 03 (Insider Tips) es placeholder de Unsplash — reemplazar si hay foto propia.

---

*Handoff preparado para Claude Code · Me Gusta Sucre · Abril 2026*
