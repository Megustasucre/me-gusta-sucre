# Observaciones Técnicas y de Diseño — index.html

Este documento detalla los hallazgos tras el análisis del `index.html` frente al sistema de diseño premium definido.

## 1. Tipografía y Estilo (Crítico)
*   **Hallazgo:** El HTML seguía referenciando y aplicando fuentes antiguas (`Lora`, `DM Sans`, `Satisfy`) mediante etiquetas `<link>` y estilos `inline`.
*   **Corrección necesaria:** Eliminar referencias antiguas y aplicar las clases `.serif` (Fraunces), `.handwritten` (Sacramento) y el estilo base de `Plus Jakarta Sans` definido en `style.css`.
*   **Limpieza de CSS:** Reemplazar colores hexadecimales hardcodeados (ej. `#c9252d`) por variables globales como `var(--red)`.
*   **Estado:** COMPLETADO — `Lora` → `Fraunces`, `DM Sans` → `Plus Jakarta Sans` en todos los inline styles. `<link>` de Google Fonts actualizado. `#c9252d` → `var(--red)`, `#111111` → `var(--text)`, `#555555` → `var(--muted)`.

## 2. Estructura y Narrativa (Flujo del Viajero)
*   **Hallazgo:** La sección "INN SECTION" duplicaba la información que aparece inmediatamente después en "ME GUSTA BRANDS".
*   **Corrección necesaria:** Eliminar la sección redundante y priorizar el grid de la "Me Gusta Collection" para presentar las 4 verticales (Inn, Café, Clases, Merch) como un ecosistema único.
*   **Orden de secciones:** Mover los testimonios (Reviews) a una posición superior para fortalecer la confianza del usuario antes de llegar al final de la página.
*   **Estado:** COMPLETADO — Inn Section eliminada. Reviews movidas arriba (del ~85% al ~60% del scroll). Nuevo orden: Hero → Ticker → Trust Bar → Brand Cards → Atracciones → Reviews → CTA Final.

## 3. Optimización de Conversión (UX/UI)
*   **Hallazgo:** Los CTAs del Hero tenían el mismo peso visual, diluyendo la acción principal.
*   **Corrección necesaria:** Aplicar jerarquía visual.
    *   **Primario:** `btn-red` para "Book a Stay".
    *   **Secundario:** `btn-outline` para "City Guide".
*   **Estado:** COMPLETADO — jerarquía implementada. Hero H1 cambiado a "Your Base in Sucre".

## 4. Deuda Técnica
*   **Inline Styles:** Gran cantidad de bloques `style="..."` que dificultan el mantenimiento y rompen la consistencia con el `style.css`.
*   **Meta:** Migrar estilos específicos a clases en `style.css` o usar utilidades de Tailwind/Custom CSS preexistentes.
*   **Estado:** PENDIENTE — los colores críticos ya usan variables CSS. Quedan bloques `style="..."` estructurales (hero, cards, footer) que requieren refactor a clases en `style.css`.

## 5. Mejora de Narrativa (Anfitrión Experto)
*   **Hallazgo:** Los textos actuales son informativos pero planos. No proyectan la autoridad de un "Anfitrión Experto" de la ciudad.
*   **Corrección necesaria:** Elevar el copywriting para que suene más humano y experto. El contenido debe vender la "experiencia de vivir Sucre", no solo los servicios por separado.
*   **Estado:** PENDIENTE.

## 6. Social Proof Humano y Dinámico
*   **Hallazgo:** Las reseñas son textuales (Google Maps). Falta el componente visual humano que genere conexión inmediata.
*   **Corrección necesaria:** Integrar imágenes de personas reales disfrutando de los servicios (Café, Hostal, Escuela) junto a los testimonios.
*   **Estado:** PENDIENTE.

## 7. Estética Editorial "Luxury Travel"
*   **Hallazgo:** El diseño es funcional pero puede sentirse "apretado" en ciertas secciones del Index.
*   **Corrección necesaria:** Aumentar el uso de espacios en blanco (white space), mejorar las transiciones entre secciones y usar fotografías de gran formato para un look de revista de viajes premium.
*   **Estado:** PENDIENTE.

---

*Análisis realizado por Antigravity — 24 de Abril, 2026.*
*Actualizado — 24 de Abril, 2026.*
