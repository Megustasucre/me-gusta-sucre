# Auditoría UX/UI — guia.html
### Handoff para Claude Code · Me Gusta Sucre · Abril 2026

---

## PRIORIDAD 1 — 🔴 Crítico

### 1. Sistema de fondos — reducir de 6 a 3 valores

**Problema:** La página alterna entre 6 fondos sin ritmo visual:
`#fafafa` / `#fdf6ec` / `#fff` / `#f4f4f4` / `#111` / `#0d0d0d`

**Solución:** Unificar en 3 valores del design system:

```
Cálido editorial:  #fdf6ec  (--cream)     → manifiesto, crónicas, social proof
Neutro funcional:  #ffffff  (--white)     → about, food, day trips
Oscuro premium:    #111111               → stats bar, practical tips, closing
```

**Cambios concretos en el HTML:**

| Sección | Fondo actual | Fondo nuevo |
|---|---|---|
| `<body>` | `#fafafa` | `#ffffff` |
| Los Capítulos | `#fff` | `#ffffff` ✓ ya correcto |
| Must-See Spots | `#f4f4f4` | `#fdf6ec` |
| About the City | `#fff` | `#ffffff` ✓ |
| Social Proof | `#fdf6ec` | `#fdf6ec` ✓ |
| Food & Coffee | `#fff` | `#ffffff` ✓ |
| Las Crónicas | `#fdf6ec` | `#fdf6ec` ✓ |
| Closing section | `#0d0d0d` | `#111111` |

Buscar y reemplazar en el archivo:
- `background:#fafafa` → `background:#fff`
- `background:#f4f4f4` → `background:#fdf6ec`
- `background:#0d0d0d` → `background:#111111`

---

### 2. Border-radius — definir sistema consistente

**Problema:** Mezcla de `border-radius:32px` (chapter cards, spot cards, crónicas cards, practical tips cards) con elementos de esquina recta (botones, pills, brand cards). Rompe la identidad editorial.

**Decisión de diseño:** La marca Me Gusta usa estética editorial de líneas rectas. Los radios grandes son inconsistentes.

**Cambios:**

**Chapter cards** — cambiar `border-radius:32px` → `border-radius:0`:
```html
<!-- Buscar en las 4 chapter cards: -->
<div class="chapter-inner" style="...border-radius:32px...">
<!-- Reemplazar por: -->
<div class="chapter-inner" style="...border-radius:0...">
```

**Spot cards y Day Trip cards** — cambiar `border-radius:32px` → `border-radius:0`:
```html
<!-- En cada .spot-card y .modal-card del carrusel: -->
style="...border-radius:32px..."
<!-- → -->
style="...border-radius:0..."
```

**Crónicas cards** — cambiar `border-radius:32px` → `border-radius:0`:
```html
style="background:#fff;border-radius:32px;overflow:hidden..."
<!-- → -->
style="background:#fff;border-radius:0;overflow:hidden..."
```

**Practical Tips cards** — cambiar `border-radius:28px` → `border-radius:0`:
```html
style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:28px..."
<!-- → -->
style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:0..."
```

**Closing section cards** — cambiar `border-radius:40px` → `border-radius:0`:
```html
style="...border-radius:40px;overflow:hidden..."
<!-- → -->
style="...border-radius:0;overflow:hidden..."
```

**Excepción permitida:** El badge flotante del café (`.cafe-badge`) y el badge del "Why travelers love it" pueden mantener `border-radius` como detalle decorativo.

---

## PRIORIDAD 2 — 🟡 Importante

### 3. Eliminar el breadcrumb o reposicionarlo

**Problema:** El breadcrumb `Home / City Guide` aparece entre el hero y el manifiesto, cortando el flujo emocional después de la imagen cinematográfica.

**Solución A (recomendada):** Eliminarlo completamente. La navbar ya indica la página activa con `nav-active`.

**Solución B:** Moverlo al top bar pre-navbar, antes de la sección hero.

