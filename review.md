# Review — Me Gusta Sucre (2026-04-16)

## guia.html — Estado actual

### Lo que esta bien
- Nav desktop: split correcto (Spanish Classes · Cafe · City Guide | Stay · Merch · Contact)
- Nav mobile: 6 links completos incluyendo Merch
- Footer Explore: corregido (ya no hay City Guide duplicado)
- SEO: og tags, canonical, robots, JSON-LD TouristDestination con coordenadas GPS
- Favicon: favicon-guia.svg (pin de mapa solido rojo)
- Seccion "What to eat": lista editorial con platos destacados por color
  - Chorizo Chuquisaqueno — rojo italico, badge "Most representative"
  - Saltena, Mondongo, Picante de Pollo, Picana — tipografia neutra
  - Chocolate de Sucre — dorado, badge "Best in Bolivia"
  - Ajenjo — verde, badge "Regional liqueur"
  - Nota del aji chuquisaqueno en tarjeta oscura al final
- Cafe badge animado (float loop) con logo, link a cafe.html, "See the menu"
- Seccion day trips: Tarabuco, Maragua, Potosi, Chataquila
- Seccion practical tips: Altitude, Currency, Getting Around, Best Time

### Pendientes / cosas a mejorar

1. **Imagenes Unsplash genericas** — Las fotos no son de Sucre real. Prioridad alta cuando haya fotos propias:
   - Hero: foto de paisaje generico, no es Sucre
   - Potosi card reutiliza la misma imagen que Plaza 25 de Mayo
   - ASUR Museum card reutiliza la misma imagen que el hero

2. **`<style>` del cafe badge en el body** — El bloque @keyframes floatBadge esta dentro del div de la imagen, no en head. Funciona pero es mejor moverlo a css/style.css.

3. **og:url y canonical apuntan a megustasucre.com** — El sitio vive en megustasucre.github.io/me-gusta-sucre/. Cuando haya dominio propio esto estara correcto; mientras tanto las previsualizaciones sociales pueden no funcionar del todo.

4. **"Chorizo Chuquisaqueno" sin tilde** — Deberia ser "Chuquisaqueno". Revisar render en produccion con Lora.

5. **CTA "See the Full Menu" en cafe.html** — Todavia apunta a "#". Pendiente URL real del menu completo.

---

## Estado global del sitio

| Pagina          | Nav | SEO | Favicon                    | Schema                  |
|-----------------|-----|-----|----------------------------|-------------------------|
| index.html      | OK  | OK  | logo principal             | Organization            |
| cafe.html       | OK  | OK  | me-gusta-cafe.png          | CafeOrCoffeeShop        |
| clases.html     | OK  | OK  | logo-me-gusta-spanish.png  | EducationalOrganization |
| hospedaje.html  | OK  | OK  | logo-me-gusta-inn.png      | LodgingBusiness         |
| guia.html       | OK  | OK  | favicon-guia.svg           | TouristDestination      |
| contacto.html   | OK  | OK  | favicon principal          | Organization            |
| merchandising   | OK  | OK  | favicon-merch.svg          | —                       |

actividades.html: eliminado y removido del sitemap.

## Push pendiente
Los cambios de esta sesion (guia.html — food section, mobile menu, footer fix, cafe badge, ajenjo) no han sido pusheados a GitHub todavia.
