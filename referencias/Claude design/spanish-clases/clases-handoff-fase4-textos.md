# Handoff para Claude Code — clases.html (Fase 4: Textos y Sincronización i18n)
*Diagnóstico Antigravity UX/UI · 25 Abril 2026*

---

## Contexto

Esta fase corrige el copy de la página y sincroniza las traducciones. El inglés (EN) ya tiene el nuevo texto actualizado en `translations.js`. El problema es que **Español (ES) y Francés (FR) aún tienen el copy antiguo**, lo que rompe la experiencia al cambiar de idioma.

**Archivos a modificar:**
- `js/translations.js` — objeto `"es" > "clases"` y `"fr" > "clases"`
- `clases.html` — 1 texto hardcodeado (heroBadge)

---

## 1. Fix en `clases.html` — Badge del Hero

**Busca** (línea ~121):
```html
data-i18n="clases.heroBadge">The most fun &amp; friendly Spanish school in Sucre
```

**Reemplaza** el contenido visible del span por:
```html
data-i18n="clases.heroBadge">Probably the most fun &amp; friendly Spanish school in Sucre
```

> Esta suavización con "Probably" convierte una afirmación superlativa arrogante en una afirmación con personalidad y humor, más honesta y creíble.

---

## 2. Actualizar `translations.js` — Sección `"en" > "clases"`

Localizar la sección `"en"` > `"clases"` (aproximadamente línea 376) y actualizar la key `heroBadge`:

```js
// ANTES:
"heroBadge": "The most fun & friendly Spanish school in Sucre",

// DESPUÉS:
"heroBadge": "Probably the most fun & friendly Spanish school in Sucre",
```

---

## 3. Actualizar `translations.js` — Sección `"es" > "clases"` (CRÍTICO)

Localizar la sección `"es"` > `"clases"` (aproximadamente línea 1099) y reemplazar las siguientes keys con el nuevo copy traducido al español:

```js
// === KEYS A REEMPLAZAR ===

"heroBadge": "Probablemente la escuela de español más divertida de Sucre",

"heroAccent": "donde mejor suena",

"heroSub": "Sucre tiene el acento de español más claro de Sudamérica. Sin atajos ni cadenas de escuelas — solo Fernando, Ely y una ciudad hecha para aprender.",

"heroCta1": "Ver Cursos y Precios ↗",

"heroCta2": "Pregúntanos lo que sea",

"introEyebrow": "Audiencia 97, Sucre — Nuestro hogar",

"introTitle": "No solo clases —",

"introAccent": "una vida en español",

"introP": "Fernando y Ely fundaron esta escuela en 2011 con una sola creencia: la mejor forma de aprender es vivirlo. Profesores bolivianos nativos, conversaciones reales desde el primer día y una ciudad Patrimonio UNESCO que hace que cada lección valga.",

"exp1": "Lecciones diseñadas según tus metas — viajes, trabajo o inmersión total",

"exp2": "El aprendizaje continúa afuera: mercados, clases de cocina, paseos por la ciudad con locales",

"exp3": "Más de 750 estudiantes de 50+ países — algunos vinieron por una semana y se quedaron meses",

"modal1Name": "Clases Presenciales",

"modal1Desc": "Inmersión total en la ciudad con el español más claro del continente. Profesores nativos, grupos pequeños y la vida real como tu aula — cada día.",

"modal2Desc": "Sesiones en vivo con el equipo de Fernando y Ely. Horarios flexibles, tu zona horaria, y una clase de prueba gratuita para empezar — sin compromiso.",

"ctaTag": "Listos cuando tú quieras",

"ctaTitle": "Conoce Me Gusta Spanish",

"ctaSub": "Horarios, precios, inscripciones y reservas online — todo lo que necesitas está en el sitio web oficial de la escuela.",

"ctaBtn1": "Ir a Me Gusta Spanish ↗",

"ctaBtn3": "Envíanos un Mensaje",
```

---

## 4. Actualizar `translations.js` — Sección `"fr" > "clases"` (CRÍTICO)

Localizar la sección `"fr"` > `"clases"` (aproximadamente línea 1808) y reemplazar las siguientes keys:

```js
// === KEYS A REEMPLAZAR ===

"heroBadge": "Probablement l'école d'espagnol la plus sympa de Sucre",

"heroAccent": "là où ça sonne le mieux",

"heroSub": "Sucre possède l'accent espagnol le plus clair d'Amérique du Sud. Pas de raccourcis ni de chaînes scolaires — juste Fernando, Ely et une ville faite pour apprendre.",

"heroCta1": "Voir Cours et Tarifs ↗",

"heroCta2": "Posez-nous n'importe quelle question",

"introEyebrow": "Audiencia 97, Sucre — Notre maison",

"introTitle": "Pas seulement des cours —",

"introAccent": "une vie en espagnol",

"introP": "Fernando et Ely ont fondé cette école en 2011 avec une seule conviction : la meilleure façon d'apprendre, c'est de le vivre. Des professeurs boliviens natifs, de vraies conversations dès le premier jour, et une ville Patrimoine UNESCO qui donne du sens à chaque leçon.",

"exp1": "Des cours façonnés selon vos objectifs — voyage, travail ou immersion totale",

"exp2": "L'apprentissage continue à l'extérieur : marchés, cours de cuisine, balades en ville avec des locaux",

"exp3": "Plus de 750 étudiants de 50+ pays — certains sont venus pour une semaine et sont restés des mois",

"modal1Name": "Cours en Présentiel",

"modal1Desc": "Immersion totale dans la ville où l'espagnol sonne le mieux. Professeurs natifs, petits groupes et la vie réelle comme salle de classe — chaque jour.",

"modal2Desc": "Sessions en direct avec l'équipe de Fernando et Ely. Horaires flexibles, votre fuseau horaire, et un cours d'essai gratuit pour commencer — sans engagement.",

"ctaTag": "Prêts quand vous l'êtes",

"ctaTitle": "Découvrez Me Gusta Spanish",

"ctaSub": "Horaires, tarifs, inscriptions et réservations en ligne — tout ce qu'il vous faut est sur le site officiel de l'école.",

"ctaBtn1": "Aller sur Me Gusta Spanish ↗",

"ctaBtn3": "Envoyez-nous un Message",
```

---

## 5. Fix Factual — Año de Fundación (Dato a Confirmar)

> ⚠️ **ACCIÓN REQUERIDA ANTES DE EJECUTAR:** La página muestra "20+ Years Experience" en el stat counter, pero el copy dice "founded in 2011" (14 años) y `programsSub` menciona "since 2005" en ES y FR. Hay 3 fechas distintas en conflicto.
>
> El cliente debe confirmar el año real de fundación. Mientras tanto, **no modificar los stats**. Una vez confirmado, actualizar:
> - El stat `data-target` en el HTML (si aplica)
> - La key `programsSub` en ES y FR que dice "desde 2005"
> - El `introP` en los 3 idiomas para que tenga el año correcto

---

## Orden de Ejecución

1. `clases.html` — fix del heroBadge (1 línea)
2. `translations.js` EN — fix de heroBadge (1 key)
3. `translations.js` ES — actualizar las 15 keys listadas arriba
4. `translations.js` FR — actualizar las 15 keys listadas arriba
5. ⏸️ PAUSAR — esperar confirmación del año de fundación para el fix factual

---

*Documento generado por Antigravity UX/UI Architect. Listo para ejecución en Claude Code.*