```html
<!-- ELIMINAR este bloque completo: -->
<div style="background:#f4f4f4;border-bottom:1px solid #e5e5e5;padding:14px 0">
  <div class="max-w-7xl mx-auto px-6">
    <p style="font-size:13px;color:#555555">
      <a href="index.html" style="color:#c9252d;text-decoration:none;font-weight:600">Home</a> / City Guide
    </p>
  </div>
</div>
```

---

### 4. Mover Quick Facts Bar — después de "About the City"

**Problema:** La barra `2810m / 1538 / 1991 / 300+` aparece entre "Los Capítulos" y "About the City", separando dos secciones que deben fluir juntas.

**Solución:** Cortar el bloque `<!-- QUICK FACTS BAR -->` y pegarlo **inmediatamente después** del cierre de la sección `<!-- ═══ INTRO: ABOUT THE CITY ════ -->`.

Nuevo orden:
```
[Los Capítulos]
[About the City]        ← sección #about
[Quick Facts Bar]       ← MOVIDO AQUÍ
[Social Proof]
[Must-See Spots]
...
```

---

### 5. Eliminar el bloque "Pro Tip" standalone — contenido duplicado

**Problema:** El Pro Tip del ají aparece dos veces:
1. Como bloque oscuro standalone entre Day Trips y Food
2. Integrado dentro de la sección Food con el ícono de pin

**Solución:** Eliminar el bloque standalone. Mantener solo la versión integrada dentro de Food.

```html
<!-- ELIMINAR este bloque completo: -->
<div class="fade-up" style="background:#111;padding:48px 0">
  <div class="max-w-3xl mx-auto px-6">
    <div style="border-left:4px solid #c9252d;padding:24px 28px;background:rgba(255,255,255,0.03);border-radius:0 12px 12px 0">
      <p style="...">Pro Tip — Local Knowledge</p>
      <p style="...">The secret ingredient of Sucre's cuisine</p>
      <p style="...">Sucre's aji...</p>
    </div>
  </div>
</div>
```

---

### 6. Modal — botón de cierre

**Problema:** El botón de cierre del modal dice literalmente `X` en texto plano.

**Solución:** Reemplazar con SVG:

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

---

### 7. Social Proof — añadir contexto

**Problema:** Los números `4.9 / 750+ / 15` flotan sin que el visitante sepa a qué se refieren.

**Solución:** Añadir un subtítulo de contexto encima del bloque de números:

```html
<!-- AÑADIR antes de los números: -->
<p style="font-size:12px;font-weight:700;color:#888;text-transform:uppercase;letter-spacing:2px;margin-bottom:8px">
  Me Gusta Sucre — Spanish School · Inn · Café
</p>
```

---

### 8. Hero — aumentar tamaño de tipografía

**Problema:** El hero de `guia.html` usa `clamp(2.2rem, 5vw, 3.8rem)`. El de `clases.html` usa `clamp(3rem, 6vw, 5.2rem)`. La guía es el contenido más premium — debería ser igual o mayor.

**Solución:**

```html
<!-- ANTES: -->
style="font-family:'Fraunces',serif;font-size:clamp(2.2rem,5vw,3.8rem);..."

<!-- DESPUÉS: -->
style="font-family:'Fraunces',serif;font-size:clamp(2.8rem,5.5vw,4.8rem);..."
```

---

## PRIORIDAD 3 — 🟢 Menor

### 9. Contadores en carruseles

**Problema:** El usuario no sabe cuántos spots hay en el carrusel.

**Solución:** Añadir un contador simple después de cada track:

```html
<!-- Después del #spots-track, antes de los nav arrows: -->
<div style="text-align:center;margin-top:16px;font-size:12px;font-weight:700;color:#999;letter-spacing:1px">
  <span id="spots-counter">1 / 9</span>
</div>
```

