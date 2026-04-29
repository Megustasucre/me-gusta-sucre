# Handoff: Me Gusta Sucre — Index Redesign

## Overview

Mejoras quirúrgicas al `index.html` de `megustasucre.com`. El archivo ya tiene una base sólida — los cambios son **reordenar secciones existentes** y **agregar una sección nueva del Inn**. No hay rediseño visual, solo reorganización de la narrativa.

---

## Problema a resolver

El index trata los 4 negocios (Inn, Spanish, Café, Merch) como iguales en "Brand Cards". Pero el **Inn es la conversión principal** — reserva = ingreso directo. Spanish, Café y Merch son servicios secundarios ("mientras estás aquí").

El viajero piensa en este orden:
1. ¿Vale la pena ir a Sucre? → Hero + Trust Bar
2. ¿Dónde me quedo? → **Inn — conversión inmediata**
3. ¿Qué voy a hacer allá? → Atracciones
4. ¿Puedo confiar en ellos? → **Reviews**
5. ¿Qué más ofrecen? → Spanish + Café + Merch
6. Ok, reservo → CTA Final

---

## Cambio 1 — Reordenar secciones

### Orden actual
```
Hero → Ticker → Trust Bar
→ Brand Cards (Inn + Spanish + Café + Merch)
→ Atracciones
→ Reviews
→ CTA Final
→ Footer
```

### Orden nuevo
```
Hero → Ticker → Trust Bar
→ Sección Inn (nueva — ver Cambio 2)
→ Atracciones
→ Reviews
→ Brand Cards reducidas (Spanish + Café + Merch — sin Inn)
→ CTA Final
→ Footer
```

**Implementación:** mover los bloques HTML en el orden indicado. No modificar el contenido interno de cada sección.

---

## Cambio 2 — Nueva sección "Inn"

Insertar después de Trust Bar, antes de Atracciones. Reemplaza la card del Inn en Brand Cards.

### HTML a insertar

