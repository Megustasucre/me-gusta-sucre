# Handoff — CTA Final Redesign
### guia.html · Me Gusta Sucre · Abril 2026

---

## Resumen de cambios

- Sección `<!-- CLOSING: SCHOOL + INN -->` completamente rediseñada
- Grid: School 2/3 + columna derecha 1/3 (Inn + Café apilados)
- Inn: fondo pizarra azulada (`oklch(18% 0.015 240)`) con noise sutil
- Café: barra inferior con dot verde pulsante
- Copy: "Boutique Inn" → "Hostal"
- Sin `border-radius` — esquinas rectas consistentes con el sistema

---

## ⚠️ Logos — verificar antes de implementar

| Elemento | Ruta esperada | Estado |
|---|---|---|
| Me Gusta Spanish | `imagenes/logos/logo-me-gusta-spanish.png` | ✅ Existe |
| Me Gusta Hostal | `imagenes/logos/logo-me-gusta-hostal.png` | ❓ Verificar |
| Me Gusta Café | `imagenes/logos/logo-me-gusta-cafe.png` | ❓ Verificar |

Si los logos del Hostal o Café no existen, usar `logo-me-gusta-sucre-chinchilla.png` como fallback temporal.

---

## CSS — reemplazar estilos del bloque closing en `style.css`

```css
/* ── Closing CTA Section ── */
.closing-section {
  background: #111;
  position: relative;
  overflow: hidden;
}

/* Header */
.closing-header {
  max-width: 1280px;
  margin: 0 auto;
  padding: 100px 48px 72px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 40px;
}
.closing-eyebrow {
  font-size: 11px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #c9252d; margin-bottom: 14px;
}
.closing-title {
  font-family: 'Fraunces', serif;
  font-size: clamp(2.8rem, 4vw, 4rem);
  font-weight: 800; color: #fff; line-height: 1.05;
}
.closing-title em { color: #c9252d; font-style: italic; }
.closing-sub {
  font-size: 15px; color: rgba(255,255,255,0.35);
  max-width: 300px; line-height: 1.8; padding-bottom: 6px;
}

/* Grid */
.closing-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
}

/* School card */
.cta-school {
  position: relative;
  min-height: 520px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  overflow: hidden;
  text-decoration: none;
  border-top: 1px solid rgba(255,255,255,0.07);
}
.cta-school-img {
  position: absolute; inset: 0;
  width: 100%; height: 100%; object-fit: cover;
  transition: transform 0.9s cubic-bezier(0.25,0.46,0.45,0.94);
}
.cta-school:hover .cta-school-img { transform: scale(1.04); }
.cta-school-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(135deg,
    rgba(10,6,2,0.97) 0%,
    rgba(10,6,2,0.75) 50%,
    rgba(10,6,2,0.3) 100%);
}
.cta-school-body {
  position: relative; z-index: 1;
  padding: 52px;
}
.cta-school-logo {
  display: flex; align-items: center; gap: 14px;
  margin-bottom: 28px;
}
.cta-school-logo img {
  height: 32px; width: auto;
  filter: brightness(0) invert(1);
}
.cta-school-tag {
  font-size: 9px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #FF3B6B;
}
.cta-school-name {
  font-family: 'Fraunces', serif; font-size: 1rem;
  font-weight: 700; color: #fff; margin-top: 2px;
}
.cta-school-title {
  font-family: 'Fraunces', serif;
  font-size: clamp(1.8rem, 2.5vw, 2.6rem);
  font-weight: 800; color: #fff;
  line-height: 1.1; margin-bottom: 18px;
}
.cta-school-title em { color: #FF3B6B; font-style: italic; }
.cta-school-desc {
  font-size: 14px; color: rgba(255,255,255,0.6);
  line-height: 1.8; margin-bottom: 32px; max-width: 480px;
}
.cta-school-tags {
  display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 32px;
}
.cta-school-tags span {
  background: rgba(255,59,107,0.12);
  color: #FF3B6B;
  padding: 6px 14px;
  font-size: 10px; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase;
}
.btn-coral {
  display: inline-block;
  background: #FF3B6B; color: #fff;
  padding: 16px 36px;
  font-weight: 700; font-size: 14px;
  text-decoration: none; letter-spacing: 0.5px;
  transition: background 0.2s;
}
.btn-coral:hover { background: #e0305c; }

/* Right col */
.cta-right {
  display: flex; flex-direction: column;
  border-left: 1px solid rgba(255,255,255,0.07);
}

/* Inn card */
.cta-inn {
  flex: 1;
  background: oklch(18% 0.015 240);
  padding: 40px 36px;
  display: flex; flex-direction: column;
  border-bottom: 1px solid rgba(255,255,255,0.07);
  position: relative; overflow: hidden;
  transition: background 0.2s;
}
.cta-inn:hover { background: oklch(21% 0.018 240); }
.cta-inn-noise {
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  opacity: 0.04; pointer-events: none;
}
.cta-inn-accent {
  position: absolute; top: 0; left: 0; right: 0;
  height: 2px; background: #2ECEC4;
}
.cta-inn-tag {
  font-size: 9px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #2ECEC4;
  margin-bottom: 14px; position: relative; z-index: 1;
}
.cta-inn-title {
  font-family: 'Fraunces', serif;
  font-size: 1.6rem; font-weight: 800; color: #fff;
  line-height: 1.1; margin-bottom: 8px; position: relative; z-index: 1;
}
.cta-inn-price {
  font-size: 12px; color: rgba(255,255,255,0.35);
  margin-bottom: 20px; position: relative; z-index: 1;
}
.cta-inn-price strong {
  font-family: 'Fraunces', serif; font-size: 1.1rem;
  color: rgba(255,255,255,0.7);
}
.cta-inn-features {
  display: flex; flex-direction: column; gap: 10px;
  margin-bottom: 28px; flex: 1; position: relative; z-index: 1;
}
.cta-inn-feat {
  display: flex; align-items: center; gap: 10px;
  font-size: 12px; color: rgba(255,255,255,0.5); font-weight: 600;
}
.cta-inn-feat::before {
  content: '';
  width: 6px; height: 6px; border-radius: 50%;
  background: #2ECEC4; flex-shrink: 0;
}
.btn-teal {
  display: block; text-align: center;
  background: #2ECEC4; color: #fff;
  padding: 14px 20px;
  font-weight: 700; font-size: 13px;
  text-decoration: none; letter-spacing: 0.5px;
  transition: background 0.2s; position: relative; z-index: 1;
}
.btn-teal:hover { background: #25b5ab; }

/* Café bar */
.cta-cafe {
  background: #1a0e06;
  padding: 28px 32px;
  display: flex; align-items: center; gap: 18px;
  text-decoration: none;
  transition: background 0.2s;
}
.cta-cafe:hover { background: #2c1a0e; }
.cta-cafe-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: #5aaa6a; flex-shrink: 0;
  animation: cafePulse 2.5s ease-in-out infinite;
}
@keyframes cafePulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.5; transform: scale(0.75); }
}
.cta-cafe-tag {
  font-size: 9px; font-weight: 700; letter-spacing: 3px;
  text-transform: uppercase; color: #5aaa6a; margin-bottom: 4px;
}
.cta-cafe-name {
  font-family: 'Fraunces', serif; font-size: 1rem;
  font-weight: 800; color: #fff; line-height: 1.1;
}
.cta-cafe-hours {
  font-size: 11px; color: rgba(255,255,255,0.35); margin-top: 3px;
}
.cta-cafe-arrow {
  font-size: 13px; font-weight: 700; color: #5aaa6a;
  margin-left: auto; white-space: nowrap;
  transition: transform 0.2s;
}
.cta-cafe:hover .cta-cafe-arrow { transform: translateX(4px); }

/* Responsive */
@media (max-width: 960px) {
  .closing-grid { grid-template-columns: 1fr; }
  .cta-right { border-left: none; border-top: 1px solid rgba(255,255,255,0.07); }
  .closing-header { flex-direction: column; align-items: flex-start; gap: 20px; padding: 60px 24px 48px; }
  .cta-school-body { padding: 36px 28px; }
}
```

