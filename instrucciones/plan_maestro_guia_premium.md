# Plan Maestro: Rediseño Total Guía de Sucre (guia.html)
### Versión Consolidada · "The Master Magazine" · Abril 2026

Este documento unifica todas las auditorías y handoffs previos en una única fuente de verdad para transformar la página de guía en una **revista editorial de lujo**.

---

## 1. Sistema de Diseño (Wanderlush)

### Paleta de Colores y Flujo de Secciones
Eliminar fondos intermedios (`#f4f4f4`, `#fafafa`) y ceñirse a este ritmo visual para evitar el "Valle del Crema":

1.  **Hero:** Imagen Full-Bleed (Cinemática)
2.  **Manifiesto:** Crema (`#fdf6ec`)
3.  **Capítulos:** Oscuro (`#111111`)
4.  **About the City:** Blanco (`#ffffff`)
5.  **Quick Facts Bar:** Oscuro (`#111111`) — *Movido después de About*
6.  **Social Proof:** Crema (`#fdf6ec`)
7.  **Must-See Spots:** Blanco (`#ffffff`)
8.  **Day Trips:** Crema (`#fdf6ec`)
9.  **Food & Drink:** Blanco (`#ffffff`) — *Ajuste UX para diferenciación*
10. **Las Crónicas:** Blanco Hueso (`#fdfcf9`) — *Look Editorial*
11. **Closing CTA:** Oscuro (`#111111`)

### Reglas Globales
- **Border-radius:** 0px (Esquinas rectas) en todos los contenedores principales (Cards, imágenes, secciones).
- **Tipografía:** Títulos en `Fraunces` (Serif). Cuerpo en `Plus Jakarta Sans`. Acentos en `Sacramento` (Cursive).

---

## 2. Bloques de Implementación

### BLOQUE 1: Atmospheric Hero (REDISEÑO)
- **Altura:** `100vh`.
- **Efecto:** Ken Burns (zoom suave) habilitado.
- **Titular:** "SUCRE: LA GUÍA DEFINITIVA" (`font-size: clamp(2.8rem, 5.5vw, 4.8rem)`).
- **Sub-copy:** "Una carta de amor a la Ciudad Blanca, escrita por quienes la habitan."

### BLOQUE 2: Manifiesto y Capítulos
- **Manifiesto:** Fondo crema. Firma manuscrita al final con la fuente `Sacramento`.
- **Capítulos:** Fondo oscuro. 4 Cards de índice visual que conectan con las secciones principales.

### BLOQUE 3: Food & Drink (Premium Layout)
- **Diseño:** Grid asimétrico. Imagen "sticky" a la izquierda que se mantiene mientras el texto de los platos desliza a la derecha.
- **Detalle:** Incluir el bloque "Aji Note" con un diseño minimalista integrado.

### BLOQUE 4: Las Crónicas (Editorial Grid)
- **Estructura:** Grid asimétrico (Asymmetrical Grid).
- **Featured Post:** El primer artículo ocupa el 60% del ancho con imagen grande y efecto de máscara (`clip-path`) al hacer hover.
- **Side List:** Los otros 3 artículos en una lista minimalista a la derecha.

### BLOQUE 5: Closing CTA (Cross-selling)
- **Diseño:** Grid 2/3 (Escuela) y 1/3 (Hostal + Café).
- **Escuela:** Fondo con imagen y overlay oscuro. Botón color Coral.
- **Hostal:** Fondo azul pizarra profundo con efecto de "ruido" sutil.
- **Café:** Barra inferior con indicador "Open Now" parpadeante (dot verde).

---

## 3. Micro-interacciones y Pulido
- **Contadores de Carrusel:** Añadir `1 / 9` en los spots y `1 / 4` en day trips.
- **Botón Modal:** Reemplazar la "X" de texto por un icono SVG elegante.
- **Logos:** Usar `logo-me-gusta-sucre-chinchilla.png` como fallback si los logos específicos de las marcas no están disponibles.

---

## 4. Orden de Ejecución Recomendado
1.  **Ajuste de Hero (100vh + Copy)**
2.  **Unificación de fondos y eliminación de border-radius**
3.  **Implementación del Grid Editorial en Las Crónicas**
4.  **Re-maquetación de la sección Food & Drink**
5.  **Implementación del nuevo Closing CTA**
6.  **Pulido de micro-interacciones (contadores, modales, SVGs)**

---
*Plan Maestro Consolidado · Antigravity UX/UI Architect · Me Gusta Sucre 2026*
