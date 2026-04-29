# Handoff para Claude Code — clases.html
*Basado en observaciones Antigravity, 24 Abril 2026*

---

## Contexto

`clases.html` es una **Bridge Page**: su único objetivo es convencer al visitante de hacer click a `megustaspanish.com`. No es una página de detalles — es un teaser de alta conversión. No agregar horarios, precios ni perfiles de profesores directamente en la página.

---

## 1. Tipografía — URGENTE

El archivo puede estar usando `Lora` o `DM Sans` en algún punto. Reemplazar por:

| Uso | Fuente correcta |
|---|---|
| Títulos, display | `'Fraunces', serif` |
| Cuerpo, UI | `'Plus Jakarta Sans', sans-serif` |
| Handwriting accent | `'Sacramento', cursive` |

Verificar que el `<head>` tenga este import (o que `sucre-fonts.css` lo cubra):
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,700;0,9..144,800;1,9..144,700;1,9..144,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Sacramento&display=swap" rel="stylesheet">
```

Buscar y reemplazar en el HTML:
- `font-family: 'Lora'` → `font-family: 'Fraunces', serif`
- `font-family: 'DM Sans'` → `font-family: 'Plus Jakarta Sans', sans-serif`

---

## 2. Hero — Más Cinematográfico

El hero actual está bien estructurado pero necesita más impacto. Aplicar:

### Ken Burns animation en la imagen de fondo:
```css
@keyframes kenBurns {
  0%   { transform: scale(1.08) translate(0, 0); }
  100% { transform: scale(1) translate(-1%, 1%); }
}
.hero-kenburns {
  animation: kenBurns 18s ease-out forwards;
}
```

### Gradiente más dramático:
```html
<!-- Reemplazar el overlay actual por: -->
<div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(10,6,2,0.92) 0%,rgba(10,6,2,0.6) 55%,rgba(10,6,2,0.25) 100%)"></div>
```

### CTAs con más peso visual:
El botón principal ("See Prices & Courses") debe ser el elemento más prominente. Asegurarse de que:
- `padding: 18px 48px` (generoso)
- `background: #FF3B6B`
- `font-size: 16px; font-weight: 700`
- No hay botones del mismo peso visual cerca que compitan

---

## 3. Cards de Programas — Glassmorphism Premium

Las tarjetas actuales (Presencial y Online) son flat dark. Elevarlas con glassmorphism sutil dentro de un fondo oscuro con textura.

### Contenedor de la sección:
```css
/* Fondo con gradiente + noise para la sección de modalidades */
.programs-section {
  background: #0d0d0d;
  position: relative;
}
.programs-section::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 30% 50%, rgba(46,206,196,0.06) 0%, transparent 60%),
              radial-gradient(ellipse at 70% 50%, rgba(255,59,107,0.06) 0%, transparent 60%);
  pointer-events: none;
}
```

### Cards con glass effect:
```css
.school-dark-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 2px; /* mínimo, mantener austeridad */
  padding: 44px 40px 48px;
  transition: border-color 0.3s, transform 0.3s;
}
.school-dark-card:hover {
  border-color: rgba(255,255,255,0.15);
  transform: translateY(-4px);
}
.school-dark-card.coral:hover { border-color: rgba(255,59,107,0.3); }
.school-dark-card.teal:hover  { border-color: rgba(46,206,196,0.3); }
```

### Accent line top (detalle premium):
Añadir al inicio de cada card un borde superior de color de acento:
```html
<div class="school-dark-card coral" style="border-top: 2px solid #FF3B6B">
<div class="school-dark-card teal"  style="border-top: 2px solid #2ECEC4">
```

---

## 4. Stats Bar — Animación de Contadores

La barra de stats (`750+`, `3`, `50+`, `20+`) debe tener animación de conteo al hacer scroll. Verificar que este script esté presente al final del `<body>`:

```html
<script>
(function(){
  const counters = document.querySelectorAll('.counter');
  const observed = new Set();
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting || observed.has(e.target)) return;
      observed.add(e.target);
      const el = e.target;
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.dataset.suffix || '';
      const dur = 1400;
      const start = performance.now();
      function tick(now){
        const p = Math.min((now - start) / dur, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(eased * target) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.4 });
  counters.forEach(c => io.observe(c));
})();
</script>
```

Cada número en el HTML debe tener `class="counter" data-target="750" data-suffix="+"`.

---

## 5. Animaciones de Scroll (fade-up / scale-in)

El archivo `js/main.js` maneja las animaciones de entrada. Para que funcionen, cada sección principal necesita:

```html
<!-- Para secciones grandes: -->
<section class="scale-in" data-anim="scale">

<!-- Para elementos internos: -->
<div class="fade-up">
<div class="fade-up" style="transition-delay:0.1s">
<div class="fade-up" style="transition-delay:0.2s">
```

Añadir `divider-line` entre secciones para ritmo visual:
```html
<div class="divider-line" data-anim="line"></div>
```

---

## 6. CTA Final — Reforzar

El bloque de cierre debe sentirse como una conclusión definitiva. Checklist:

- [ ] Fondo oscuro (`#0a0604` o `#111`) — no crema
- [ ] Logo de la escuela centrado arriba
- [ ] Titular grande en Fraunces con acento coral
- [ ] Subtítulo claro: "All details, pricing and enrollment on the school's official website"
- [ ] Dos botones: primario coral ("Go to School Website ↗") + secundario teal ("Contact Us")
- [ ] Sin imágenes ni decoración extra — solo tipografía y CTA

---

## 7. i18n — Verificar en translations.js

Confirmar que estas keys existen en los 3 idiomas (EN / ES / FR) en `js/translations.js`:

```
clases.topbar, clases.topbarLink
clases.heroBadge, clases.heroTitle, clases.heroAccent, clases.heroSub
clases.heroCta1, clases.heroCta2
clases.stat1, clases.stat2, clases.stat3, clases.stat4
clases.introEyebrow, clases.introTitle, clases.introAccent, clases.introP
clases.exp1, clases.exp2, clases.exp3
clases.programsEyebrow, clases.programsTitle, clases.programsAccent
clases.modal1Type, clases.modal1Name, clases.modal1Desc
clases.modal1c1..c6
clases.modal2Type, clases.modal2Name, clases.modal2Desc
clases.modal2c1..c6
clases.ctaTag, clases.ctaTitle, clases.ctaSub
clases.ctaBtn1, clases.ctaBtn2, clases.ctaBtn3
clases.address
```

---

## 8. Lo que NO añadir

Según la estrategia de Bridge Page, **no agregar**:
- ❌ Horarios o calendario
- ❌ Perfiles de profesores
- ❌ Tabla de precios detallada
- ❌ Galería de fotos (más de 2-3 imágenes de alto impacto)
- ❌ Carruseles
- ❌ Formulario de contacto (redirigir a contacto.html)

---

## Orden de prioridad

1. 🔴 Tipografía (Fraunces + Jakarta Sans) — rompe la marca si está mal
2. 🔴 Glassmorphism en cards de programas — el cambio visual más impactante
3. 🟡 Hero Ken Burns + gradiente — mejora conversión del primer impacto
4. 🟡 Animaciones de scroll (fade-up, scale-in, divider-line)
5. 🟢 Contadores animados — detalle que refuerza credibilidad
6. 🟢 i18n check — evitar textos rotos en ES/FR

---

*Documento preparado para handoff a Claude Code.*
