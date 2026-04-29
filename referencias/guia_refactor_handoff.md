# Hand-off para Claude: Refactorización de guia.html

**Contexto del Proyecto:**
Estás trabajando en el sitio "Me Gusta Sucre" (un proyecto de turismo premium, escuela de español y hostal/café). El diseño actual sigue una estética editorial, tipo revista "Wanderlush" (tipografías Fraunces y Plus Jakarta Sans, colores oscuros contrastados con beige #fdf6ec, animaciones fluidas).

**Archivos Objetivo:**
1. `guia.html`
2. `css/style.css`
3. `js/translations.js`
4. Nuevo archivo: `blog-post.html`

## Tareas a Ejecutar

Debes realizar los siguientes cambios técnicos y estructurales respetando rigurosamente el diseño premium actual:

### 1. Limpieza de CSS (guia.html y style.css)
- **Problema:** `guia.html` está saturado de estilos en línea (ej. `<section style="padding:100px 0;background:#fff">`).
- **Acción:** Extrae todos estos estilos en línea (backgrounds, paddings, flexbox) y conviértelos en clases semánticas dentro de `css/style.css` (o utiliza las clases utilitarias de Tailwind si ya están disponibles en el proyecto). No rompas el diseño responsivo ni las animaciones.

### 2. Páginas de Blog Reales (Las Crónicas)
- **Problema:** Actualmente, los 5 artículos del blog ("Las Crónicas" al final de `guia.html`) abren en ventanas modales generadas por JS.
- **Acción en guia.html:** Elimina la clase `modal-card` y los atributos `data-modal-*` de estos 5 elementos. Envuélvelos en etiquetas `<a>` normales para que redirijan a páginas individuales (ej. `href="blog-post.html"`).
- **Acción Nuevo Archivo:** Crea **SOLO UN archivo** de blog (`blog-post.html`) que sirva como prototipo para el primer artículo ("Todo lo que necesitas saber antes de llegar"). El objetivo es que definamos y aprobemos primero el diseño de esta única página antes de crear las demás. Debe ser una plantilla funcional que mantenga el estilo visual de la web (Nav transparente, Hero con el título de la crónica, cuerpo de texto formateado para lectura, fecha de publicación, autor y Footer).

### 3. Arreglo Responsivo del Carrusel
- **Problema:** En el script al final de `guia.html`, el contador del carrusel se calcula de forma estática: `Math.round(spotsTrack.scrollLeft / 384) + 1;` Esto se rompe en versión móvil porque las tarjetas usan `82vw`.
- **Acción:** Modifica la lógica JS para que calcule el índice dinámicamente usando el ancho real de la tarjeta (`.clientWidth`).

### 4. Soporte Multi-idioma (i18n) para los Modales
- **Problema:** En la sección "Must-See Spots", los modales leen el texto desde atributos hardcodeados (`data-modal-tag`, `data-modal-desc`). Esto rompe el sistema de traducciones si el usuario cambia el idioma a Francés o Español.
- **Acción:** Cambia la lógica para usar claves de traducción (ej. `data-i18n-modal-desc="guia.must1ModalDesc"`). Actualiza el JS para que lea desde el sistema de traducciones activo. Añade estas nuevas claves en `js/translations.js`.

### 5. Añadir "Puente Sucre" y Placeholders
- **Day Trips:** Añade una nueva tarjeta (la 5ta) en la sección "Day Trips" para **"Puente Sucre"**. Mantén la estructura del carrusel deslizable.
- **Imágenes:** Reemplaza todos los enlaces de imágenes de `unsplash.com` en las tarjetas por rutas locales de placeholder (ej. `imagenes/placeholder.webp`) para indicar dónde el cliente deberá colocar sus fotos reales locales.

## Reglas Estrictas
- **NO** modifiques la voz y el tono de los textos (están escritos por locales, "100% sucrenses").
- **NO** alteres la navegación (Navbar) ni el pie de página (Footer) en el HTML existente, a menos que sea para limpiar estilos en línea.
- Garantiza que cualquier clase nueva añadida a `style.css` mantenga la filosofía de diseño actual (Wanderlush/Premium).
