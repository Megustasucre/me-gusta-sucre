# Me Gusta Sucre — Project Review

**URL:** megustasucre.com  
**Rama:** master  
**Páginas:** index, cafe, clases, hospedaje, guia, contacto, merchandising, 404  
**Idiomas:** EN / ES / FR (i18n via `js/translations.js` + `data-i18n`)

---

## Estado actual por página

### index.html
- Hero con Ken Burns animation
- Sección del café: layout diagonal con `clip-path:polygon()`, imagen a la derecha, card de horarios/dirección
- Brand cards: Spanish, Inn, Café, Merch
- Reseñas: marquee infinito en dos filas, reseñas reales de Google Maps (4.9 / 750+)

### cafe.html
- Hero, Info Bar, Intro, Nuestros Cafés (Lavazza/Jaqaku), Menú 8 items (Bebidas + Comida), CTA, Atmosphere, Cross-sell, Footer

### clases.html — MINI-PAGINA
- Hero con strip de países, botón directo a `megustaspanish.com`
- Stats: 750+ estudiantes, 3 profesores, 50+ países, 20+ años
- Programas: 4 cards compactas (nombre, tipo, precio)
- CTA → `megustaspanish.com`

### hospedaje.html
- Color de marca: **turquesa `#14b8a6`** (oscuro `#0f766e`, claro `#2dd4bf`, muy claro `#99f6e4`)
- Hero → `#rooms` (ver habitaciones)
- 4 habitaciones: Deluxe Suite ($65), Standard Private ($45), Standard Room ($35), Dorm Bed ($18)
- Cada card tiene CTA que pre-selecciona la habitación en el formulario y scrollea a `#reservar`
- **Formulario de reservas** (`#reservar`): selector visual de habitación, fechas con min-date automático, contador de noches en tiempo real, huéspedes, nombre, mensaje opcional → envía por WhatsApp con datos pre-formateados
- CTA final → `#reservar` (no WhatsApp directo)

### guia.html
- Hero: `hero_guia.webp`, CTAs → `clases.html` + `hospedaje.html`
- **Barra de sección sticky** con anclas: Must-See Spots / Day Trips / Practical Tips / Food & Coffee (scroll-spy activo, traducida EN/ES/FR)
- Quick facts bar: 2810m, 1538, UNESCO 1991, 300+ días de sol
- Bento grid de spots: Plaza 25 de Mayo (large), Casa de la Libertad, Recoleta Viewpoint, Catedral, USFX, Cal Orcko
- Day trips: Tarabuco, Maragua, Potosí, Chataquila — todos con CTA "Ask us anything →" → WhatsApp
- Practical tips: 4 cards (clima, moneda, transporte, mejor época)
- Food & Coffee: lista editorial de platos + cross-sell Café
- **Sección de cierre** (reemplaza cross-sell + CTA final): grid 2/3 + 1/3 — escuela con imagen de fondo (producto principal), Inn compact card con precio "from $18/night"
  - Escuela: imagen de fondo, título "Learn Spanish while you're here", pills, CTA → `clases.html`
  - Inn: turquesa, precio ancla, bullet list, CTA → `hospedaje.html`

### contacto.html
- Hero split: texto izquierda / brand preview cards derecha
- 3 cards: Me Gusta Spanish (rosa), Inn (azul), Café (verde)
- Cada card con dirección, teléfono, email, botón WhatsApp

### merchandising.html
- Hero con `sucre_street.webp`
- 6 productos: camiseta, tote bag, mug, hoodie, libros, gift set

### 404.html
- Página trilingual con chinchilla animada pixel art

---

## Técnico

### CSS
- **Tailwind v3 CLI** — build local purged (~15KB) en `css/tw.css`
- Input: `css/tw-input.css`, config: `tailwind.config.js`, script: `npm run build:css`
- `css/style.css` — componentes custom: `.room-amenity`, `.room-cta`, `.btn-red`, `.eyebrow`, `.fade-up`, `.hero-kenburns`, `.whatsapp-float`, etc.
- `hospedaje.html` tiene overrides de `.room-amenity` para turquesa (no afecta otras páginas)

### i18n
- Todo en `js/translations.js` — objetos `en`, `es`, `fr` con claves anidadas por página
- `data-i18n="clave"` → setea `textContent`
- `data-i18n-html="clave"` → setea `innerHTML` (para claves con spans/HTML embebido)
- `data-i18n-placeholder` → placeholders de inputs (con función custom en `hospedaje.html`)

