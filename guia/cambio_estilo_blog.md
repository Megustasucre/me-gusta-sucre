# Instrucciones para el Rediseño Premium del Blog y Optimización de Color

Este documento contiene las instrucciones precisas para que otra IA implemente el nuevo diseño "Premium Editorial" y optimice el flujo visual de las secciones en `guia.html`.

## 1. Ajustes de Ritmo Visual (Colores de Fondo)

Para evitar la monotonía visual (el "Valle del Crema"), debemos aplicar ligeras variaciones de fondo en las últimas secciones:

1.  **Sección Food & Drink (`#food`):** Cambiar el fondo a Blanco Puro (`#ffffff`).
2.  **Sección Las Crónicas (`#cronicas`):** Cambiar el fondo a un Blanco Hueso Editorial (`#fdfcf9`).

---

## 2. Cambios en CSS (`css/style.css`)

**Instrucción:** Buscar y reemplazar los bloques correspondientes por estos nuevos estilos:

```css
/* ─── SECCIÓN FOOD (Optimización de Color) ─── */
.food-section {
  padding: 120px 0;
  background: #ffffff; /* Cambio a blanco para resaltar la gastronomía */
}

/* ═══════════════════════════════════════════════════════════
   LAS CRÓNICAS — Blog section in guia.html
═══════════════════════════════════════════════════════════ */
.blog-section { 
  padding: 120px 0; 
  background: #fdfcf9; /* Blanco hueso para estilo editorial */
}
.blog-inner { max-width: 1280px; margin: 0 auto; padding: 0 48px; }
.blog-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 80px; padding-bottom: 40px; border-bottom: 1px solid #e8dfd0; }
.blog-eyebrow { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: var(--red); margin-bottom: 12px; }
.blog-title { font-family: 'Fraunces', serif; font-size: clamp(2.8rem, 5vw, 4rem); font-weight: 800; color: #111; line-height: 1; }
.blog-title em { color: var(--red); font-style: italic; }
.blog-sub { font-size: 15px; color: #888; max-width: 320px; line-height: 1.8; padding-bottom: 6px; }

/* Editorial Grid */
.blog-grid-premium { display: grid; grid-template-columns: 1.2fr 1fr; gap: 80px; align-items: start; }

/* Article Featured */
.art-featured { text-decoration: none; color: inherit; display: block; position: relative; grid-column: span 1; }
.art-featured .art-img-wrap { position: relative; height: 560px; overflow: hidden; margin-bottom: 32px; clip-path: inset(0 0 0 0); transition: clip-path 0.8s cubic-bezier(0.165, 0.84, 0.44, 1); }
.art-featured .art-img-wrap img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s ease; }
.art-featured:hover .art-img-wrap { clip-path: inset(20px 20px 20px 20px); }
.art-featured:hover .art-img-wrap img { transform: scale(1.1); }

.art-tag { display: inline-block; font-size: 9px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--red); margin-bottom: 16px; background: rgba(201, 37, 45, 0.06); padding: 4px 12px; transition: all 0.3s; }
.art-featured:hover .art-tag, .art-minimal:hover .art-tag { background: var(--red); color: #fff; }

.art-title-lg { font-family: 'Fraunces', serif; font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 800; color: #111; line-height: 1.1; margin-bottom: 20px; transition: color 0.3s; }
.art-featured:hover .art-title-lg { color: var(--red); }

.art-excerpt { font-size: 15px; color: #555; line-height: 1.8; margin-bottom: 24px; max-width: 90%; }
.art-meta { font-size: 10px; font-weight: 700; color: #999; letter-spacing: 1px; text-transform: uppercase; display: flex; align-items: center; gap: 12px; }
.art-meta::before { content: ''; width: 30px; height: 1px; background: #e8dfd0; }

/* Side List Minimal */
.art-side-list { display: flex; flex-direction: column; gap: 48px; }
.art-minimal { display: grid; grid-template-columns: 160px 1fr; gap: 28px; text-decoration: none; color: inherit; padding-bottom: 48px; border-bottom: 1px solid #e8dfd0; transition: transform 0.3s ease; }
.art-minimal:last-child { border-bottom: none; }
.art-minimal:hover { transform: translateX(10px); }

.art-minimal-img { height: 160px; overflow: hidden; }
.art-minimal-img img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }
.art-minimal:hover .art-minimal-img img { transform: scale(1.1); }

.art-minimal-body { display: flex; flex-direction: column; justify-content: center; }
.art-minimal-title { font-family: 'Fraunces', serif; font-size: 1.3rem; font-weight: 800; color: #111; line-height: 1.2; margin-bottom: 12px; transition: color 0.3s; }
.art-minimal:hover .art-minimal-title { color: var(--red); }
.art-minimal-excerpt { font-size: 13.5px; color: #666; line-height: 1.6; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

@media (max-width: 1100px) {
  .blog-grid-premium { grid-template-columns: 1fr; gap: 60px; }
  .art-featured .art-img-wrap { height: 440px; }
  .blog-inner { padding: 0 24px; }
}

@media (max-width: 640px) {
  .art-minimal { grid-template-columns: 1fr; gap: 20px; }
  .art-minimal-img { height: 200px; }
  .art-featured .art-img-wrap { height: 320px; }
  .art-title-lg { font-size: 1.6rem; }
}
```

## 3. Cambios en HTML (`guia.html`)

**Instrucción:** Reemplazar el bloque `<div class="article-list">...</div>` (aproximadamente líneas 930-1002) por la estructura de **Grid Editorial** detallada en la versión anterior del plan, asegurando que se integre dentro de la sección `#cronicas`.

---

## Resumen de Impacto UX/UI
Esta actualización no solo mejora la estética de la lista de blogs, sino que utiliza el color para guiar al usuario a través de diferentes "temas" (Naturaleza -> Gastronomía -> Historias), eliminando la monotonía visual y aumentando el tiempo de permanencia en la página.
