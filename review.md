# Review — Me Gusta Sucre (Actualizado: 2026-04-17)

## Estado General del Proyecto

El sitio web es una plataforma **multi-idioma (Inglés, Español y Francés)** con subdirectorios `/en/`, `/es/`, `/fr/`. La infraestructura de enrutamiento, selección de idioma y UI compartida (nav/footer) ya están completas en las 21 páginas. Las traducciones editoriales del cuerpo de las páginas secundarias están parcialmente completas.

---

## Traducciones Completadas

| Página         | EN | ES | FR |
|----------------|----|----|----|
| index.html     | ok | ok | ok |
| guia.html      | ok | pendiente | pendiente |
| cafe.html      | ok | ok | ok |
| clases.html    | ok | ok | ok |
| hospedaje.html | ok | pendiente | pendiente |
| merchandising.html | ok | pendiente | pendiente |
| contacto.html  | ok | pendiente | pendiente |

---

## Tareas Pendientes

### 1. Traducciones Editoriales Restantes (Prioridad Alta)

Las siguientes 6 páginas necesitan traduccion completa del cuerpo (head meta + body content) en ambos idiomas. La UI (nav/footer) ya está en el idioma correcto — solo falta el contenido editorial:

- **es/guia.html** y **fr/guia.html**
- **es/hospedaje.html** y **fr/hospedaje.html**
- **es/merchandising.html** y **fr/merchandising.html**
- **es/contacto.html** y **fr/contacto.html**

Nota sobre hospedaje.html: la sesión anterior fue interrumpida justo al leer el archivo de referencia (en/hospedaje.html). El archivo es/hospedaje.html tiene nav/footer en español pero todo el body en inglés. Se leyó hasta la línea ~530 del archivo de referencia; falta leer el resto (reviews, location, CTA final) antes de editar.

### 2. Optimización SEO Multi-idioma (Prioridad Media)

- **sitemap.xml**: Reescribir para incluir las tres variantes de URL por pagina con etiquetas `<xhtml:link rel="alternate" hreflang="x">`.
- **Etiquetas hreflang**: Agregar `<link rel="alternate" hreflang="x" href="...">` en el `<head>` de todas las páginas de los tres idiomas.

### 3. Reemplazo de Imágenes (Prioridad Baja)

- Sustituir fotos de Unsplash por fotografías originales de Me Gusta Sucre cuando sean entregadas, optimizadas en WebP.

### 4. Actualización de Enlaces Definitivos

- Los enlaces del menu del Café apuntan a un flujo provisional de WhatsApp. Actualizar al link oficial cuando esté disponible.

---

## Estructura de Directorios Actual

```
/ (raíz)
 ├── index.html        (Redireccionamiento automatico por idioma del navegador)
 ├── css/              (Estilos compartidos)
 ├── js/               (Scripts compartidos)
 ├── images/           (Assets compartidos)
 ├── en/               (Contenido completo en ingles — fuente de referencia)
 │   └── index, guia, cafe, clases, hospedaje, merchandising, contacto.html
 ├── es/               (UI en español completa — body pendiente en 4 páginas)
 └── fr/               (UI en francés completa — body pendiente en 4 páginas)
```

---

## Notas Tecnicas para la Proxima Sesion

- Al traducir, respetar el contenido ya traducido en nav/footer (no sobreescribir).
- En fr/clases.html habia strings pre-traducidos ("Contactez-nous") de sesiones anteriores — siempre verificar con Grep antes de aplicar Edit.
- Los WhatsApp links deben tener el texto pre-llenado URL-encoded en el idioma correcto.
- Canonical URL y og:url deben apuntar a la ruta del idioma correspondiente (e.g. `/es/hospedaje.html`).
- JSON-LD description tambien debe traducirse.