### Imágenes
- Propias en `/imagenes/wikipedia/` como `.webp`
- Unsplash para fotos de negocio (temporales hasta tener fotos reales)
- Logos en `/imagenes/logos/`

---

## Imágenes propias actuales

| Archivo | Usado en |
|---------|----------|
| `hero_guia.webp` | guia.html — hero |
| `catedral.webp` | guia.html — card Catedral |
| `cal_orcko.webp` | guia.html — card Cal Orcko (slide 2) |
| `cal_orcko_parque.webp` | guia.html — card Cal Orcko (slide 1) |
| `casa_libertad.webp` | guia.html — card Casa de la Libertad |
| `patio-usfx.webp` | guia.html — card USFX |
| `recoleta.webp` | guia.html — card La Recoleta |
| `san_felipe.webp` | guia.html — sección colonial |
| `plaza_25mayo.webp` | guia.html — card Plaza + CTA final |
| `sucre_street.webp` | merchandising.html — hero |
| `tarabuco.webp` | guia.html — excursión Tarabuco |
| `maragua.webp` | guia.html — excursión Maragua |
| `potosi.webp` | guia.html — excursión Potosí |
| `chataquila.webp` | guia.html — excursión Chataquila |
| `iglesia-san-francisco.webp` | contacto.html — hero background |

---

## Colores de marca por producto

| Producto | Principal | Oscuro | Claro |
|----------|-----------|--------|-------|
| Me Gusta Sucre (global) | `#c9252d` | — | — |
| Me Gusta Spanish (escuela) | `#FF3B6B` | — | — |
| Me Gusta Inn | `#14b8a6` | `#0f766e` | `#99f6e4` |
| Me Gusta Café | `#5aaa6a` | — | — |

---

## Objetivos nuevos — próxima sesión

### Identidad de marca (problema central)
La IA detectó que la página tiene identidad dividida. Se definió lo siguiente:

**Frase central de marca:**
> "Los mejores recuerdos que te puedes llevar de Bolivia — desde la estadía, las clases y el café."

**Audiencia:** turistas internacionales, regionales y nacionales (los tres por igual)
**Acción principal:** guía de la ciudad + ofrecer los servicios (inn, café, clases, merch)

---

### Re-arquitectura del index.html
Rediseñar el flujo completo basado en la lógica del viajero:

```
1. Hero        — nueva frase central + CTA: "Explore Sucre" + "Book a Stay"
2. Barra       — 4.9★ · 750+ viajeros · UNESCO Heritage · Ciudad Blanca
3. Servicios   — 4 cards: Inn / Café / Clases / Merch
4. City guide  — 3 highlights de Sucre → guia.html
5. Reviews     — marquee actual (ya existe, mover más arriba)
6. CTA final   — WhatsApp / Contacto
```

Problemas a resolver del análisis IA:
- [ ] Jerarquía del nav — definir primario vs secundario
- [ ] Hero CTA — un botón dominante, no dos del mismo peso
- [ ] Reviews enterradas al 85% del scroll — moverlas más arriba
- [ ] Duplicación de contenido (café aparece 2 veces en el index)

---

### Información pendiente que debe enviar el usuario
- [ ] Números de contacto actualizados
- [ ] Fotos reales del café (interior, patio, barra)
- [ ] Fotos reales del inn (habitaciones, fachada, áreas comunes)
- [ ] Fotos de clases (aula, profesor, estudiantes)

---

### Páginas nuevas solicitadas
- [ ] Blog de turistas en Sucre (atracciones gratuitas, de pago, familiares, entretenimiento)
- [ ] Página de Actividades / Me Gusta Trekkers

### guia.html — evolución a blog
Convertir la guía de ciudad en un blog editorial de viajes:
- Artículos sobre lugares para visitar en Sucre (gratuitos, de pago, familiares, entretenimiento)
- Estilo blog: imagen destacada, fecha, categoría, texto editorial
- Puede reemplazar o complementar el bento grid actual de spots
- Contenido generado por el equipo de Me Gusta Sucre como expertos locales

### Funcionalidades nuevas
- [ ] Chatbot de contacto (solo para Spanish School e Inn) — decidir plataforma (Tidio, Crisp o simulado con WhatsApp)
- [ ] E-commerce con Takenos — merch, vouchers de clase, reservas
- [ ] CNAME en el repo para `megustasucre.com` (GitHub Pages custom domain)

### Pendiente anterior
- [ ] Números de contacto actualizados
