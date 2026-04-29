# Handoff — Food & Drink Section Redesign
### guia.html · Me Gusta Sucre · Abril 2026

---

## Qué reemplazar

Buscar en `guia.html` la sección:
```html
<!-- ═══ FOOD & COFFEE ════════════════════════════════ -->
<section id="food" style="padding:100px 0;background:#fff">
```

Reemplazar **todo el bloque** hasta el cierre `</section>` con el HTML de abajo.

---

## CSS — añadir en `<style>` inline o en `style.css`

```css
/* ── Food Section ── */
.food-section {
  padding: 120px 0;
  background: #fdf6ec;
}
.food-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 48px;
}

/* ── Header ── */
.food-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 40px;
  margin-bottom: 80px;
  padding-bottom: 40px;
  border-bottom: 1px solid #e8dfd0;
}
.food-eyebrow {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #c9252d;
  margin-bottom: 14px;
}
.food-title {
  font-family: 'Fraunces', serif;
  font-size: clamp(2.8rem, 4vw, 4rem);
  font-weight: 800;
  color: #111;
  line-height: 1.05;
}
.food-title em { color: #c9252d; font-style: italic; }
.food-intro {
  font-size: 15px;
  color: #666;
  line-height: 1.85;
  max-width: 340px;
  padding-bottom: 6px;
}

/* ── Two-column body ── */
.food-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: start;
}

/* ── Image col ── */
.food-img-col { position: sticky; top: 100px; }
.food-img-wrap {
  position: relative;
  overflow: hidden;
  height: 560px;
}
.food-img-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* ── Café CTA bar ── */
.cafe-cta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  background: #1a0e06;
  padding: 24px 28px;
  text-decoration: none;
  transition: background 0.25s;
  border-top: 2px solid #5aaa6a;
}
.cafe-cta:hover { background: #2c1a0e; }
.cafe-cta-left { display: flex; align-items: center; gap: 16px; }
.cafe-cta-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #5aaa6a;
  flex-shrink: 0;
  animation: pulse 2.5s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.6; transform: scale(0.8); }
}
.cafe-cta-tag {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #5aaa6a;
  margin-bottom: 4px;
}
.cafe-cta-name {
  font-family: 'Fraunces', serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.1;
}
.cafe-cta-detail {
  font-size: 12px;
  color: rgba(255,255,255,0.45);
  margin-top: 3px;
}
.cafe-cta-arrow {
  font-size: 13px;
  font-weight: 700;
  color: #5aaa6a;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: gap 0.2s;
}
.cafe-cta:hover .cafe-cta-arrow { gap: 13px; }

/* ── Dish list ── */
.dish-list { display: flex; flex-direction: column; }
.dish-item {
  padding: 28px 0;
  border-bottom: 1px solid #e8dfd0;
}
.dish-item:first-child { border-top: 1px solid #e8dfd0; }
.dish-top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 10px;
}
.dish-name {
  font-family: 'Fraunces', serif;
  font-size: 1.35rem;
  font-weight: 800;
  color: #111;
  line-height: 1.1;
}
.dish-name.featured { color: #c9252d; font-style: italic; }
.dish-name.gold     { color: #b8860b; font-style: italic; }
.dish-name.green    { color: #3a7d44; font-style: italic; }
.dish-badge {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 4px 10px;
  white-space: nowrap;
  flex-shrink: 0;
}
.dish-badge.red   { background: #c9252d; color: #fff; }
.dish-badge.gold  { background: #b8860b; color: #fff; }
.dish-badge.green { background: #3a7d44; color: #fff; }
.dish-badge.muted { background: rgba(0,0,0,0.06); color: #666; }
.dish-desc {
  font-size: 13.5px;
  color: #666;
  line-height: 1.8;
}

/* ── Ají note ── */
.aji-note {
  margin-top: 36px;
  background: #111;
  padding: 28px;
  display: flex;
  align-items: flex-start;
  gap: 20px;
  border-left: 3px solid #c9252d;
}
.aji-icon {
  width: 44px; height: 44px;
  background: rgba(201,37,45,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.aji-label {
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #c9252d;
  margin-bottom: 6px;
}
.aji-title {
  font-family: 'Fraunces', serif;
  font-size: 1.2rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 8px;
  font-style: italic;
}
.aji-body {
  font-size: 13px;
  color: rgba(255,255,255,0.55);
  line-height: 1.8;
}

/* ── Responsive ── */
@media (max-width: 900px) {
  .food-body { grid-template-columns: 1fr; gap: 48px; }
  .food-img-col { position: static; }
  .food-header { flex-direction: column; align-items: flex-start; gap: 20px; }
  .food-inner { padding: 0 24px; }
  .food-img-wrap { height: 400px; }
}
```