---

## HTML — reemplazar sección completa

Buscar `<!-- ═══ CLOSING: SCHOOL + INN ═══════════════════════ -->` y reemplazar hasta el cierre `</section>`:

```html
<!-- ═══ CLOSING: SCHOOL + INN + CAFÉ ══════════════════ -->
<section class="closing-section fade-up">

  <!-- Header -->
  <div class="closing-header">
    <div>
      <p class="closing-eyebrow" data-i18n="guia.xsellEyebrow">Make the most of your time</p>
      <h2 class="closing-title">
        More from <em data-i18n="guia.xsellTitleAccent">Me Gusta</em>
      </h2>
    </div>
    <p class="closing-sub" data-i18n="guia.xsellSub">Classes in the morning, explore the city in the afternoon. Everything is steps away.</p>
  </div>

  <!-- Grid -->
  <div class="closing-grid">

    <!-- School — hero card -->
    <a href="clases.html" class="cta-school">
      <img class="cta-school-img"
        src="https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=1400&q=82"
        alt="Spanish classes Sucre" loading="lazy" />
      <div class="cta-school-overlay"></div>
      <div class="cta-school-body">
        <div class="cta-school-logo">
          <img src="imagenes/logos/logo-me-gusta-spanish.png" alt="Me Gusta Spanish" />
          <div>
            <p class="cta-school-tag" data-i18n="guia.xsell1Type">Language School</p>
            <p class="cta-school-name">Me Gusta Spanish</p>
          </div>
        </div>
        <h3 class="cta-school-title">
          Learn Spanish <em data-i18n="guia.ctaAccent">while you're here.</em>
        </h3>
        <p class="cta-school-desc" data-i18n="guia.xsell1P">Sucre is South America's #1 city for Spanish immersion. Morning classes with native teachers at Audiencia #97 — then spend the afternoon exploring everything in this guide.</p>
        <div class="cta-school-tags">
          <span data-i18n="guia.xsell1Tag1">Private Classes</span>
          <span data-i18n="guia.xsell1Tag2">Group Classes</span>
          <span data-i18n="guia.xsell1Tag3">All Levels</span>
        </div>
        <a href="clases.html" class="btn-coral" data-i18n="guia.xsell1Btn">Start Learning Spanish →</a>
      </div>
    </a>

    <!-- Right col: Hostal + Café -->
    <div class="cta-right">

      <!-- Hostal -->
      <div class="cta-inn">
        <div class="cta-inn-noise"></div>
        <div class="cta-inn-accent"></div>
        <p class="cta-inn-tag" data-i18n="guia.xsell2Type">Hostal · Historic Center</p>
        <h3 class="cta-inn-title" data-i18n="guia.xsell2Name">Me Gusta Hostal</h3>
        <p class="cta-inn-price">
          <span data-i18n="guia.xsell2From">from</span>
          <strong>$18</strong>
          <span data-i18n="guia.xsell2Night">/ night</span>
          · La Paz #571
        </p>
        <div class="cta-inn-features">
          <div class="cta-inn-feat" data-i18n="guia.xsell2Tag1">Steps from Plaza 25 de Mayo</div>
          <div class="cta-inn-feat" data-i18n="guia.xsell2Tag2">Breakfast included</div>
          <div class="cta-inn-feat" data-i18n="guia.xsell2Tag3">Team that knows Sucre inside out</div>
        </div>
        <a href="hospedaje.html" class="btn-teal" data-i18n="index.brand2Cta">See Rooms &amp; Rates</a>
      </div>

      <!-- Café -->
      <a href="cafe.html" class="cta-cafe">
        <span class="cta-cafe-dot"></span>
        <div>
          <p class="cta-cafe-tag" data-i18n="guia.cafeName">Me Gusta Café</p>
          <p class="cta-cafe-name" data-i18n="guia.cafeAddress">Bolivar #603 · Open Now</p>
          <p class="cta-cafe-hours" data-i18n="guia.cafeHours">Mon–Sat 8am–8pm · Bolivian coffee &amp; pastries</p>
        </div>
        <span class="cta-cafe-arrow" data-i18n="guia.cafeBtn">See menu →</span>
      </a>

    </div>
  </div>

</section>
```

