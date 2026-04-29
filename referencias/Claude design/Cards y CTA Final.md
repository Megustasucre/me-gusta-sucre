# Cambios: Cards + CTA Final

## 1. `css/style.css` — Cards de atracciones

### Agregar borde a `.card`

Buscar:
```css
.card {
  background: #fff;
  border-radius: 0;
  overflow: hidden;
  box-shadow: 0 6px 32px rgba(26,18,10,0.08);
  transition: transform 0.3s, box-shadow 0.3s;
}
```

Reemplazar por:
```css
.card {
  background: #fff;
  border-radius: 0;
  overflow: hidden;
  box-shadow: 0 6px 32px rgba(26,18,10,0.08);
  transition: transform 0.3s, box-shadow 0.3s;
  border: 1px solid rgba(26,18,10,0.06);
}
```

### Agregar animación de arrow en links de card

Al final del bloque de cards en `style.css`, agregar:

```css
/* ─── CARD LINK — arrow animado al hover ─── */
.card-body-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: gap 0.2s ease;
}
.card-body-link:hover { gap: 10px; }
```

---

## 2. `index.html` — Links "Explore →" en cards

Hay 3 cards. En cada una, buscar el link y agregar la clase `card-body-link`.

### Buscar (3 veces, una por card):
```html
<a href="guia.html" style="font-family:'Plus Jakarta Sans',sans-serif;font-size:13px;font-weight:700;color:var(--red);text-decoration:none" data-i18n="index.explore">Explore →</a>
```

### Reemplazar por:
```html
<a href="guia.html" class="card-body-link" style="font-family:'Plus Jakarta Sans',sans-serif;font-size:13px;font-weight:700;color:var(--red);text-decoration:none" data-i18n="index.explore">Explore →</a>
```

---

## 3. `index.html` — CTA Final: altura de 600px → 520px

### Buscar:
```html
<div style="position:relative;height:600px;overflow:hidden">
```

### Reemplazar por:
```html
<div style="position:relative;height:520px;overflow:hidden">
```

---

*Archivos afectados: `css/style.css` · `index.html`*
