# Brand Cards Redesign — "While You're Here" Section

## Qué cambiar en `index.html`

Reemplaza la sección `<!-- ═══ MIENTRAS ESTÁS AQUÍ -->` completa con el nuevo diseño de tarjetas editoriales. Los cambios principales son:

### 1. Estructura de la sección

- **Fondo**: cambia de `background:#f4f4f4` a `background:#111` (oscuro)
- **Header**: de centrado a dos columnas (título izquierda, descripción derecha)
- **Grid**: de `md:grid-cols-2 lg:grid-cols-3` a siempre 3 columnas (`grid-template-columns: repeat(3, 1fr)`)

### 2. Nueva estructura de cada tarjeta `.pcard`

Cada tarjeta tiene dos partes:

```
.pcard
├── .pcard-img-wrap          ← imagen fija 320px de alto
│   ├── img.pcard-img        ← zoom on hover
│   └── .pcard-img-overlay   ← gradiente sutil bottom
└── .pcard-body              ← fondo oscuro propio de cada marca
    └── .pcard-inner
        ├── p.pcard-cat      ← etiqueta en color de marca (uppercase, tracking)
        ├── h3.pcard-title   ← Fraunces serif, 2.1rem, blanco
        ├── p.pcard-rule     ← línea divisoria en color de marca (opacity 0.3)
        ├── p.pcard-desc     ← descripción corta, blanco 45%
        └── span.pcard-cta   ← "See Courses →", color de marca, uppercase
```

### 3. Colores por tarjeta

| Tarjeta | Acento | Fondo `.pcard-body` |
|---|---|---|
| Me Gusta Spanish | `#FF3B6B` | `#161616` (default) |
| Me Gusta Café | `#5aaa6a` | `#1a0e06` |
| Me Gusta Merch | `#e8a020` | `#0f0c02` |

### 4. CSS completo a añadir

Agrega este bloque `<style>` justo después del cierre de la sección:

```css
.brands-section { background:#111; padding:100px 0 0; }

.brands-header {
  max-width:1280px; margin:0 auto; padding:0 48px 72px;
  display:flex; align-items:flex-end; justify-content:space-between; gap:40px;
}
.brands-sub {
  font-size:15px; color:rgba(255,255,255,0.38);
  max-width:300px; line-height:1.8; padding-bottom:6px;
}

.brands-grid { display:grid; grid-template-columns:repeat(3,1fr); }

.pcard { display:flex; flex-direction:column; text-decoration:none; overflow:hidden; }

.pcard-img-wrap { position:relative; height:320px; overflow:hidden; flex-shrink:0; }
.pcard-img { width:100%; height:100%; object-fit:cover; transition:transform 0.9s cubic-bezier(0.25,0.46,0.45,0.94); }
.pcard:hover .pcard-img { transform:scale(1.07); }
.pcard-img-overlay {
  position:absolute; inset:0;
  background:linear-gradient(to bottom, transparent 40%, rgba(0,0,0,0.45) 100%);
}

.pcard-body { position:relative; background:#161616; padding:28px 36px 44px; flex:1; border-top:1px solid rgba(255,255,255,0.06); }
.pcard-inner { position:relative; z-index:1; }

.pcard-cat { font-size:10px; font-weight:700; letter-spacing:3.5px; text-transform:uppercase; margin-bottom:12px; }
.pcard-title { font-family:'Fraunces',serif; font-size:2.1rem; font-weight:800; color:#fff; line-height:1.05; margin-bottom:18px; }
.pcard-rule { border:none; border-top:1px solid; margin-bottom:18px; }
.pcard-desc { font-size:13px; color:rgba(255,255,255,0.45); line-height:1.8; margin-bottom:24px; }

.pcard-cta { font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase; display:inline-flex; align-items:center; gap:8px; transition:gap 0.25s; }
.pcard:hover .pcard-cta { gap:14px; }

.pcard + .pcard { border-left:1px solid rgba(255,255,255,0.07); }

@media (max-width:900px) {
  .brands-grid { grid-template-columns:1fr; }
  .pcard + .pcard { border-left:none; border-top:1px solid rgba(255,255,255,0.07); }
  .brands-header { flex-direction:column; align-items:flex-start; gap:20px; padding:0 24px 52px; }
  .brands-sub { max-width:100%; }
}
```

### 5. HTML completo de la sección

