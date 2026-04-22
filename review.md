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

### cafe.html — MINI-PAGINA (pendiente)
Actualmente tiene: Hero, Info Bar, Intro (historia), Nuestros Cafés (Lavazza/Jaqaku), Menú 8 items, CTA Full Menu, Atmosphere (polaroids), Cross-sell, Footer.  
**Pendiente:** reducir a Hero + Info Bar + Menú (4 items) + CTA → sitio del café + Footer.

### clases.html — MINI-PAGINA (hecho)
- Hero con strip de países, botón directo a `megustaspanish.com`
- Stats: 750+ estudiantes, 3 profesores, 50+ países, 20+ años
- Programas: 4 cards compactas (nombre, tipo, precio)
- CTA → `megustaspanish.com`
- Footer
- **Eliminado:** Why Sucre (3 cards), Host Family, Cross-sell. 604 → 429 líneas.

### hospedaje.html — MINI-PAGINA (pendiente)
Actualmente tiene: Hero, Rooms (3 hab. detalladas), Amenidades, Galería, Reviews, Ubicación, Cross-sell, CTA Final, Footer.  
**Pendiente:** reducir a Hero + Rooms compactas + CTA → sitio del inn + Footer.

### guia.html
- Hero: `hero_guia.webp` (vista aérea de Sucre)
- Cards (240px): Catedral (landscape, `object-position:center 20%`), USFX Derecho, Cal Orcko (carrusel CSS con `cal_orcko_parque.webp` + `cal_orcko.webp`), Casa de la Libertad
- Plaza 25 de Mayo, La Recoleta, San Felipe Neri
- Excursiones: Tarabuco, Maragua, Potosí, Chataquila

### merchandising.html
- Hero con `sucre_street.webp`
- 6 productos: camiseta, tote bag, mug, hoodie, libros, gift set

### 404.html
- Página trilingual con chinchilla animada pixel art

---

## Técnico

### CSS
- **Tailwind v3 CLI** — build local purged (~15KB) en `css/tw.css`. CDN reemplazado.
- Input: `css/tw-input.css`, config: `tailwind.config.js`, script: `npm run build:css`

### i18n
- Todo en `js/translations.js` — objetos `en`, `es`, `fr` con claves anidadas por página
- Atributo `data-i18n="clave"` en el HTML, sin routing por idioma

### Imágenes
- Propias en `/imagenes/wikipedia/` como `.webp` (convertidas con Pillow)
- Unsplash para fotos de negocio (temporales hasta tener fotos reales)

---

## Imágenes propias actuales

| Archivo | Usado en |
|---------|----------|
| `hero_guia.webp` | guia.html — hero |
| `catedral.webp` | guia.html — card Catedral |
| `cal_orcko.webp` | guia.html — card Cal Orcko (slide 2) |
| `cal_orcko_parque.webp` | guia.html — card Cal Orcko (slide 1) |
| `casa_libertad.webp` | guia.html — card Casa de la Libertad |
| `patio_usfx.webp` | guia.html — card USFX |
| `la_recoleta.webp` | guia.html — card La Recoleta |
| `san_felipe.webp` | guia.html — sección colonial |
| `plaza_25mayo.webp` | guia.html — card Plaza |
| `sucre_street.webp` | merchandising.html — hero |
| `tarabuco.webp` | guia.html — excursión Tarabuco |
| `maragua.webp` | guia.html — excursión Maragua |
| `potosi.webp` | guia.html — excursión Potosí |
| `chataquila.webp` | guia.html — excursión Chataquila |

---

## Pendiente

### Inmediato
- [ ] Slim down `cafe.html` a mini-página
- [ ] Slim down `hospedaje.html` a mini-página

### Fotos reales (cuando el usuario las pase)
- Hero del café (interior, patio o fachada)
- Fotos de platos del menú
- Galería del café
- Hero de la escuela (aula, clase)
- Hero del inn (fachada o lobby)
- Habitaciones del inn

### Futuro
- Me Gusta Trekkers — página nueva
- E-commerce con Takenos
- CNAME en el repo para `megustasucre.com` (GitHub Pages custom domain)
