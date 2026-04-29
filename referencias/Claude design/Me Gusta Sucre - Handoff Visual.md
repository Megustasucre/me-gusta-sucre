# Handoff: Me Gusta Sucre — Mejoras Visuales Index

## Overview

Este documento complementa el handoff anterior (`Me Gusta Sucre — Handoff Index.md`). Cubre exclusivamente los **cambios visuales y de animación** del `index.html` — los cambios estructurales (reorden de secciones, sección Inn, i18n) ya están documentados en el handoff anterior.

---

## Cambio 1 — Inn: fondo cream en vez de negro

### Problema actual
La sección Inn usa `background:#111111` — igual que Trust Bar. Crea un bloque oscuro pesado sin respiración visual.

### Fix

```html
<!-- Cambiar el background de la sección Inn -->
<!-- ANTES -->
<section style="padding:140px 0;background:#111111">

<!-- DESPUÉS -->
<section style="padding:140px 0;background:var(--cream);position:relative;overflow:hidden">
```

**Ajustes de texto dentro del Inn** (de blanco a oscuro):

```html
<!-- H2 -->
<!-- ANTES: color:#ffffff -->
<h2 style="...;color:#ffffff;...">

<!-- DESPUÉS: color:var(--dark) -->
<h2 style="...;color:var(--dark);...">

<!-- Párrafo descriptivo -->
<!-- ANTES: color:rgba(255,255,255,0.7) -->
<p style="...;color:rgba(255,255,255,0.7);...">

<!-- DESPUÉS: color:var(--muted) -->
<p style="...;color:var(--muted);...">
```

**Gradiente de foto** (de negro a cream):

```html
<!-- ANTES -->
<div style="position:absolute;inset:0;background:linear-gradient(to right,transparent 60%,#111111 100%)"></div>

<!-- DESPUÉS -->
<div style="position:absolute;inset:0;background:linear-gradient(to right,transparent 55%,var(--cream) 100%)"></div>
```

**Price tag** (de oscuro a cream):

```html
<!-- ANTES -->
<div style="...;background:rgba(20,184,166,0.15);...">
  <p style="...;color:#2dd4bf;...">DESDE</p>
  <p style="...;color:#14b8a6;...">$18 ...</p>

<!-- DESPUÉS -->
<div style="...;background:rgba(253,246,236,0.95);border:1px solid rgba(20,184,166,0.3);backdrop-filter:blur(12px);...">
  <p style="...;color:var(--inn-d);...">DESDE</p>
  <p style="...;color:var(--inn-d);...">$18 ...</p>
```

**CTAs** (de outline blanco a outline turquesa):

```html
<!-- Botón secundario -->
<!-- ANTES: border:2px solid rgba(255,255,255,0.4);color:#fff -->
<!-- DESPUÉS: border:2px solid var(--inn);color:var(--inn-d) -->
```

**Texto decorativo de fondo** — agregar en la sección:
```css
/* En style.css o inline en la sección */
.inn-section::before {
  content: "INN";
  position: absolute;
  font-family: 'Fraunces', serif;
  font-weight: 900;
  font-size: 22vw;
  color: var(--inn);
  opacity: 0.04;
  right: -5%;
  top: 50%;
  transform: translateY(-50%) rotate(-8deg);
  pointer-events: none;
  line-height: 1;
  white-space: nowrap;
}
```

---

## Cambio 2 — Eliminar SVG curva entre Trust Bar e Inn

La curva SVG ya no aplica porque Inn no es oscuro.

```html
<!-- ELIMINAR este bloque completo -->
<svg viewBox="0 0 1440 48" ...>
  <path d="M0,48 C360,0 1080,0 1440,48 L1440,0 L0,0 Z" fill="#111111"/>
</svg>
```

---

## Cambio 3 — Transición entre secciones: Línea + Scale Reveal (Opción C)

### CSS a agregar en `style.css`

```css
/* ─── DIVIDER LINE — crece de izquierda a derecha al entrar en viewport ─── */
.divider-line {
  height: 2px;
  background: transparent;
  position: relative;
  overflow: hidden;
  margin: 0;
}
.divider-line::after {
  content: "";
  position: absolute;
  top: 0; left: 0;
  height: 100%;
  width: 0;
  background: var(--red);
  transition: width 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.divider-line.in::after { width: 100%; }

/* ─── SCALE REVEAL — secciones aparecen con scale sutil ─── */
.scale-in {
  opacity: 0;
  transform: scale(0.97) translateY(24px);
  transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}
.scale-in.in {
  opacity: 1;
  transform: scale(1) translateY(0);
}

/* ─── NÚMERO DE SECCIÓN — aparece desde la derecha ─── */
.sec-number {
  font-family: 'Fraunces', serif;
  font-size: 8rem;
  font-weight: 800;
  color: transparent;
  -webkit-text-stroke: 1px rgba(201, 37, 45, 0.12);
  position: absolute;
  top: 40px;
  right: 40px;
  line-height: 1;
  pointer-events: none;
  opacity: 0;
  transform: translateX(30px);
  transition: opacity 0.8s ease 0.3s, transform 0.8s cubic-bezier(0.22, 1, 0.36, 1) 0.3s;
}
.scale-in.in .sec-number { opacity: 1; transform: translateX(0); }
```