```html
<section class="brands-section scale-in" data-anim="scale">
  <div class="brands-header">
    <div>
      <p class="eyebrow" style="color:rgba(255,255,255,0.35);margin-bottom:14px" data-i18n="index.brandsEyebrow">While you're here</p>
      <h2 class="serif" style="font-size:clamp(2.4rem,4vw,3.6rem);font-weight:800;color:#fff;line-height:1.05">
        <span data-i18n="index.brandsTitle">Learn, Taste</span><br>
        <span style="color:var(--red);font-style:italic" data-i18n="index.brandsAccent">&amp; Take Home</span>
      </h2>
    </div>
    <p class="brands-sub" data-i18n="index.brandsSub">While you're in Sucre, the city has more to offer. Learn the language, discover the best coffee in town, and take something back.</p>
  </div>

  <div class="brands-grid">

    <!-- 01 Spanish School -->
    <a href="https://megustaspanish.com" target="_blank" rel="noopener" class="pcard fade-up">
      <div class="pcard-img-wrap">
        <img src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=900&fm=webp&q=82" alt="Me Gusta Spanish" loading="lazy" class="pcard-img" />
        <div class="pcard-img-overlay"></div>
      </div>
      <div class="pcard-body">
        <div class="pcard-inner">
          <p class="pcard-cat" style="color:#FF3B6B" data-i18n="index.brand1Pill">Spanish School</p>
          <h3 class="pcard-title" data-i18n="index.brand1Name">Me Gusta<br>Spanish</h3>
          <p class="pcard-rule" style="border-color:rgba(255,59,107,0.3)"></p>
          <p class="pcard-desc" data-i18n="index.brand1Desc">Bolivian teachers who share their culture, humor, and city — 750+ students, 50+ countries.</p>
          <span class="pcard-cta" style="color:#FF3B6B" data-i18n="index.brand1Cta">See Courses →</span>
        </div>
      </div>
    </a>

    <!-- 02 Café -->
    <a href="cafe.html" class="pcard fade-up" style="transition-delay:0.1s">
      <div class="pcard-img-wrap">
        <img src="https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=900&fm=webp&q=82" alt="Me Gusta Café" loading="lazy" class="pcard-img" />
        <div class="pcard-img-overlay"></div>
      </div>
      <div class="pcard-body" style="background:#1a0e06">
        <div class="pcard-inner">
          <p class="pcard-cat" style="color:#5aaa6a" data-i18n="index.brand3Pill">Café</p>
          <h3 class="pcard-title" data-i18n="index.brand3Name">Me Gusta<br>Café</h3>
          <p class="pcard-rule" style="border-color:rgba(90,170,106,0.3)"></p>
          <p class="pcard-desc" data-i18n="index.brand3Desc">Bolivian coffee and pastries baked in-house. A colonial patio where time slows down.</p>
          <span class="pcard-cta" style="color:#5aaa6a" data-i18n="index.brand3Cta">See the Menu →</span>
        </div>
      </div>
    </a>

    <!-- 03 Merch -->
    <a href="merchandising.html" class="pcard fade-up" style="transition-delay:0.2s">
      <div class="pcard-img-wrap">
        <img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=900&fm=webp&q=82" alt="Me Gusta Merch" loading="lazy" class="pcard-img" />
        <div class="pcard-img-overlay"></div>
      </div>
      <div class="pcard-body" style="background:#0f0c02">
        <div class="pcard-inner">
          <p class="pcard-cat" style="color:#e8a020" data-i18n="index.brand4Pill">Merch</p>
          <h3 class="pcard-title" data-i18n="index.brand4Name">Me Gusta<br>Merch</h3>
          <p class="pcard-rule" style="border-color:rgba(232,160,32,0.3)"></p>
          <p class="pcard-desc" data-i18n="index.brand4Desc">Designed in Sucre, made to last. Tees, totes &amp; mugs with the soul of the White City.</p>
          <span class="pcard-cta" style="color:#e8a020" data-i18n="index.brand4Cta">Shop Now →</span>
        </div>
      </div>
    </a>

  </div>
</section>
```

### 6. Notas para Claude Code

- El `<style>` puede ir en el `<head>` o inline al final de la sección — ambos funcionan.
- El `divider-line` que estaba antes de la sección puede **eliminarse** ya que la transición al fondo oscuro ya sirve de separador visual.
- Las descripciones (`.pcard-desc`) son versiones cortas — si quieres mantener el texto original de `data-i18n`, funciona igual, solo que el card se verá más largo.
- El CSS es autocontenido y no rompe ningún otro componente existente.
