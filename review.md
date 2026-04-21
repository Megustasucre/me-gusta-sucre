# Me Gusta Sucre — Project Review

## Estado actual del sitio

**URL:** megustasucre.com
**Rama:** master
**Páginas:** index, cafe, clases, hospedaje, guia, contacto, merchandising, 404
**Idiomas:** EN / ES / FR (i18n via `js/translations.js` + `data-i18n`)

---

## Lo que está hecho

### Navbar
- Logo + texto wordmark en todas las páginas
- Logo blanco cuando el navbar es transparente, a color cuando hace scroll (`filter: brightness(0) invert(1)`)
- Logo oficial: `logo-me-gusta-sucre-chinchilla.png`
- Cada sub-marca muestra su propio logo: Café (`me-gusta-cafe.png`), Spanish (`logo-me-gusta-spanish.png`), Inn (`logo-me-gusta-inn.png`)
- Texto wordmark: Lora serif, 1.75rem, "Me Gusta" blanco + nombre de marca en color (`#5aaa6a` Café, `#FF3B6B` Spanish, `#2563eb` Inn, `#c9252d` Sucre)
- Tamaño logos: 56px desktop, 40px mobile

### index.html
- Hero con Ken Burns animation
- Sección del café con galería de 3 fotos
- Sección de la escuela con galería de 3 fotos
- Brand cards: Spanish, Inn, Café, Merch
- Sección de reseñas (testimonials): marquee infinito en dos filas, reseñas reales de Google Maps de los 3 negocios, rating 4.9 / 750+ reseñas

### cafe.html
- Hero con foto de café + chips de características (BOLIVIAN COFFEE, COLONIAL PATIO, FREE WIFI, PET FRIENDLY, VEGETARIAN OPTIONS)
- Tarjeta de horarios bottom-right con dot verde animado
- Sección "Our Story", menú con fotos, galería 2x2, cross-sell con inn y escuela

### clases.html
- Hero con strip de países de origen de estudiantes (50+ países, sin países hispanohablantes)
- Location tag bottom-right
- Sección de programas, metodología, host family, cross-sell

### hospedaje.html
- Hero con Ken Burns
- 4 tipos de habitaciones con fotos y precios
- Galería de 5 fotos
- Cross-sell con café y escuela

### guia.html
- Hero con foto propia (`hero_sucre.webp`)
- Sección colonial architecture con foto propia (`san_felipe.webp`)
- Cards de lugares: Plaza 25 de Mayo, Casa de la Libertad, La Recoleta, Catedral, Cal Orcko — todos con fotos propias
- Cards de excursiones: Tarabuco, Maragua, Potosí (fotos propias), Chataquila (pendiente)
- Sección de recomendaciones del café

### merchandising.html
- Hero con `sucre_street.webp`
- 6 productos: camiseta, tote bag, mug, hoodie, libros, gift set

### 404.html
- Página trilingual con chinchilla animada pixel art (walking animation)
- Links de vuelta al sitio

---

## Imágenes

### Propias (en `/imagenes/wikipedia/`)
| Archivo | Usado en |
|---------|---------|
| `hero_sucre.webp` | guia.html — hero |
| `plaza_25mayo.webp` | guia.html — card Plaza |
| `catedral.webp` | guia.html — card Catedral |
| `casa_libertad.webp` | guia.html — card Casa de la Libertad |
| `la_recoleta.webp` | guia.html — card La Recoleta |
| `san_felipe.webp` | guia.html — sección colonial |
| `cal_orcko.webp` | guia.html — card Cal Orcko |
| `sucre_street.webp` | merchandising.html — hero |
| `tarabuco.webp` | guia.html — excursión Tarabuco |
| `maragua.webp` | guia.html — excursión Maragua |
| `potosi.webp` | guia.html — excursión Potosí |
| `chataquila.webp` | guia.html — excursión Chataquila |
| `asur.webp` | guia.html — museo ASUR |

### Pendientes de reemplazar (siguen con Unsplash)
**Fotos propias del negocio (el usuario las tiene):**
- Hero del café (interior, patio o fachada)
- Fotos de platos y postres del menú
- Galería del café (patio, interior, café servido)
- Hero de la escuela (aula, clase en acción)
- Foto de clase con profesor
- Hero del inn (fachada o lobby)
- Habitaciones: Suite Colonial, Patio Room, Standard, Dormitorio
- Galería del inn

**Fotos gratuitas a buscar:**
- Foto familia boliviana (clases.html)
- Fotos de productos merch (camiseta, tote bag, mug, hoodie)

---

## Pendiente técnico

1. **Vite + Tailwind CLI build** — Reemplazar Tailwind CDN (~400KB sin optimizar) por CSS estático purged (~5-15KB). Actualmente todas las páginas cargan `https://cdn.tailwindcss.com`.

2. **Fotos propias** — Integrar fotos reales del café, escuela e inn cuando el usuario las pase.

3. **Commit pendiente** — Los cambios de esta sesión (logos, imágenes wikipedia) aún no están commiteados.
