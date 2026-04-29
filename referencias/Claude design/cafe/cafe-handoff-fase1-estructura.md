# Handoff para Claude Code — cafe.html (Rediseño Estructural Bridge Page)
*Arquitectura UX/UI Antigravity · 25 Abril 2026*

---

## Objetivo de la Página

`cafe.html` es una **Bridge Page** — su único objetivo es enviar tráfico calificado al **sitio web propio del café** (URL pendiente de confirmar), de la misma manera que `clases.html` envía tráfico a `megustaspanish.com`.

**No es el destino final. Es el puente.**

El modelo espejo es exacto:

| `clases.html` | `cafe.html` |
|---|---|
| Bridge → `megustaspanish.com` | Bridge → `[URL café — pendiente]` |
| CTA: "Go to Me Gusta Spanish ↗" | CTA: "Visit Me Gusta Café ↗" |
| Sección de programas como teaser | Sección de cafés como teaser |
| Sin precios ni horarios de clases | Sin menú completo ni precios |

> ⚠️ **URL pendiente:** El sitio web del café aún no existe. Usar `href="#"` como placeholder en todos los CTAs primarios hasta que se confirme la URL. Una vez lista, reemplazar todos los `href="#"` por la URL definitiva en el HTML y en `translations.js`.

---

## Estructura Final Aprobada

```
1. HERO         — cinematográfico 75vh             [OSCURO]
2. INFO BAR     — dirección + horarios             [OSCURO chocolate]
3. SPLIT        — historia + carrusel              [BLANCO]
4. DOS CAFÉS    — con foto de fondo + glassmorphism [OSCURO chocolate con foto]
5. CTA FINAL    — crema premium                    [CLARO #fdf6ec]
6. FOOTER       — footer estándar del sitio        [OSCURO marrón]
```

> **Ritmo visual correcto:** `Oscuro → Oscuro → Blanco → Oscuro → Claro → Oscuro` — espejado de `clases.html`. El CTA en crema después del oscuro de los dos cafés crea el máximo contraste justo en el momento de conversión. Si tanto la sección de cafés como el CTA fueran oscuros, el usuario no distingue dónde termina una y empieza la otra.

---

## Instrucciones de Cambio

---

### SECCIÓN 1 — Hero (modificar existente)

**Localizar** la sección del Hero (línea ~154) y aplicar los siguientes cambios:

**A. Ampliar la altura:**
```html
<!-- ANTES -->
<section style="position:relative;height:440px;display:flex;align-items:flex-end;overflow:hidden">

<!-- DESPUÉS -->
<section style="position:relative;height:75vh;min-height:520px;display:flex;align-items:flex-end;overflow:hidden">
```

**B. Añadir subtítulo debajo del H1** (insertar después del `<h1>`, antes de los botones):
```html
<p style="font-size:16px;color:rgba(255,255,255,0.68);line-height:1.85;max-width:480px;margin-bottom:28px" data-i18n="cafe.introP">Single-origin Bolivian coffee, homemade pastries and honest food — in the heart of Sucre's historic center. The kind of place where one hour turns into three.</p>
```

**C. Reemplazar los botones del Hero:**
```html
<!-- ANTES -->
<a href="#menu" class="cafe-btn-primary" ...>See the Menu</a>
<a href="contacto.html" class="cafe-btn-outline" ...>Find Us</a>

<!-- DESPUÉS -->
<a href="#" class="cafe-btn-primary" style="padding:12px 28px" data-i18n="cafe.heroCta1">Visit Me Gusta Café ↗</a>
<a href="#cafe-info" class="cafe-btn-outline" style="padding:12px 28px" data-i18n="cafe.heroCta2">Hours &amp; Location</a>
```

> `href="#"` es el placeholder hasta que la URL del sitio del café esté lista.

---

### SECCIÓN 2 — Info Bar (corregir datos)

**Localizar** el div `background:#2c1a0e` del Info Bar (línea ~181).

**A. Corregir el horario:**
```html
<!-- ANTES -->
data-i18n="cafe.hours">Mon–Sun · 7:00 am – 8:00 pm

<!-- DESPUÉS -->
data-i18n="cafe.hours">Mon–Sat · 7:00 am – 8:00 pm
```

**B. Reemplazar el ítem de email** por un descriptor del producto. Localizar el `<div>` que contiene el SVG de email y `info@megustasucre.com` y reemplazarlo por:
```html
<div style="display:flex;align-items:center;gap:10px">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="#8b4513"><path d="M20 3H4v10c0 2.21 1.79 4 4 4h6c2.21 0 4-1.79 4-4v-3h2c1.11 0 2-.89 2-2V5c0-1.11-.89-2-2-2zm0 5h-2V5h2v3zM4 19h16v2H4z"/></svg>
  <span style="font-size:14px;color:rgba(255,255,255,0.75)" data-i18n="cafe.tag1">Bolivian Coffee</span>
</div>
```

**C. Añadir el atributo `id="cafe-info"`** al div del Info Bar para que el anchor del Hero funcione:
```html
<div id="cafe-info" style="background:#2c1a0e;padding:20px 0;border-bottom:1px solid #3d2510">
```

