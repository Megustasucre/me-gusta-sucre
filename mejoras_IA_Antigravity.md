# 🚀 Mejoras IA Antigravity — Me Gusta Sucre

Este documento resume la auditoría de diseño, UX/UI y estrategia realizada por la IA Antigravity. Sirve como hoja de ruta para la sesión de mañana.

---

## 🧐 Estado Actual (Hallazgos Clave)

### 1. Inconsistencia Tipográfica (Crítico)
*   **Diseño Teórico:** El `style.css` define `Fraunces` y `Plus Jakarta Sans`.
*   **Realidad:** Todos los HTML usan `Lora` y `DM Sans` mediante estilos inline.
*   **Meta:** Unificar a la tipografía premium (`Fraunces` / `Jakarta`) para elevar el valor percibido.

### 2. Deuda Técnica de Diseño
*   **Estilos Fragmentados:** Exceso de estilos inline y bloques `<style>` dentro de los HTML.
*   **Variable Drift:** Colores y espaciados hardcodeados que no siguen las variables de `:root`.
*   **Meta:** Migrar estilos a `style.css` y usar variables `var(--red)`, `var(--cream)`, etc.

### 3. Experiencia de Usuario (UX)
*   **Jerarquía de CTAs:** El Hero del Index tiene botones con pesos visuales idénticos.
*   **Flujo del Viajero:** Falta una narrativa clara que conecte la Guía (Atracción) con los servicios (Conversión).

---

## 🎨 Visión Estratégica
*   **Sentido:** Ser el "Anfitrión Experto" de Sucre.
*   **Objetivo:** Convertir curiosidad turística en reservas directas mediante una estética editorial de confianza (Wanderlush).

## 📐 Estructura del Sitio (Estrategia)

Para resolver la identidad dividida, el sitio se organizará en tres niveles:
1.  **El Portal (Index):** Puerta de entrada a la experiencia completa.
2.  **La Autoridad (Guía):** Contenido de valor que genera confianza y tráfico.
3.  **La Conversión (Colección):** Los 4 servicios directos (Inn, Escuela, Café, Merch).

---

## 📖 Narrativa del Index (Flujo del Viajero)

El nuevo orden del `index.html` seguirá este flujo lógico para maximizar la conversión:
1.  **Hero "Anfitrión Experto":** Posicionamiento de marca + CTAs jerarquizados (Primario: Reservar / Secundario: Explorar).
2.  **Trust Bar:** 4.9★ Google, UNESCO Heritage, +20 años de experiencia.
3.  **The Me Gusta Collection:** Presentación de los 4 pilares como un ecosistema premium único.
4.  **City Teaser:** 3 lugares imperdibles de Sucre (conecta con la Guía).
5.  **Testimonios:** Voces reales de viajeros (Social Proof).
6.  **CTA Final Humano:** Contacto directo por WhatsApp para soporte personal.

---

## 📅 Roadmap para Mañana

### Fase 1: Unificación Visual
- [ ] **Migración Global de Fuentes:** Cambiar `Lora/DM Sans` por `Fraunces/Plus Jakarta Sans` en todas las páginas.
- [ ] **Limpieza de Colores:** Reemplazar colores hex hardcodeados por variables CSS.
- [ ] **Estandarización de Botones:** Asegurar que `.btn-red` y `.btn-gold` se vean idénticos en todo el sitio.

### Fase 2: Optimización de Estructura y Narrativa
- [ ] **Re-arquitectura del Index:** Reordenar las secciones según el "Flujo del Viajero".
- [ ] **Refactor de CTAs:** Implementar la jerarquía de botones Primario/Secundario en el Hero.
- [ ] **Brand Identity Check:** Reforzar los colores de identidad en cada página vertical.

### Fase 3: Pulido Editorial y Componentización
- [ ] **Refactor de Bento Grids:** Optimización responsiva en Guía y Merch.
- [ ] **Sección de Cierre:** Implementar el nuevo bloque de "Anfitrión" en el footer de todas las páginas.

---

**Preparado para ejecutar mañana.** 
*Documento actualizado por Antigravity — 23 de Abril, 2026.*
