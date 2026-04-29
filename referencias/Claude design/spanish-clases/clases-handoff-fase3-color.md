# Handoff para Claude Code — clases.html (Fase 3: Ritmo de Color)
*Diagnóstico y especificaciones de Antigravity UX/UI · 25 Abril 2026*

---

## Diagnóstico del Problema

El flujo de secciones actual tiene demasiados bloques oscuros consecutivos que crean fatiga visual y una lectura monótona. El ritmo actual es:

| Sección | Fondo actual | Problema |
|---|---|---|
| Hero | Imagen + overlay negro | ✅ Correcto — arranque cinematográfico |
| Stats Bar | `#111111` | ⚠️ Negro puro |
| "More than classes" | `#fdf6ec` (crema) | ✅ Correcto — respiro visual |
| Programas (Presencial/Online) | `#0d0d0d` | ⚠️ Negro puro |
| CTA Final | `#0a0604` | ❌ Negro casi idéntico al anterior — sin separación visual |
| Footer | `#111111` | ⚠️ Negro puro — bloque de cierre aceptable |

**Problema central:** Stats Bar (`#111`) + Programas (`#0d0d0d`) + CTA (`#0a0604`) + Footer (`#111`) son 4 bloques oscuros casi idénticos consecutivos. El usuario percibe la página como una masa negra sin ritmo.

---

## Principio de Diseño Aplicado

Una Bridge Page premium de alta conversión debe tener un **ritmo alternado de luz y oscuridad**, donde cada sección oscura tiene una personalidad cromática propia (no todos el mismo negro), y el CTA final debe sentirse como un momento de "aterrizaje" diferente a las secciones previas.

**Ritmo objetivo:**
```
Hero (cinematográfico negro) →
Stats Bar (carbon profundo) →
"More than classes" (crema clara) ← RESPIRO ✅
Programas (teal oscuro, con personalidad) →
CTA Final (crema oscura cálida) ← DIFERENCIADO
Footer (neutral oscuro) →
```

---

## Instrucciones de Cambio

### Archivo: `clases.html`

---

#### 1. Stats Bar — De negro plano a carbon con personalidad

**Busca** (línea ~149):
```html
<div class="scale-in" data-anim="scale" style="background:#111111;padding:52px 0">
```

**Reemplaza con:**
```html
<div class="scale-in" data-anim="scale" style="background:#1a120a;padding:52px 0">
```

> **Por qué:** `#1a120a` es el `--dark` del sistema de diseño del sitio. Es un marrón oscuro cálido que conecta emocionalmente con la marca, versus el frío `#111111` que no tiene identidad. Este cambio es sutil pero perceptible — las cifras en Coral y Teal van a "pop" mucho más sobre este fondo.

---

#### 2. Sección de Programas — De negro a teal muy oscuro

**Busca en `css/style.css`** la regla `.programs-section` (aproximadamente línea 803):
```css
.programs-section {
  background: #0d0d0d;
  position: relative;
}
```

**Reemplaza con:**
```css
.programs-section {
  background: #061a18;
  position: relative;
}
```

> **Por qué:** `#061a18` es un teal/verde muy oscuro casi negro. Diferencia visualmente esta sección de los bloques negros puros sin romper la estética premium. Conecta emocionalmente con el color Teal (`#2ECEC4`) de la marca de la escuela. Los degradados radiales que ya existen en `.programs-section::before` se van a intensificar naturalmente sobre este fondo.

---

#### 3. CTA Final — De negro cálido a crema oscura de marca

**Busca** (línea ~283):
```html
<section class="scale-in" data-anim="scale" style="background:#0a0604;padding:100px 24px">
```

**Reemplaza con:**
```html
<section class="scale-in" data-anim="scale" style="background:var(--cream2);padding:100px 24px">
```

Adicionalmente, dentro de este mismo bloque CTA, deberás actualizar los colores de los textos para que sean legibles sobre fondo claro:

- El `<h2>` con `color:#fff` → cambiar a `color:#111`
- El `<p>` con `color:rgba(255,255,255,0.5)` → cambiar a `color:#666`
- El `<span class="handwritten">` con `color:#2ECEC4` → mantener (funciona bien en ambos fondos)
- El logo: quitar `opacity:0.9` → añadir `filter:none` (en fondo claro no necesita opacidad)

> **Por qué:** El CTA final es el momento de conversión. Pasar a un fondo crema (`#f7f0e4`) después de la oscuridad de la sección de programas crea un **contraste dramático** que llama la atención de manera natural. El usuario inconscientemente siente que llegó a "otro lugar" — y eso es exactamente lo que queremos en el momento de la llamada a la acción. Los botones Coral y Teal resaltan aún más sobre fondos claros.

---

## Resultado Visual Esperado

```
Hero          → negro cinematográfico con imagen
Stats Bar     → marrón oscuro cálido (#1a120a)  ← identidad de marca
─── divider ───
"More than classes" → crema #fdf6ec             ← RESPIRO CLARO
─── divider ───
Programas     → teal muy oscuro (#061a18)        ← oscuro con personalidad
─── divider ───
CTA Final     → crema cálida #f7f0e4             ← ATERRIZAJE CLARO = conversión
Footer        → #111111                          ← cierre estándar
```

Este ritmo crea **2 momentos de luz** (More than classes + CTA Final) que actúan como anclas visuales y rompen la fatiga de los bloques oscuros.

---

*Documento generado por Antigravity UX/UI Architect. Listo para ejecución en Claude Code.*