---

### SECCIÓN 3 — Split Historia + Carrusel (modificar fondo)

**Localizar** la sección de presentación (línea ~201):
```html
<!-- ANTES -->
<section style="padding:72px 0;background:#fdf6ec">

<!-- DESPUÉS -->
<section style="padding:72px 0;background:#ffffff">
```

> Cambiar de crema a blanco puro para que no se fusione con el body. El cuerpo es crema — la sección interior necesita ser distinta.

---

### SECCIÓN 4 — DOS CAFÉS (insertar después del carrusel, antes del CTA actual)

**Insertar** esta nueva sección completa después del `</section>` del carrusel (línea ~275) y antes del CTA existente.

```html
<div class="divider-line" data-anim="line"></div>

<!-- ═══ DOS CAFÉS ═══════════════════════════════════════════════════ -->
<section style="background:#2c1a0e;padding:88px 0;position:relative;overflow:hidden">

  <!-- Textura radial sutil -->
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 20% 50%,rgba(90,170,106,0.06) 0%,transparent 60%),radial-gradient(ellipse at 80% 50%,rgba(139,69,19,0.08) 0%,transparent 60%);pointer-events:none"></div>

  <div class="max-w-5xl mx-auto px-6 relative">

    <div class="text-center fade-up" style="margin-bottom:56px">
      <p class="eyebrow mb-4" style="color:#5aaa6a" data-i18n="cafe.coffeeEyebrow">Our Coffees</p>
      <h2 style="font-family:'Fraunces',serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:800;color:#fff;line-height:1.1">
        <span data-i18n="cafe.coffeeTitle">Two origins.</span> <span style="color:#8b4513;font-style:italic" data-i18n="cafe.coffeeAccent">One great cup.</span>
      </h2>
    </div>

    <div class="grid md:grid-cols-2 gap-6">

      <!-- LAVAZZA -->
      <div class="fade-up" style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);padding:40px 36px;position:relative;backdrop-filter:blur(8px)">
        <div style="position:absolute;top:0;left:0;right:0;height:3px;background:#8b4513"></div>
        <p style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#8b4513;margin-bottom:12px" data-i18n="cafe.lavazzaType">Italian Coffee</p>
        <h3 style="font-family:'Fraunces',serif;font-size:1.7rem;font-weight:800;color:#fff;line-height:1.1;margin-bottom:20px">Lavazza</h3>
        <p style="font-size:15px;color:rgba(255,255,255,0.55);line-height:1.8" data-i18n="cafe.lavazzaDesc">One of the world's most recognized coffee brands. Italian blend with intense character, perfect crema and an aroma that fills the room. Our choice for espressos, lattes and cappuccinos.</p>
      </div>

      <!-- JAQAKU -->
      <div class="fade-up" style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);padding:40px 36px;position:relative;backdrop-filter:blur(8px);transition-delay:0.12s">
        <div style="position:absolute;top:0;left:0;right:0;height:3px;background:#5aaa6a"></div>
        <p style="font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#5aaa6a;margin-bottom:12px" data-i18n="cafe.jaqakuType">Bolivian Coffee</p>
        <h3 style="font-family:'Fraunces',serif;font-size:1.7rem;font-weight:800;color:#fff;line-height:1.1;margin-bottom:20px">Jaqaku</h3>
        <p style="font-size:15px;color:rgba(255,255,255,0.55);line-height:1.8" data-i18n="cafe.jaqakuDesc">Bolivian highland beans with their own identity. Jaqaku brings the unique flavors of Bolivia's valleys — smooth, aromatic, and with the character of our land.</p>
      </div>

    </div>
  </div>
</section>

<div class="divider-line" data-anim="line"></div>
```

---

### SECCIÓN 5 — CTA Final "Find Us" (reemplazar el CTA existente)

**Localizar** la sección CTA actual (línea ~297, con imagen de fondo de café) y **reemplazarla completamente** con:

```html
<!-- ═══ CTA FINAL — CAFÉ WEBSITE ════════════════════════════ -->
<section class="scale-in" data-anim="scale" style="background:#fdf6ec;padding:100px 24px">
  <div style="max-width:640px;margin:0 auto;text-align:center">

    <img src="imagenes/logos/me-gusta-cafe.png" alt="Me Gusta Café" style="height:72px;width:auto;margin:0 auto 32px;display:block" />

    <p style="font-family:'Sacramento',cursive;font-size:2rem;color:#8b4513;display:block;margin-bottom:20px" data-i18n="cafe.ctaTag">Bolivar #603</p>

    <h2 style="font-family:'Fraunces',serif;font-size:clamp(1.9rem,4vw,3rem);font-weight:800;color:#111;line-height:1.1;margin-bottom:24px" data-i18n="cafe.ctaTitle">The kind of place where one hour turns into three.</h2>

    <p style="font-size:15px;color:#666;line-height:1.85;margin-bottom:40px" data-i18n="cafe.ctaSub">Single-origin Bolivian coffee, homemade food, and a colonial patio in the heart of Sucre. Full menu and everything else — on the official website.</p>

    <div class="flex flex-wrap justify-center" style="gap:14px">
      <a href="#" target="_blank" class="cafe-btn-primary" style="padding:16px 44px;font-size:15px" data-i18n="cafe.ctaBtn">Discover Me Gusta Café ↗</a>
      <a href="https://maps.google.com/?q=Bolivar+603+Sucre+Bolivia" target="_blank" class="cafe-btn-outline" style="padding:16px 32px;font-size:15px" data-i18n="cafe.ctaBtn2">Find Us on Maps</a>
    </div>

    <p style="font-size:12px;color:#bbb;margin-top:28px;letter-spacing:1.5px;text-transform:uppercase" data-i18n="cafe.hours">Mon–Sat · 7:00 am – 8:00 pm</p>

  </div>
</section>
```

