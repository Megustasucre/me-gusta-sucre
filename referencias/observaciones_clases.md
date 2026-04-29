# Observaciones Técnicas y de Diseño — clases.html

Este documento detalla los hallazgos y la hoja de ruta para elevar la página de la Escuela de Español al estándar "Wanderlush".

## 1. Tipografía y Cohesión de Marca (Urgente)
*   **Hallazgo:** El archivo utiliza fuentes obsoletas (`Lora`, `DM Sans`) que rompen la unidad visual con el nuevo Index.
*   **Corrección:** Migrar a `Fraunces` (Serif Display) para títulos y `Plus Jakarta Sans` para el cuerpo.
*   **Identidad:** Mantener el Coral (`#FF3B6B`) y el Teal (`#2ECEC4`) como acentos, pero aplicados mediante variables o clases consistentes.

## 2. Estrategia de Conversión (Página de Transición / Bridge Page)
*   **Hallazgo:** Tienes toda la razón. Siendo esta una página de "puente" hacia `megustaspanish.com`, no debemos sobrecargarla con detalles (como horarios o perfiles de profesores).
*   **Mejora Estratégica:**
    *   **Foco en el "Teaser":** Vender el *por qué* (la experiencia, la inmersión, el prestigio) y dejar el *cómo* (precios, horarios exactos) para la web de la escuela.
    *   **CTAs más Agresivos:** Los botones que dirigen a la web de la escuela deben ser los elementos con mayor peso visual en la página, usando el color Coral (`#FF3B6B`) de forma estratégica.
    *   **Prueba Social Rápida:** Mantener el enfoque en números (750+ estudiantes) y reconocimientos (Actividad #1) para generar confianza inmediata y provocar el clic hacia la web oficial.

## 3. Interfaz y Estética Premium (UI/UX)
*   **Hero Cinematográfico:** Aumentar el impacto del Hero para que sea tan envolvente como el del Index.
*   **Cards de Programas:** Aplicar efectos de Glassmorphism o sombras suaves para que los cursos (Privado, Grupo, Online) se sientan como productos premium.
*   **Contadores Dinámicos:** Implementar la animación de conteo en la barra de estadísticas (750+ estudiantes, 20+ años).

## 4. Deuda Técnica
*   **Bloque <style> interno:** Mover los estilos específicos de la escuela a `style.css` para evitar duplicidad.
*   **Inline Styles:** Limpiar los atributos `style="..."` en el HTML para facilitar el mantenimiento.
*   **i18n:** Verificar que los nuevos textos de la narrativa "Anfitrión Experto" estén sincronizados en `translations.js`.

## 5. Plan de Rediseño Estructural Definitivo (Minimalista y Visual)
Tras revisar el exceso de imágenes (sobrecarga visual), se ha acordado implementar una estructura de embudo (funnel) minimalista "Desde Cero" para la página de clases (`clases.html`), maximizando la conversión hacia la web oficial.

### Estructura Aprobada:
1. **El Gancho (Hero Section):** 1 sola foto de fondo estelar, título "Aprende Español en Sucre" y CTA directo.
2. **Autoridad (Stats Bar):** Barra tipográfica pura y limpia (750+ Alumnos). Cero imágenes.
3. **El Valor (Composición Split Elegante):**
   * **Izquierda (Texto):** Títulos grandes en fuente `Fraunces` y 3 viñetas breves sobre por qué elegir la escuela (Acento Neutro, Inmersión).
   * **Derecha (Visual):** Composición premium de dos fotos superpuestas tipo editorial para satisfacer la necesidad de mostrar cómo es la escuela, sin usar carruseles obsoletos ni distraer al usuario.
4. **Modalidades (Tarjetas Dark Premium):** Tarjetas elegantes oscuras (`#111`) para Clases Presenciales y Online. Sin imágenes de fondo, puro contraste y tipografía sofisticada.
5. **Cierre (CTA Final):** Bloque oscuro minimalista. "Visita la web oficial para precios y cursos". Sin la antigua galería grid de 4 fotos.

**Resultado:** La página pasará de ~10 imágenes a **solo 2-3 áreas visuales de altísimo impacto**, guiando el ojo del usuario directamente a los botones de reserva.

---
*Análisis actualizado por Antigravity — 24 de Abril, 2026.*