### HTML — agregar entre cada sección

```html
<!-- Entre Trust Bar e Inn -->
<div class="divider-line" data-anim="line"></div>

<!-- Sección Inn: agregar clase + data-anim + número -->
<section style="padding:140px 0;background:var(--cream);..." class="scale-in" data-anim="scale" style="position:relative">
  <div class="sec-number">01</div>
  <!-- contenido existente... -->
</section>

<!-- Entre Inn y Atracciones -->
<div class="divider-line" data-anim="line"></div>

<!-- Sección Atracciones -->
<section style="padding:140px 0;background:#ffffff" class="scale-in" data-anim="scale" style="position:relative">
  <div class="sec-number">02</div>
  <!-- contenido existente... -->
</section>

<!-- Entre Atracciones y Reviews -->
<div class="divider-line" data-anim="line"></div>

<!-- Sección Reviews -->
<section style="padding:130px 0 120px;background:var(--cream);..." class="scale-in" data-anim="scale" style="position:relative">
  <div class="sec-number" style="-webkit-text-stroke:1px rgba(201,37,45,0.08)">03</div>
  <!-- contenido existente... -->
</section>

<!-- Entre Reviews y Brand Cards -->
<div class="divider-line" data-anim="line"></div>

<!-- Sección Brand Cards -->
<section style="padding:140px 0;background:#f4f4f4" class="scale-in" data-anim="scale" style="position:relative">
  <div class="sec-number">04</div>
  <!-- contenido existente... -->
</section>

<!-- Entre Brand Cards y CTA Final -->
<div class="divider-line" data-anim="line"></div>

<!-- CTA Final -->
<section style="position:relative;overflow:hidden;..." class="scale-in" data-anim="scale">
  <!-- contenido existente... -->
</section>
```

### JS — agregar en `main.js` (o al final del `index.html` antes de `</body>`)

```js
// ─── SECTION ANIMATIONS — Divider Line + Scale Reveal ───
(function () {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('[data-anim]').forEach(el => io.observe(el));
})();
```

> **Nota:** Si `main.js` ya tiene un IntersectionObserver para `.fade-up`, fusionar ambos en un solo observer en vez de crear uno nuevo. Solo agregar `'[data-anim]'` al selector existente.

---

## Cambio 4 — Texto decorativo en secciones

Agregar en `style.css` para las secciones que no lo tienen:

```css
/* Atracciones */
section[id="atracciones"]::before,
.att-section::before {
  content: "SUCRE";
  position: absolute;
  font-family: 'Fraunces', serif;
  font-weight: 900;
  font-size: 20vw;
  color: var(--red);
  opacity: 0.04;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%) rotate(3deg);
  pointer-events: none;
  white-space: nowrap;
  z-index: 0;
}

/* Reviews */
.rev-section::before {
  content: "LOVE";
  position: absolute;
  font-family: 'Fraunces', serif;
  font-weight: 900;
  font-size: 22vw;
  color: var(--dark);
  opacity: 0.04;
  right: -3%; top: 5%;
  pointer-events: none;
  white-space: nowrap;
}
```

---

## Resumen de archivos a modificar

| Archivo | Cambio |
|---|---|
| `index.html` | Cambios 1, 2 y 3 (fondo Inn, SVG eliminado, clases + dividers) |
| `css/style.css` | Cambio 3 (CSS: `.divider-line`, `.scale-in`, `.sec-number`) + Cambio 4 (textos decorativos) |
| `js/main.js` | Cambio 3 (JS: IntersectionObserver para `[data-anim]`) |

---

## Variables CSS del Inn (ya deben existir en `:root` de `style.css`)

```css
:root {
  /* Inn — agregar si no existen */
  --inn:      #14b8a6;
  --inn-dark: #0f766e;
  --inn-light:#2dd4bf;
  --inn-pale: #99f6e4;
}
```

---

*Documento preparado el 24 de Abril, 2026.*
*Complementa: Me Gusta Sucre — Handoff Index.md*