---

## HTML — reemplazar la sección completa

```html
<!-- ═══ FOOD & DRINK ════════════════════════════════ -->
<section id="food" class="food-section">
  <div class="food-inner">

    <!-- Header -->
    <div class="food-header">
      <div>
        <p class="food-eyebrow" data-i18n="guia.foodEyebrow">Eat & Drink</p>
        <h2 class="food-title">
          <span data-i18n="guia.foodTitlePre">What to eat</span><br>
          in <em data-i18n="guia.foodTitleAccent">Sucre</em>
        </h2>
      </div>
      <p class="food-intro" data-i18n="guia.foodSub">Sucre has one of Bolivia's richest food traditions — built around slow-cooked stews, handmade doughs, and a spice culture unlike anywhere else in the country.</p>
    </div>

    <!-- Body -->
    <div class="food-body">

      <!-- Col izquierda: imagen sticky + Café CTA -->
      <div class="food-img-col">
        <div class="food-img-wrap">
          <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=900&q=82" alt="Coffee and food in Sucre Bolivia" />
        </div>
        <a href="cafe.html" class="cafe-cta">
          <div class="cafe-cta-left">
            <span class="cafe-cta-dot"></span>
            <div>
              <p class="cafe-cta-tag" data-i18n="guia.cafeName">Me Gusta Café</p>
              <p class="cafe-cta-name" data-i18n="guia.cafeAddress">Bolivar #603 · Open Now</p>
              <p class="cafe-cta-detail" data-i18n="guia.cafeHours">Mon–Sat 8am–8pm · Bolivian coffee &amp; pastries</p>
            </div>
          </div>
          <span class="cafe-cta-arrow" data-i18n="guia.cafeBtn">See the menu →</span>
        </a>
      </div>

      <!-- Col derecha: lista de platos -->
      <div>
        <div class="dish-list">

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name featured">Chorizo Chuquisaqueño</h3>
              <span class="dish-badge red" data-i18n="guia.food1Badge">Most representative</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food1Desc">The defining dish of Sucre. Spiced pork sausage grilled over charcoal and served with mote (hominy corn), potatoes, and the local ají. Order it from a street stall near the market — never at a tourist restaurant. The version at Mercado Central at noon is the benchmark.</p>
          </div>

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name">Salteña</h3>
              <span class="dish-badge muted" data-i18n="guia.food3Sub">Breakfast ritual</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food3Desc">Bolivia's most beloved pastry — a crimped, baked dough filled with slow-cooked beef or chicken stew in a gelatin broth that liquefies as it bakes. Gone from the best stalls by 10am without exception. Ask your hotel where the closest good one is the night before.</p>
          </div>

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name">Mondongo</h3>
              <span class="dish-badge muted" data-i18n="guia.food2Sub">Sunday tradition</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food2Desc">The Sunday stew of Sucre. A slow-cooked tripe and pork soup with hominy, chicha, and ají — traditionally eaten at home after church. Some restaurants serve it on Sundays only. If you're in the city on a Sunday and adventurous, this is the most authentic meal you can have.</p>
          </div>

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name">Picante de Pollo</h3>
              <span class="dish-badge muted" data-i18n="guia.food4Sub">Rich ají sauce</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food4Desc">Chicken braised until tender in a deep, slow-cooked sauce that takes hours to prepare. A Chuquisaca classic — order it at a family-run restaurant, never at a place with a laminated menu.</p>
          </div>

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name gold">Chocolate de Sucre</h3>
              <span class="dish-badge gold" data-i18n="guia.food6Badge">Best in Bolivia</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food6Desc">Sucre is Bolivia's chocolate capital — the country grows some of the world's finest cacao in the lowland departments, and the city's chocolate makers have been refining it here for generations. Buy a bar at Taboada or Para Ti on Calle Arenales, and bring several home.</p>
          </div>

          <div class="dish-item">
            <div class="dish-top">
              <h3 class="dish-name green">Ajenjo</h3>
              <span class="dish-badge green" data-i18n="guia.food7Badge">Regional liqueur</span>
            </div>
            <p class="dish-desc" data-i18n="guia.food7Desc">A herbal liqueur made from wormwood (ajenjo), produced exclusively in Chuquisaca and found almost nowhere else in Bolivia. Served ice-cold as a digestif after a heavy meal. It tastes like nothing else. Try it once — you'll either hate it or bring two bottles home.</p>
          </div>

        </div>

        <!-- Ají note -->
        <div class="aji-note">
          <div class="aji-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="#c9252d"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/></svg>
          </div>
          <div>
            <p class="aji-label" data-i18n="guia.ajiLabel">Ingrediente secreto</p>
            <p class="aji-title" data-i18n="guia.ajiTitle">El Ají de Sucre</p>
            <p class="aji-body" data-i18n="guia.ajiBody">Un chile cultivado exclusivamente en Chuquisaca, único en toda Bolivia. Si el cocinero lo usa, estás comiendo lo auténtico. Pídelo por nombre en cualquier mercado.</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
```

