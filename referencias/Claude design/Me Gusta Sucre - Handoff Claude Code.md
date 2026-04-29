# Handoff: Me Gusta Sucre — Index Redesign + Mejoras UX

## Overview

Este documento es una hoja de ruta técnica para implementar las mejoras de UX/UI identificadas en el sitio `megustasucre.com`. Está basado en el análisis de 4 documentos (Antigravity IA, review.md, Observaciones del cliente, Observación IA) y la revisión del `index.html` actual.

El sitio ya tiene una base sólida. Los cambios son quirúrgicos: reordenar secciones del index, migrar tipografía en subpáginas, y mejorar la página de Merch.

---

## Fidelidad

**Alta fidelidad para el index** — el orden de secciones, jerarquía de CTAs y tokens de diseño están definidos con precisión. Implementar tal cual.

**Referencia estructural para subpáginas** — las subpáginas necesitan migración de tipografía y consistencia de variables CSS; el layout existente se mantiene.

---

## Problema central (contexto)

El sitio mezcla "guía turística de Sucre" con "hub de negocios Me Gusta". La solución es una **narrativa del viajero** clara:

> "Me Gusta Sucre es tu base en Sucre — te damos dónde quedarte, dónde comer, cómo aprender y cómo disfrutar la ciudad."

El Inn es la **conversión principal** (reserva = ingreso directo). Spanish y Café son servicios secundarios ("mientras estás aquí").

---

## Cambio 1 — Reordenar secciones de `index.html`

### Orden actual
```
Hero → Ticker → Trust Bar → Brand Cards (Inn+Spanish+Café+Merch) → Atracciones → Reviews → CTA Final → Footer
```

### Orden propuesto
```
Hero → Ticker → Trust Bar → INN (sección propia) → Atracciones → Reviews → "Mientras estás aquí" (Spanish+Café+Merch) → CTA Final → Footer
```

### Por qué este orden

| Momento del viajero | Sección |
|---|---|
| ¿Es Sucre para mí? | Hero + Trust Bar |
| ¿Dónde me quedo? | **Inn — conversión inmediata** |
| ¿Qué voy a hacer allá? | Atracciones |
| ¿Puedo confiar en ellos? | **Reviews — cierra el argumento antes del scroll** |
| ¿Qué más ofrecen? | Spanish + Café + Merch — compactos, secundarios |
| Ok, reservo | CTA Final |

---

## Cambio 2 — Nueva sección "Inn" (reemplaza Brand Cards para Inn)

Sacar el Inn de las Brand Cards y darle su propia sección prominente.

### Layout
- **Fondo:** `#111111`
- **Grid:** 2 columnas en desktop (`1fr 1fr`), 1 columna en mobile
- **Columna izquierda:** Foto principal del Inn (usar Unsplash temporal hasta tener foto real: `https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=1200&fm=webp&q=80`)
- **Columna derecha:** Contenido

### Contenido columna derecha
```
Eyebrow:  "Me Gusta Sucre Inn"          color: #14b8a6   font-size: 11px   letter-spacing: 4px   uppercase
H2:       "Tu Casa en\nSucre"           font: Fraunces 800   size: clamp(2.4rem, 4vw, 3.5rem)   color: #ffffff
Subhead:  "Hostal boutique en el corazón del centro histórico.
           Desayuno incluido, WiFi y atención personalizada
           desde el primer mensaje."
          color: rgba(255,255,255,0.7)   font-size: 15px   line-height: 1.85

4 amenities en fila:
  [✓ Desayuno incluido]  [✓ WiFi gratis]  [✓ Centro histórico]  [✓ WhatsApp 24h]
  Estilo: badge redondeado, background: rgba(20,184,166,0.15), border: rgba(20,184,166,0.3), color: #2dd4bf

Precios desde:
  Label:  "DESDE"   font-size: 10px   letter-spacing: 2px   color: rgba(255,255,255,0.5)
  Price:  "$18 / noche"   font: Fraunces 700   font-size: 2.2rem   color: #14b8a6

CTAs:
  Primario:   "Ver Habitaciones →"    .btn estilo turquesa   background: #14b8a6   color: #fff
  Secundario: "WhatsApp directo"      .btn outline blanco
  → ambos linkean a hospedaje.html#reservar
```

### Responsive
- Mobile: columna de foto 300px de alto, luego contenido
- Foto con overlay `linear-gradient(to right, rgba(0,0,0,0.3), transparent)` en desktop

---

## Cambio 3 — "Mientras estás aquí" (reemplaza Brand Cards para Spanish+Café+Merch)

Las Brand Cards existentes se convierten en una sección de **3 columnas compactas** con tono secundario.

