# REDISEÑO TOTAL: City Guide (guia.html) — "The Master Magazine"
*Arquitectura UX/UI Antigravity · Versión REINICIO · 25 Abril 2026*

---

## 1. El Concepto
Transformar `guia.html` de un listado visual a una **Revista de Viajes de Lujo**. El objetivo no es solo informar, sino establecer a "Me Gusta Sucre" como la autoridad absoluta. No es una guía turística; es una carta de amor a la ciudad.

---

## 2. Nueva Estructura de la Página

### Bloque 1: El Impacto (Atmospheric Hero)
- **Altura**: `100vh` (Pantalla completa).
- **Diseño**: Imagen cinemática (slow zoom / Ken Burns effect) con gradiente oscuro profundo.
- **Copy**: "SUCRE: LA GUÍA DEFINITIVA" (Fraunces Serif, Bold).
- **Sub-copy**: "Una carta de amor a la Ciudad Blanca, escrita por quienes la habitan."

### Bloque 2: El Manifiesto (Founder's Letter)
- **Diseño**: Fondo crema (`#fdf6ec`), tipografía serif elegante.
- **Contenido**: Texto en primera persona ("Vivir en Sucre desde 2011...") con una firma manuscrita (`Sacramento` font). 
- **Objetivo**: Humanizar la marca y generar confianza inmediata.

### Bloque 3: Los Capítulos (Navegación Visual)
- **Diseño**: 4 Cards grandes que sirven como índice visual.
- **Categorías**: 
    1. **El Alma** (Lo que hay que ver)
    2. **La Cocina** (Qué comer y Café)
    3. **Las Crónicas** (Artículos de blog)
    4. **El Manual** (Información útil/logística)

### Bloque 4: Capítulo 1 — El Alma de Sucre (The Sights)
- **Bento Grid Editorial**: Cards asimétricas para romper la monotonía.
- **Capa Narrativa**: Cada card tiene un título y un párrafo corto (3-4 líneas) con voz de blog.
- **Interacción**: Al hacer clic, abre un **Editorial Modal** (Magazine style) con la historia completa y mapa.

### Bloque 5: Capítulo 2 — Cocina de Altura (Eats)
- **Diseño**: Fondo Blanco. Listado tipo menú de alta gama.
- **Highlight**: Sección especial para **Me Gusta Café** con el badge flotante.
- **Contenido**: Platos típicos + El "Aji Note" (ingrediente secreto).

### Bloque 6: El Manual del Viajero (Información Útil)
- **Diseño**: Fondo Oscuro (`#111`). Estilo "Notebook/Field Notes".
- **Cards Minimalistas**: Altitud, Moneda, Transporte, Clima.
- **Pro Tip**: Bloque destacado "Cash is King".

### Bloque 7: Las Crónicas (El Blog de Sucre)
- **Diseño**: 4 Cards verticales elegantes con títulos sugerentes.
- **Temas**: 
    1. **Sucre After Dark**: La vida nocturna y cultural.
    2. **Pequeños Viajeros**: Guía para familias (parques, dinosaurios).
    3. **Tradiciones de Domingo**: Mercados y cultura viva.
    4. **Insider Tips**: Consejos de supervivencia local y secretos.
- **UX**: Cada card abre un modal editorial con el artículo completo.

### Bloque 8: El Cierre (Stay & Learn)
- **Conversión Final**: Presentación del Inn y la Escuela como las "Puertas de Entrada" a todo lo leído arriba.

---

## 3. Especificaciones Técnicas UX/UI (Wanderlush System)

- **Tipografía**: Títulos en `Fraunces` (Serif). Cuerpo en `Plus Jakarta Sans`. Acentos en `Sacramento` (Cursive).
- **Filtros**: **Floating Glassmorphism Bar** (Fondo blanco 85% opacidad + blur) que aparece al entrar en la sección de sitios.
- **Modales**: Sistema de modales fluido con imagen full-width, tipografía editorial y botón de Google Maps.
- **Sticky Nav**: Menú de sub-secciones que cambia según el scroll.
- **Cross-selling**: Enlaces contextuales (inline links) dentro de los párrafos del blog (ej: links a `clases.html`).

---
*Documento generado por Antigravity UX/UI Architect. Listo para ejecución.*