---

## i18n — keys nuevas a añadir en `translations.js`

Las siguientes keys son nuevas y deben añadirse en los 3 idiomas (EN / ES / FR):

```
guia.foodTitlePre     → "What to eat" / "Qué comer" / "Que manger"
guia.foodTitleAccent  → "Sucre" (igual en los 3)
guia.cafeName         → "Me Gusta Café" (igual en los 3)
guia.cafeAddress      → "Bolivar #603 · Open Now" / "Bolivar #603 · Abierto ahora" / "Bolivar #603 · Ouvert maintenant"
guia.cafeHours        → "Mon–Sat 8am–8pm · Bolivian coffee & pastries" / "Lun–Sab 8am–8pm · Café boliviano y repostería" / "Lun–Sam 8h–20h · Café bolivien et pâtisseries"
guia.cafeBtn          → "See the menu →" / "Ver el menú →" / "Voir le menu →"
guia.food1Desc        → [texto narrativo del chorizo — ver HTML]
guia.food2Desc        → [texto narrativo del mondongo]
guia.food3Desc        → [texto narrativo de la salteña]
guia.food4Desc        → [texto narrativo del picante de pollo]
guia.food6Desc        → [texto narrativo del chocolate]
guia.food7Desc        → [texto narrativo del ajenjo]
guia.ajiLabel         → "Secret ingredient" / "Ingrediente secreto" / "Ingrédient secret"
guia.ajiTitle         → "El Ají de Sucre" (igual en los 3)
guia.ajiBody          → [texto del ají — ver HTML]
```

**Keys existentes que se reutilizan sin cambios:**
`guia.foodEyebrow`, `guia.food1Badge`, `guia.food2Sub`, `guia.food3Sub`, `guia.food4Sub`, `guia.food6Badge`, `guia.food7Badge`

---

## Notas importantes

- **Eliminar** el bloque standalone `<!-- Pro Tip -->` que está antes de esta sección — el ají ya está integrado aquí.
- La imagen usa Unsplash. Si tienes una foto propia del café, reemplazar la URL.
- El CTA del café usa `href="cafe.html"` — verificar que la ruta es correcta desde `guia.html`.
- `position: sticky` en `.food-img-col` requiere que ningún ancestro tenga `overflow: hidden`. Verificar si la sección tiene ese estilo heredado.

---

*Handoff preparado para Claude Code · Me Gusta Sucre · Abril 2026*