```html
<!-- ═══ INN ════════════════════════════════════════ -->
<section style="padding:140px 0; background:#111111;">
  <div class="max-w-7xl mx-auto px-6">
    <div class="inn-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:80px; align-items:center;">

      <!-- Foto -->
      <div style="position:relative; height:520px; overflow:hidden;">
        <img
          src="https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1200&fm=webp&q=80"
          alt="Me Gusta Sucre Inn"
          style="width:100%; height:100%; object-fit:cover;"
          loading="lazy"
        />
        <div style="position:absolute; inset:0; background:linear-gradient(to right, transparent 60%, #111111 100%);"></div>
        <!-- Precio flotante sobre la foto -->
        <div style="position:absolute; bottom:28px; left:28px; background:rgba(20,184,166,0.15); border:1px solid rgba(20,184,166,0.4); backdrop-filter:blur(12px); padding:16px 22px;">
          <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:10px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#2dd4bf; margin:0 0 4px;">DESDE</p>
          <p style="font-family:'Fraunces',serif; font-size:2rem; font-weight:700; color:#14b8a6; margin:0; line-height:1;">$18 <span style="font-size:1rem; font-weight:400; color:rgba(255,255,255,0.5);">/ noche</span></p>
        </div>
      </div>

      <!-- Contenido -->
      <div>
        <p class="eyebrow" style="color:#14b8a6; margin-bottom:16px;" data-i18n="inn.eyebrow">Me Gusta Sucre Inn</p>

        <h2 style="font-family:'Fraunces',serif; font-size:clamp(2.4rem,4vw,3.5rem); font-weight:800; color:#ffffff; line-height:1.1; margin-bottom:20px;" data-i18n="inn.title">
          Tu Casa en <span style="color:#14b8a6; font-style:italic;">Sucre</span>
        </h2>

        <p style="font-size:15px; color:rgba(255,255,255,0.7); line-height:1.85; margin-bottom:28px;" data-i18n="inn.desc">
          Hostal boutique en el corazón del centro histórico. Desayuno incluido, WiFi y atención personalizada desde el primer mensaje.
        </p>

        <!-- Amenities -->
        <div style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:36px;">
          <span style="background:rgba(20,184,166,0.12); border:1px solid rgba(20,184,166,0.3); border-radius:50px; padding:6px 16px; font-size:11px; font-weight:700; color:#2dd4bf; letter-spacing:0.5px;" data-i18n="inn.amenity1">✓ Desayuno incluido</span>
          <span style="background:rgba(20,184,166,0.12); border:1px solid rgba(20,184,166,0.3); border-radius:50px; padding:6px 16px; font-size:11px; font-weight:700; color:#2dd4bf; letter-spacing:0.5px;" data-i18n="inn.amenity2">✓ WiFi gratis</span>
          <span style="background:rgba(20,184,166,0.12); border:1px solid rgba(20,184,166,0.3); border-radius:50px; padding:6px 16px; font-size:11px; font-weight:700; color:#2dd4bf; letter-spacing:0.5px;" data-i18n="inn.amenity3">✓ Centro histórico</span>
          <span style="background:rgba(20,184,166,0.12); border:1px solid rgba(20,184,166,0.3); border-radius:50px; padding:6px 16px; font-size:11px; font-weight:700; color:#2dd4bf; letter-spacing:0.5px;" data-i18n="inn.amenity4">✓ WhatsApp 24h</span>
        </div>

        <!-- CTAs -->
        <div style="display:flex; flex-wrap:wrap; gap:14px;">
          <a href="hospedaje.html#reservar" style="background:#14b8a6; color:#fff; padding:13px 30px; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:13px; letter-spacing:0.5px; text-decoration:none; display:inline-block; transition:background 0.2s, transform 0.2s;" data-i18n="inn.cta1">Ver Habitaciones →</a>
          <a href="https://wa.me/59173425725?text=Hola!%20Me%20interesa%20reservar%20en%20Me%20Gusta%20Sucre%20Inn." target="_blank" style="background:transparent; color:#fff; padding:11px 28px; font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:13px; letter-spacing:0.5px; text-decoration:none; display:inline-block; border:2px solid rgba(255,255,255,0.4); transition:all 0.2s;" data-i18n="inn.cta2">WhatsApp directo</a>
        </div>
      </div>

    </div>
  </div>
</section>
<style>
  @media(max-width:768px){
    .inn-grid{ grid-template-columns:1fr !important; gap:0 !important; }
    .inn-grid > div:first-child{ height:280px !important; }
    .inn-grid > div:first-child > div:last-child{ display:none !important; }
  }
</style>
```

---

## Cambio 3 — Brand Cards: sacar el Inn

En la sección `<!-- ═══ ME GUSTA BRANDS ═══ -->`, eliminar la card del Inn (la primera `<a href="hospedaje.html" class="brand-card fade-up">`).

Actualizar el H2 de la sección:

```html
<!-- Antes -->
<h2 class="section-title">
  <span data-i18n="index.brandsTitle">Stay, Eat,</span>
  <span class="accent" data-i18n="index.brandsAccent">Learn</span>
  <span data-i18n="index.brandsAnd">&amp; Shop</span>
</h2>

<!-- Después -->
<h2 class="section-title">
  <span data-i18n="index.brandsTitle">Aprende,</span>
  <span class="accent" data-i18n="index.brandsAccent">Saborea</span>
  <span data-i18n="index.brandsAnd">y llévate algo</span>
</h2>
```

Actualizar el eyebrow:
```html
<!-- Antes -->
<p class="eyebrow mb-4" data-i18n="index.brandsEyebrow">Me Gusta Collection</p>

<!-- Después -->
<p class="eyebrow mb-4" data-i18n="index.brandsEyebrow">Mientras estás aquí</p>
```

El grid pasa de `lg:grid-cols-4` a `lg:grid-cols-3`:
```html
<!-- Antes -->
<div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

<!-- Después -->
<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
```

---

## Cambio 4 — Mover Reviews antes de Brand Cards