Y en el JS, actualizar el contador al hacer scroll:
```js
spotsTrack.addEventListener('scroll', function() {
  var index = Math.round(spotsTrack.scrollLeft / 384) + 1;
  var total = document.querySelectorAll('#spots-track .spot-card').length;
  var counter = document.getElementById('spots-counter');
  if (counter) counter.textContent = Math.min(index, total) + ' / ' + total;
});
```

Repetir para `#daytrips-track` con id `daytrips-counter` y total 4.

---

### 10. Verificar rutas de logos faltantes

**Problema:** El badge del café y el card del Inn referencian logos que probablemente no existen:
- `imagenes/logos/me-gusta-cafe.png`
- `imagenes/logos/logo-me-gusta-inn.png`

En el proyecto solo existen:
- `logo-me-gusta-spanish.png`
- `logo-me-gusta-sucre-chinchilla.png`

**Solución:**
- Si no existen los archivos, usar `logo-me-gusta-sucre-chinchilla.png` como fallback para el Inn
- Para el Café, eliminar la imagen y usar solo texto, o crear el archivo correspondiente

```html
<!-- CAFE BADGE — fallback si me-gusta-cafe.png no existe: -->
<img src="imagenes/logos/logo-me-gusta-sucre-chinchilla.png" ...>

<!-- INN CARD — fallback si logo-me-gusta-inn.png no existe: -->
<img src="imagenes/logos/logo-me-gusta-sucre-chinchilla.png" ...>
```

---

### 11. Fix `z-index` en closing section

**Problema:** El div con `z-1` en la closing section puede no funcionar sin `position:relative` explícito.

**Solución:**

```html
<!-- ANTES: -->
<div class="max-w-7xl mx-auto px-6 relative z-1">

<!-- DESPUÉS: -->
<div class="max-w-7xl mx-auto px-6" style="position:relative;z-index:1">
```

---

### 12. Refactorizar `data-i18n-html` — frágil

**Problema:** Varios textos usan `data-i18n-html` para incluir `<span style="...">` dentro del JSON de traducciones. Si el JSON tiene un error, rompe el HTML visible.

**Patrón problemático:**
```html
<h2 data-i18n-html="guia.aboutTitle">Bolivia's most <span style="color:#c9252d;font-style:italic">livable</span> city</h2>
```

**Solución:** Separar el acento en HTML estático y solo traducir el texto:
```html
<h2>
  <span data-i18n="guia.aboutTitlePre">Bolivia's most</span>
  <span style="color:#c9252d;font-style:italic" data-i18n="guia.aboutTitleAccent">livable</span>
  <span data-i18n="guia.aboutTitlePost">city</span>
</h2>
```

Actualizar `translations.js` con las nuevas keys para EN / ES / FR.

---

### 13. Sticky filters — z-index en mobile

**Problema:** Los filtros usan `position:sticky;top:80px`. Si el navbar cambia de altura en mobile (< 375px), los filtros pueden solaparse.

**Solución:** Añadir media query:

```css
@media (max-width: 640px) {
  #spot-filters {
    top: 64px; /* altura reducida del navbar en mobile */
  }
}
```

---

## Orden de implementación recomendado

```
1. Sistema de fondos (buscar/reemplazar — 10 min)
2. Border-radius → 0 (buscar/reemplazar — 15 min)
3. Eliminar breadcrumb (borrar bloque — 2 min)
4. Mover Quick Facts Bar (cortar/pegar — 5 min)
5. Eliminar Pro Tip duplicado (borrar bloque — 2 min)
6. Modal close button SVG (reemplazar — 3 min)
7. Social proof contexto (añadir línea — 2 min)
8. Hero font-size (reemplazar valor — 1 min)
9. Contadores carrusel (añadir HTML + JS — 10 min)
10. Verificar rutas de logos (revisar archivos — 5 min)
11. Fix z-index closing (reemplazar clase — 1 min)
12. Refactorizar data-i18n-html (requiere translations.js — 20 min)
13. Sticky filters mobile (añadir CSS — 2 min)
```

**Tiempo total estimado:** ~80 min

---

*Auditoría realizada por Claude · Me Gusta Sucre · Abril 2026*