### Layout
- **Fondo:** `#f4f4f4`
- **Eyebrow:** "Mientras estás aquí"   color: `var(--red)`
- **H2:** "Aprende, Saborea y Llévate algo"   font: Fraunces 800
- **Grid:** 3 columnas en desktop, 1 en mobile
- **Cards:** mantener las Brand Cards existentes de Spanish, Café y Merch (sin Inn)
- **Orden de cards:** Spanish → Café → Merch

### Cambio de orden en Brand Cards
El orden actual es: Inn, Spanish, Café, Merch.
El nuevo orden (sin Inn): **Spanish, Café, Merch**.

---

## Cambio 4 — Reviews sube (antes de "Mientras estás aquí")

Mover la sección de testimonios (marquee infinito) para que quede **entre Atracciones y "Mientras estás aquí"**.

No cambiar el componente — solo moverlo en el HTML.

---

## Cambio 5 — Migración tipográfica en subpáginas

### Problema
`index.html` ya usa `Fraunces` + `Plus Jakarta Sans`. Las demás páginas siguen con `Lora` + `DM Sans` en estilos inline.

### Páginas afectadas
- `cafe.html`
- `guia.html`
- `hospedaje.html`
- `merchandising.html`
- `clases.html`
- `contacto.html`

### Qué cambiar en cada una

**1. Google Fonts `<link>` en `<head>`**

Reemplazar:
```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:...&family=Lora:...&family=Satisfy&display=swap" rel="stylesheet" />
```
Por:
```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,700;0,9..144,800;1,9..144,700;1,9..144,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Sacramento&display=swap" rel="stylesheet" />
```

**2. Reemplazos globales en cada archivo**

| Buscar | Reemplazar por |
|---|---|
| `font-family:'Lora',serif` | `font-family:'Fraunces',serif` |
| `font-family:'DM Sans',sans-serif` | `font-family:'Plus Jakarta Sans',sans-serif` |
| `font-family:'Satisfy',cursive` | `font-family:'Sacramento',cursive` |
| `font-family: 'Lora'` | `font-family: 'Fraunces'` |
| `font-family: 'DM Sans'` | `font-family: 'Plus Jakarta Sans'` |

**3. Variables CSS hardcodeadas**

Buscar y reemplazar colores inline:

| Hex hardcodeado | Variable |
|---|---|
| `#c9252d` | `var(--red)` |
| `#a01c23` | `var(--red2)` |
| `#e8a020` | `var(--gold)` |
| `#1a120a` | `var(--dark)` |
| `#fdf6ec` | `var(--cream)` |
| `#555555` | `var(--muted)` |
| `#111111` | `var(--text)` |

---

## Cambio 6 — Mejora de `merchandising.html`

### Problema actual
6 productos sin precio, sin mecanismo de compra claro, sin propuesta de valor.

### Propuesta: Catálogo visual + compra por WhatsApp (MVP sin e-commerce)

**Secciones:**

**A. Hero** (mantener estructura actual con `sucre_street.webp`)
- Eyebrow: "Me Gusta Merch"
- H1: "Llévate un pedazo de Sucre"
- Subhead: "Diseñado en Sucre, hecho para durar."
- CTA: "Ver Catálogo ↓"

**B. Propuesta de valor — 3 bullets**
```
📍 Diseñado en Sucre        — Cada pieza refleja la identidad de la Ciudad Blanca
🌱 Materiales de calidad    — Algodón 100%, impresión durable
📦 Envío nacional           — Entrega a todo Bolivia vía Tigo Money
```
Layout: 3 columnas, fondo `var(--cream)`, iconos SVG simples.

**C. Grid de productos — 6 cards**

Cada card debe tener:
```
- Foto del producto (imagen actual o placeholder)
- Nombre del producto
- Descripción corta (1 línea)
- PRECIO en Bs (hardcodeado — acordar con cliente)
- Badge de disponibilidad: "Disponible" (verde) o "Próximamente" (gris)
- CTA: "Pedir por WhatsApp →"
  href: https://wa.me/59173425725?text=Hola!%20Me%20interesa%20[NOMBRE_PRODUCTO]
```

Precios sugeridos (confirmar con cliente):
| Producto | Precio Bs |
|---|---|
| Camiseta | 120 Bs |
| Tote bag | 65 Bs |
| Mug | 55 Bs |
| Hoodie | 220 Bs |
| Libros | 85 Bs |
| Gift set | 280 Bs |

**D. CTA final**
```
Fondo: var(--dark)
Texto: "¿Querés algo personalizado?"
Sub:   "Escribinos y lo coordinamos directamente."
CTA:   "Contactar por WhatsApp" → wa.me/59173425725
```

---

## Cambio 7 — Jerarquía del nav

### Problema
6 ítems al mismo nivel visual. El usuario no sabe qué es primario.

### Propuesta
Separar visualmente en 2 grupos:

