# Handoff Maestro — guia.html
### Me Gusta Sucre · Abril 2026
### Claude Code: aplicar todos estos cambios en orden

---

## Sistema de fondos — 3 valores únicos

Antes de tocar HTML, interiorizar este sistema:

```
CLARO   → #ffffff  — contenido funcional (spots, about, food)
CÁLIDO  → #fdf6ec  — editorial/narrativo (manifiesto, social proof, day trips, crónicas)
OSCURO  → #111111  — impacto visual (capítulos, stats, closing)
```

Todo `#f4f4f4`, `#fafafa`, `#0d0d0d`, `#0a0a0a` deben reemplazarse por uno de estos 3.

---

## CAMBIO 1 — Eliminar Breadcrumb

```html
<!-- ELIMINAR BLOQUE COMPLETO: -->
<div style="background:#f4f4f4;border-bottom:1px solid #e5e5e5;padding:14px 0">
  <div class="max-w-7xl mx-auto px-6">
    <p style="font-size:13px;color:#555555">
      <a href="index.html" style="color:#c9252d;text-decoration:none;font-weight:600">Home</a> / City Guide
    </p>
  </div>
</div>
```

---

## CAMBIO 2 — Capítulos: fondo oscuro

```html
<!-- ANTES: -->
<section style="padding:80px 0;background:#fff">

<!-- DESPUÉS: -->
<section style="padding:80px 0;background:#111111">
```

También actualizar los títulos internos al color claro:
```html
<!-- El eyebrow "La Guía": -->
<p class="eyebrow mb-2" style="color:#c9252d;letter-spacing:2px" ...>

<!-- El h2 "Los Capítulos": cambiar color:#111 → color:#fff -->
<h2 style="...;color:#fff;...">
  <span ...>Los</span> <span style="color:#c9252d;font-style:italic" ...>Capítulos</span>
</h2>
```

---

## CAMBIO 3 — Capítulo 03 "El Manual": actualizar href

```html
<!-- ANTES: -->
<a href="#tips" class="chapter-card">

<!-- DESPUÉS: -->
<a href="#cronicas" class="chapter-card">
```

---

## CAMBIO 4 — Mover Quick Facts Bar después de About the City

Cortar el bloque `<!-- QUICK FACTS BAR -->` de su posición actual (entre Capítulos y About) y pegarlo **inmediatamente después** del cierre `</section>` de About the City.

Nuevo orden:
```
[Capítulos]          → #111111
[About the City]     → #fff
[Quick Facts Bar]    ← MOVIDO AQUÍ → #111111
[Social Proof]       → #fdf6ec
[Must-See Spots]     → #fff
...
```

---

## CAMBIO 5 — Must-See Spots: cambiar fondo

```html
<!-- ANTES: -->
<section id="spots" style="padding:100px 0;background:#f4f4f4">

<!-- DESPUÉS: -->
<section id="spots" style="padding:100px 0;background:#fff">
```

---

## CAMBIO 6 — Day Trips: cambiar fondo

```html
<!-- ANTES: -->
<section id="daytrips" style="padding:100px 0;background:#fff">

<!-- DESPUÉS: -->
<section id="daytrips" style="padding:100px 0;background:#fdf6ec">
```

Actualizar también los colores de texto internos que asumían fondo blanco:
- `color:#111` en títulos → se mantiene (legible sobre crema)
- `color:#666` en párrafos → se mantiene
- Bordes `#e5e5e5` → cambiar a `#e8dfd0` para armonizar con la crema

---

## CAMBIO 7 — Eliminar bloque "Pro Tip"

```html
<!-- ELIMINAR BLOQUE COMPLETO: -->
<div class="fade-up" style="background:#111;padding:48px 0">
  <div class="max-w-3xl mx-auto px-6">
    <div style="border-left:4px solid #c9252d;padding:24px 28px;...">
      <p ...>Pro Tip — Local Knowledge</p>
      <p ...>The secret ingredient of Sucre's cuisine</p>
      <p ...>Sucre's aji...</p>
    </div>
  </div>
</div>
```

---