---

## i18n — keys nuevas en `translations.js`

```
guia.xsell2Name  → "Me Gusta Hostal" (igual en los 3)
guia.xsell2Tag3  → "Team that knows Sucre inside out"
                   "Un equipo que conoce Sucre por dentro"
                   "Une équipe qui connaît Sucre de l'intérieur"
guia.cafeName    → "Me Gusta Café" (igual)
guia.cafeAddress → "Bolivar #603 · Open Now" / "Bolivar #603 · Abierto ahora" / "Bolivar #603 · Ouvert maintenant"
guia.cafeHours   → "Mon–Sat 8am–8pm · Bolivian coffee & pastries"
                   "Lun–Sab 8am–8pm · Café boliviano y repostería"
                   "Lun–Sam 8h–20h · Café bolivien et pâtisseries"
guia.cafeBtn     → "See menu →" / "Ver el menú →" / "Voir le menu →"
```

**Keys existentes reutilizadas:** `guia.xsellEyebrow`, `guia.xsellSub`, `guia.xsell1Type`, `guia.ctaAccent`, `guia.xsell1P`, `guia.xsell1Tag1`, `guia.xsell1Tag2`, `guia.xsell1Tag3`, `guia.xsell1Btn`, `guia.xsell2Type`, `guia.xsell2From`, `guia.xsell2Night`, `index.brand2Cta`

---

## Notas

- Eliminar el `radial-gradient` ambient glow de la sección anterior — el nuevo diseño no lo usa.
- El `fade-up` en la sección necesita que `js/main.js` esté cargado — ya lo está.
- El `z-index:1` del `.relative` anterior está resuelto con `position:relative;z-index:1` en cada elemento que lo necesita.
- Si `logo-me-gusta-hostal.png` no existe, añadir el logo en el HTML así como fallback:
  ```html
  <img src="imagenes/logos/logo-me-gusta-sucre-chinchilla.png" alt="Me Gusta Hostal" />
  ```

---

*Handoff preparado para Claude Code · Me Gusta Sucre · Abril 2026*