**Primario** (izquierda del logo): `City Guide` · `Stay`
**Secundario** (derecha del logo): `Café` · `Classes` · `Merch` · `Contact`

Implementación:
- Links primarios: `font-weight: 700`, color normal
- Links secundarios: `font-weight: 600`, `color: rgba(255,255,255,0.75)` sobre hero, `var(--muted)` al scrollear
- En mobile: mismo orden, pero separados por un divisor sutil

---

## Tokens de diseño

```css
:root {
  --red:    #c9252d;
  --red2:   #a01c23;
  --gold:   #e8a020;
  --gold2:  #d18c15;
  --dark:   #1a120a;
  --cream:  #fdf6ec;
  --cream2: #f7f0e4;
  --text:   #111111;
  --muted:  #555555;
  --white:  #ffffff;

  /* Por producto */
  --inn:       #14b8a6;
  --inn-dark:  #0f766e;
  --inn-light: #2dd4bf;
  --inn-pale:  #99f6e4;
  --spanish:   #FF3B6B;
  --cafe:      #5aaa6a;
  --merch:     #e8a020;
}
```

**Tipografía:**
| Uso | Familia | Peso |
|---|---|---|
| Titulares (H1, H2, H3) | Fraunces, serif | 700–800 |
| Titulares itálicos / accent | Fraunces, serif | italic 700 |
| UI / body / nav / botones | Plus Jakarta Sans | 400–700 |
| Handwritten accent | Sacramento, cursive | 400 |

**Espaciado luxury:**
- Secciones principales: `padding: 130px 0` → clase `.section-luxury` ya en `style.css`
- Max-width contenido: `max-width: 1280px; margin: 0 auto; padding: 0 32px`

---

## Terminología fija (no cambiar)

| ❌ No usar | ✅ Usar |
|---|---|
| "boutique inn" / "posada boutique" | "hostal" |
| "specialty coffee" / "single-origin" | "café boliviano" |
| "boutique hotel" | "hostal boutique" |
| "posada" | "hostal" |

---

## Pendiente (fuera del scope de este handoff)

Estas tareas requieren decisiones adicionales del cliente:

- **Chatbot** — solo para Spanish, Inn y Merch (no Café). Plataforma sin decidir: Tidio, Crisp, o simulado con WhatsApp.
- **E-commerce Takenos** — merch, vouchers de clase, reservas. Requiere cuenta en Takenos.
- **Blog de turismo** — evolución de `guia.html` a blog editorial con artículos por categoría (gratuito, de pago, familiar, entretenimiento).
- **Fotos reales** — Inn (habitaciones, fachada), Café (interior, patio, barra), Clases (aula, profesores).
- **Actividades / Me Gusta Trekkers** — página nueva, aún no definida.
- **og:image PNG** — exportar `imagenes/og-image.svg` a PNG 1200×630 para previews de WhatsApp/Facebook.

---

## Archivos del proyecto

```
/
├── index.html              ← Cambios 1-4 (reordenar secciones)
├── merchandising.html      ← Cambio 6 (catálogo con precios + WhatsApp)
├── cafe.html               ← Cambio 5 (migración tipográfica)
├── guia.html               ← Cambio 5 (migración tipográfica)
├── hospedaje.html          ← Cambio 5 (migración tipográfica)
├── clases.html             ← Cambio 5 (migración tipográfica)
├── contacto.html           ← Cambio 5 (migración tipográfica)
├── css/
│   ├── style.css           ← Design system (variables, componentes)
│   ├── tw.css              ← Tailwind v3 compilado (no editar directo)
│   └── tw-input.css        ← Input de Tailwind
├── js/
│   ├── translations.js     ← i18n EN/ES/FR
│   └── main.js             ← Lógica general (navbar scroll, fade-up, etc.)
└── imagenes/
    ├── logos/
    │   └── logo-me-gusta-sucre-chinchilla.png
    └── wikipedia/          ← Fotos propias (.webp)
```

---

## Notas para el dev

1. El sistema i18n sobreescribe el `textContent` del DOM al cargar — cualquier texto visible al usuario **debe estar en `translations.js`**, no solo en el HTML.
2. Para textos con HTML embebido (spans, links), usar `data-i18n-html` en vez de `data-i18n`.
3. Tailwind se compila con `npm run build:css` — no editar `tw.css` directamente.
4. El logo chinchilla ya existe en `/imagenes/logos/logo-me-gusta-sucre-chinchilla.png`.
5. Las fotos de Unsplash son temporales — dejar los `src` como están hasta recibir fotos reales.

---

*Documento preparado el 24 de Abril, 2026.*  
*Basado en: mejoras_IA_Antigravity.md · review.md · Nuevas observaciones · Observación IA.txt*
