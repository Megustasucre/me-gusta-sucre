# Me Gusta Sucre — Project Review

**URL:** megustasucre.com  
**Rama:** master  
**Páginas:** index, cafe, clases, hospedaje, guia, contacto, merchandising, 404  
**Idiomas:** EN / ES / FR (i18n via `js/translations.js` + `data-i18n`)  
**Última actualización:** 24 de Abril, 2026

---

## Estado actual por página

### index.html — COMPLETADA

Orden de scroll implementado:
```
Hero → Ticker → Trust Bar → Brand Cards → Atracciones → Reviews → CTA Final → Footer
```

- **Top bar eliminado**
- **Hero:** Ken Burns animation — H1 "Your Base in Sucre", CTA primario `btn-red` → Book Your Stay, CTA secundario `btn-outline` → City Guide
- **Trust Bar:** barra `#111111` con 4 datos — 4.9★ Google · 750+ Travelers · UNESCO 1991 · 20+ yrs Spanish School. Responsive 2x2 en mobile. SVG de transición curva hacia Brand Cards.
- **Brand Cards** (orden: Inn, Spanish, Café, Merch): Inn `#14b8a6`, Spanish `#FF3B6B`, Café `#5aaa6a`, Merch `#e8a020` — color del Inn corregido de azul a turquesa en todos sus usos
- **Atracciones:** 3 cards (Plaza 25 de Mayo, Cal Orcko, La Recoleta) — imagen 300px
- **Reviews:** marquee infinito, reseñas reales de Google Maps (4.9 / 750+) — posición ~60% del scroll
- **CTA Final:** banner con `sucre_street.webp`, 600px, `object-position:center 35%`
- **Tipografía migrada:** `Lora` → `Fraunces`, `DM Sans` → `Plus Jakarta Sans`. Google Fonts actualizado.
- **Variables CSS:** `#c9252d` → `var(--red)`, `#111111` → `var(--text)`, `#555555` → `var(--muted)`
- **Copywriting** (tono "Anfitrión Experto"): hero sub, brand cards, atracciones subtitle, CTA final. Tono elevado via agente turismo.
- **Espaciado luxury:** Brand Cards + Atracciones en 140px, Testimonials 130px/120px. Clase `.section-luxury` en `style.css`.
- **Secciones eliminadas:** Why Sucre, Café Preview standalone, Spanish School Preview standalone, Inn Section standalone
- **Terminología corregida:** "boutique inn" → "hostal", "specialty coffee" / "single-origin" eliminados de todos los textos

### cafe.html

- Hero, Info Bar, Intro, Nuestros Cafés (Lavazza/Jaqaku), Menú 8 items (Bebidas + Comida), CTA, Atmosphere, Cross-sell, Footer
- **Meta tags corregidos:** eliminadas referencias a "specialty" y "single-origin" en description, OG, Twitter y JSON-LD

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
- **Sección de cierre:** grid 2/3 + 1/3 — escuela con imagen de fondo, Inn compact card con precio "from $18/night"

### contacto.html

- Hero split: texto izquierda / brand preview cards derecha
- 3 cards: Me Gusta Spanish (rosa), Inn (turquesa), Café (verde)
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
- `css/style.css` — componentes custom: `.room-amenity`, `.room-cta`, `.btn-red`, `.eyebrow`, `.fade-up`, `.hero-kenburns`, `.whatsapp-float`, `.section-luxury`, etc.
- `hospedaje.html` tiene overrides de `.room-amenity` para turquesa (no afecta otras páginas)
- **Navbar:** `top:0` (top bar eliminado), `.hero-section { padding-top:110px }`

### i18n

- Todo en `js/translations.js` — objetos `en`, `es`, `fr` con claves anidadas por página
- `data-i18n="clave"` → setea `textContent`
- `data-i18n-html="clave"` → setea `innerHTML` (para claves con spans/HTML embebido)
- `data-i18n-placeholder` → placeholders de inputs (con función custom en `hospedaje.html`)
- **Importante:** el JS sobreescribe el HTML al cargar — el texto visible al usuario es siempre el de `translations.js`, no el fallback del HTML

### Imágenes

- Propias en `/imagenes/` como `.webp`
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

## Identidad de marca

**Frase central:**
> "Los mejores recuerdos que te puedes llevar de Bolivia — desde la estadía, las clases y el café."

**Audiencia:** turistas internacionales, regionales y nacionales  
**Acción principal:** guía de la ciudad + ofrecer los servicios (hostal, café, clases, merch)  
**Tono:** Anfitrión Experto — humano, local, sin marketing genérico

**Terminología fija:**
- "hostal" (no "boutique inn", no "posada boutique")
- "café boliviano" (no "specialty coffee", no "single-origin")
- La escuela existe hace 20+ años — no es nueva, es el producto más antiguo

---

## Pendiente

### Contenido / Activos
- [ ] Números de contacto actualizados (todas las páginas)
- [ ] Fotos reales: Inn (habitaciones, fachada, áreas comunes), Café (interior, patio, barra), Clases (aula, profesor, estudiantes)
- [ ] Social proof visual — fotos de personas reales junto a testimonios

### Diseño / UX
- [ ] Tipografía migrada solo en index.html — falta en: guia.html, hospedaje.html, merchandising.html, clases.html, cafe.html, contacto.html
- [ ] Jerarquía del nav — separar visualmente primario (Stay, City Guide) de secundario (Café, Clases, Merch, Contact)

### Páginas nuevas
- [ ] guia.html — evolución a blog editorial de viajes (artículos por categoría: gratuito, de pago, familiar, entretenimiento)
- [ ] Página de Actividades / Me Gusta Trekkers

### Funcionalidades
- [ ] Chatbot — solo para Spanish School, Inn y Merch (NO Café). Plataforma sin decidir (Tidio, Crisp o simulado con WhatsApp)
- [ ] E-commerce con Takenos — merch, vouchers de clase, reservas
- [ ] CNAME en el repo para `megustasucre.com` (GitHub Pages custom domain)