## CAMBIO 8 — Reemplazar Food & Coffee

> ✅ Ya hecho — usar handoff `food-section-handoff.md`

---

## CAMBIO 9 — Eliminar Practical Tips

```html
<!-- ELIMINAR SECCIÓN COMPLETA: -->
<section id="tips" style="padding:100px 0;background:#111">
  ...
  <!-- Todo hasta el </section> -->
</section>
```

---

## CAMBIO 10 — Reemplazar Las Crónicas

> ✅ Usar handoff `cronicas-handoff-v2.md`

---

## CAMBIO 11 — Reemplazar Closing CTA

> ✅ Usar handoff `cta-handoff.md`

---

## CAMBIO 12 — Closing: fondo unificado

En el nuevo CTA, asegurarse de que el fondo sea `#111111`:

```css
.closing-section { background: #111111; }
```

Eliminar el `#0d0d0d` del bloque anterior si quedara alguna referencia.

---

## Resultado final — flujo de fondos

```
Hero              → imagen full-bleed
Manifiesto        → #fdf6ec  (crema cálido)
Capítulos         → #111111  (oscuro, impacto)
About the City    → #ffffff  (limpio)
Quick Facts       → #111111  (oscuro, stats)
Social Proof      → #fdf6ec  (crema)
Must-See Spots    → #ffffff  (limpio)
Day Trips         → #fdf6ec  (crema)
Food & Drink      → #fdf6ec  (crema — nuevo diseño)
Las Crónicas      → #fdf6ec  (crema)
Closing CTA       → #111111  (oscuro, final fuerte)
```

Ritmo: imagen → crema → **oscuro** → blanco → **oscuro** → crema → blanco → crema → crema → crema → **oscuro**

3 fondos. Sin `#f4f4f4`. Sin `#0d0d0d`. Sin `#fafafa`.

---

## Otros fixes menores

### Modal close button — cambiar X por SVG
```html
<!-- ANTES: -->
<button id="modal-close" style="...">X</button>

<!-- DESPUÉS: -->
<button id="modal-close" style="position:absolute;top:14px;right:14px;z-index:1;background:rgba(0,0,0,0.55);border:none;color:#fff;width:36px;height:36px;cursor:pointer;display:flex;align-items:center;justify-content:center" aria-label="Close">
  <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
    <path d="M1 1l12 12M13 1L1 13" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
  </svg>
</button>
```

### Social Proof — añadir contexto
```html
<!-- AÑADIR antes de los números: -->
<p style="font-size:12px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:2px;margin-bottom:16px">
  Me Gusta Sucre — Spanish School · Inn · Café
</p>
```

### Closing section — fix z-index
```html
<!-- CAMBIAR: -->
<div class="max-w-7xl mx-auto px-6 relative z-1">

<!-- POR: -->
<div class="max-w-7xl mx-auto px-6" style="position:relative;z-index:1">
```

### Logos faltantes — verificar
- `imagenes/logos/logo-me-gusta-hostal.png` → si no existe, usar `logo-me-gusta-sucre-chinchilla.png`
- `imagenes/logos/logo-me-gusta-cafe.png` → si no existe, usar `logo-me-gusta-sucre-chinchilla.png`

---

## Orden de implementación recomendado

```
1.  Eliminar Breadcrumb                    (2 min)
2.  Capítulos → fondo #111111              (3 min)
3.  Capítulo 03 href="#tips" → "#cronicas" (1 min)
4.  Mover Quick Facts Bar                  (5 min)
5.  Must-See Spots → fondo #fff            (1 min)
6.  Day Trips → fondo #fdf6ec             (2 min)
7.  Eliminar Pro Tip                       (2 min)
8.  Aplicar food-section-handoff.md        (15 min)
9.  Eliminar Practical Tips                (2 min)
10. Aplicar cronicas-handoff-v2.md         (15 min)
11. Aplicar cta-handoff.md                 (15 min)
12. Fixes menores (modal, social proof)    (5 min)
```

**Tiempo total estimado: ~70 min**

---

*Handoff Maestro · Me Gusta Sucre · Abril 2026*
