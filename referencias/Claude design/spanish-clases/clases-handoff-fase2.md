# Handoff para Claude Code — clases.html (Fase 2: UX/UI Premium)
*Basado en observaciones expertas de UX/UI Antigravity*

---

## Contexto

Esta es la segunda fase de optimización para la Bridge Page `clases.html`. El objetivo es elevar el refinamiento visual (animaciones, contraste) y simplificar la carga cognitiva en la sección de cursos para maximizar la conversión hacia `megustaspanish.com`.

**NOTA IMPORTANTE:**
- **Eliminar** el Top Bar (`<div class="top-bar">...</div>`) para mantener la limpieza visual y priorizar la conversión.
- **No** modificar el Navbar global (mantener todos los links actuales, no ocultar nada).

---

## 1. Mejora de Contraste en Secciones

La sección "More than classes" (la que contiene el texto de Audiencia #97 y las fotos editoriales) actualmente tiene un fondo `#fafafa`. Para darle un aspecto más cálido y premium alineado con la marca:

- **Fondo:** Cambiar el fondo de esa `<section>` a `var(--cream)` (o directamente `#fdf6ec` si no funciona la variable inline).
- Asegurar que los textos oscuros (`#111` y `#666`) mantengan una excelente legibilidad sobre este nuevo fondo crema.

---

## 2. Animaciones Premium en Imágenes ("More than classes")

El bloque de imágenes `.school-editorial` es muy estático. Necesita más dinamismo y lujo visual.
Añadir las siguientes reglas CSS (preferiblemente en `css/style.css` o en el bloque `<style>` de la página) y aplicarlas al bloque:

### A. Animación de Entrada (Clip-Path Reveal)
Hacer que la imagen principal se revele elegantemente desde abajo hacia arriba al hacer scroll.
```css
@keyframes revealUp {
  0%   { clip-path: polygon(0 100%, 100% 100%, 100% 100%, 0 100%); transform: translateY(20px); }
  100% { clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); transform: translateY(0); }
}
.school-editorial .photo-main {
  /* Mantener el rotate(2deg) y estilos actuales, agregar: */
  animation: revealUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}
.fade-up.visible .school-editorial .photo-main {
  opacity: 1;
}
```

### B. Animación de Flotación (Floating)
La foto secundaria (`.photo-accent`) debe flotar suavemente de manera continua.
```css
@keyframes floatGentle {
  0%, 100% { transform: translateY(0) rotate(-2deg); }
  50%      { transform: translateY(-12px) rotate(-2deg); }
}
.school-editorial .photo-accent {
  /* Mantener el rotate(-2deg) y border #2ECEC4, agregar: */
  animation: floatGentle 6s ease-in-out infinite;
}
```

### C. Sombras de Acento (Teñidas)
Reemplazar los `box-shadow` genéricos en `style.css` por sombras que usen los colores de la marca para dar un efecto de "glow":
- En `.photo-main`: `box-shadow: 0 20px 60px rgba(10, 6, 2, 0.15);`
- En `.photo-accent`: `box-shadow: 0 15px 45px rgba(46, 206, 196, 0.25);`

---

## 3. Simplificación y Minimalismo en Tarjetas de Programas

Para reducir la carga cognitiva (menos texto para leer = más rápida la decisión de click), simplificaremos las tarjetas de Presencial y Online (`.school-dark-card`).

- **Borrar Subprogramas:** Eliminar todos los divs con la clase `.card-feature` (Private, Couples, Group, etc.) dentro de ambas tarjetas.
- **Centrado y Párrafo:** Aumentar el tamaño de fuente del párrafo descriptivo (`<p data-i18n="clases.modal1Desc">`) a `font-size: 15px;` y aplicar un text-align center si es necesario para equilibrar el diseño.
- **Botones Full-Width:** Modificar los enlaces `.school-btn-coral` y `.school-btn-teal` dentro de estas tarjetas específicas para que abarquen el 100% del ancho. Puedes usar estilos inline o agregar una nueva clase utilitaria:
```css
width: 100%;
text-align: center;
display: block;
```
*Al hacer los botones 100% anchos, se llenará el espacio vacío dejado por la eliminación de los subprogramas y ofrecerá un "tap target" masivo para usuarios en dispositivos móviles.*

---
*Fin del documento de Handoff.*