El bloque `<!-- ═══ TESTIMONIALS ═══ -->` debe quedar **después de Atracciones** y **antes de Brand Cards**.

Orden final en el HTML:
```
1. Hero
2. Ticker
3. Trust Bar + SVG transition
4. [NUEVA] Sección Inn
5. Atracciones (ya existe)
6. [MOVER] Testimonials (ya existe — solo moverlo)
7. Brand Cards reducidas (Spanish + Café + Merch)
8. CTA Final
9. Footer
```

---

## Cambio 5 — i18n: agregar claves de la sección Inn

En `js/translations.js`, agregar las siguientes claves en los 3 idiomas:

```js
// EN
inn: {
  eyebrow: "Me Gusta Sucre Inn",
  title: 'Your Home in <span style="color:#14b8a6;font-style:italic">Sucre</span>',
  desc: "Boutique hostal in the heart of the historic center. Breakfast included, WiFi, and personal attention from your first message.",
  amenity1: "✓ Breakfast included",
  amenity2: "✓ Free WiFi",
  amenity3: "✓ Historic center",
  amenity4: "✓ WhatsApp 24h",
  cta1: "See Rooms →",
  cta2: "WhatsApp us",
},

// ES
inn: {
  eyebrow: "Me Gusta Sucre Inn",
  title: 'Tu Casa en <span style="color:#14b8a6;font-style:italic">Sucre</span>',
  desc: "Hostal boutique en el corazón del centro histórico. Desayuno incluido, WiFi y atención personalizada desde el primer mensaje.",
  amenity1: "✓ Desayuno incluido",
  amenity2: "✓ WiFi gratis",
  amenity3: "✓ Centro histórico",
  amenity4: "✓ WhatsApp 24h",
  cta1: "Ver Habitaciones →",
  cta2: "WhatsApp directo",
},

// FR
inn: {
  eyebrow: "Me Gusta Sucre Inn",
  title: 'Votre Maison à <span style="color:#14b8a6;font-style:italic">Sucre</span>',
  desc: "Auberge boutique au cœur du centre historique. Petit-déjeuner inclus, WiFi et attention personnalisée dès votre premier message.",
  amenity1: "✓ Petit-déjeuner inclus",
  amenity2: "✓ WiFi gratuit",
  amenity3: "✓ Centre historique",
  amenity4: "✓ WhatsApp 24h",
  cta1: "Voir les Chambres →",
  cta2: "WhatsApp direct",
},
```

> **Nota:** las claves con HTML embebido (`title`) necesitan `data-i18n-html` en el elemento, no `data-i18n`.

---

## Tokens de diseño (Inn)

```
Color principal:   #14b8a6
Color oscuro:      #0f766e
Color claro:       #2dd4bf
Color muy claro:   #99f6e4
Fondo sección:     #111111
Foto overlay:      linear-gradient(to right, transparent 60%, #111111 100%)
Badge bg:          rgba(20,184,166,0.12)
Badge border:      rgba(20,184,166,0.3)
```

---

## Archivos a modificar

| Archivo | Cambio |
|---|---|
| `index.html` | Cambios 1, 2, 3 y 4 |
| `js/translations.js` | Cambio 5 — agregar claves `inn.*` en EN/ES/FR |

---

## Notas

- La sección Inn usa `data-i18n-html` para el H2 (tiene un `<span>` embebido). Asegurarse de que `main.js` o `translations.js` soporte esta directiva — ya existe en el proyecto para otros elementos.
- El texto visible al usuario siempre lo define `translations.js`, no el fallback del HTML. Actualizar ambos para consistencia.
- La foto del Inn (`photo-1564501049412`) es Unsplash temporal — reemplazar cuando lleguen las fotos reales.
- El precio `$18 / noche` corresponde a la cama de dorm según `hospedaje.html`. Confirmar si es el precio correcto para mostrar en el index.

---

*Documento preparado el 24 de Abril, 2026.*
*Basado en: review.md · Observación IA.txt · mejoras_IA_Antigravity.md*