> **Por qué este copy:** La línea *"The kind of place where one hour turns into three"* ya estaba en `translations.js` como descripción del café. Es la mejor frase — evoca atmósfera, calma, conversación. Convertirla en el titular del CTA hace que el usuario no lea información, sino que **siente** el lugar antes de llegar.
>
> `href="#"` es placeholder para la URL del sitio del café.

---

### SECCIÓN 6 — Limpieza de código muerto

**Eliminar completamente** el bloque del Lightbox (líneas ~355–364):
```html
<!-- Eliminar este bloque completo: -->
<div id="lightbox" class="hidden fixed inset-0 ...">
  ...
</div>
```

**Corregir el orden de los scripts** — mover el WhatsApp float y los scripts para que queden dentro del `<body>`, en el siguiente orden justo antes de `</body>`:
```html
  <script src="js/translations.js"></script>
  <script src="js/main.js"></script>
  <a href="https://wa.me/59173425725" target="_blank" class="whatsapp-float" aria-label="WhatsApp">
    ...
  </a>
</body>
```

> **Nota:** El WhatsApp float del café usa el número del hostal (`59173425725`) que es el contacto general de Me Gusta Sucre. Esto está bien — es el único canal de contacto disponible para el ecosistema.

---

### SECCIÓN 7 — Corrección en `translations.js`

Localizar el bloque `"en" > "cafe"` y actualizar:
```js
"hours": "Mon–Sat · 7:00 am – 8:00 pm",
"heroCta1": "Visit Me Gusta Café ↗",
"heroCta2": "Hours & Location",
"ctaTag": "The coffee is ready.",
"ctaTitle": "Visit",
"ctaSub": "Full menu, hours, location — everything on the official website. Come before class, after class, or just because.",
"ctaBtn": "Go to Me Gusta Café ↗",
"ctaBtn2": "Bolivar #603 ↗",
"coffeeEyebrow": "Our Coffees",
"coffeeTitle": "Two origins.",
"coffeeAccent": "One great cup.",
```

Localizar el bloque `"es" > "cafe"` y actualizar:
```js
"hours": "Lun–Sáb · 7:00 am – 8:00 pm",
"heroCta1": "Visita Me Gusta Café ↗",
"heroCta2": "Horario y Ubicación",
"ctaTag": "El café está listo.",
"ctaTitle": "Visita",
"ctaSub": "Menú completo, horarios, ubicación — todo en el sitio web oficial. Ven antes de clases, después, o simplemente porque sí.",
"ctaBtn": "Ir a Me Gusta Café ↗",
"ctaBtn2": "Bolívar #603 ↗",
"coffeeEyebrow": "Nuestros Cafés",
"coffeeTitle": "Dos orígenes.",
"coffeeAccent": "Una gran taza.",
```

Localizar el bloque `"fr" > "cafe"` y actualizar:
```js
"hours": "Lun–Sam · 7h00 – 20h00",
"heroCta1": "Visiter Me Gusta Café ↗",
"heroCta2": "Horaires et Localisation",
"ctaTag": "Le café est prêt.",
"ctaTitle": "Visitez",
"ctaSub": "Menu complet, horaires, adresse — tout sur le site officiel. Venez avant les cours, après, ou juste parce que.",
"ctaBtn": "Aller sur Me Gusta Café ↗",
"ctaBtn2": "Bolivar #603 ↗",
"coffeeEyebrow": "Nos Cafés",
"coffeeTitle": "Deux origines.",
"coffeeAccent": "Une grande tasse.",
```

Corregir también en el Schema JSON-LD del `<head>` de `cafe.html`:
```json
// ANTES
"openingHours": "Mo-Sa 08:00-20:00"

// DESPUÉS  
"openingHours": "Mo-Sa 07:00-20:00"
```

---

### NOTA PENDIENTE — Botón de Menú

El botón "See the Menu" en el Hero quedará como link a Google Maps (`How to Find Us ↗`) por ahora. Cuando el cliente confirme el link del menú digital, Claude Code debe:
1. Restaurar el botón primario como "See the Menu ↗" con el link correcto
2. El botón "How to Find Us" pasa a ser secundario (outline)
3. Actualizar las keys `heroCta1` y `heroCta2` en los 3 idiomas

---

*Documento generado por Antigravity UX/UI Architect. Listo para ejecución en Claude Code.*
