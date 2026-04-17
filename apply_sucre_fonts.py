import os
import re

target_files = ['index.html', 'hospedaje.html', 'merchandising.html', 'contacto.html', 'guia.html', 'cafe.html', 'clases.html']

fonts_css = """@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Lora:ital,wght@0,400..700;1,400..700&family=Satisfy&display=swap');

body, .eyebrow, .btn-red, .btn-gold, .btn-outline, .btn-outline-dark, .top-bar, .nav-link, .badge, .float-tag, .room-amenity, .room-cta, .brand-card-pill, .brand-card-cta, .whatsapp-float {
  font-family: 'DM Sans', sans-serif !important;
}

.serif, .section-title, .brand-card-name {
  font-family: 'Lora', serif !important;
}

.handwritten {
  font-family: 'Satisfy', cursive !important;
}

.polaroid::after {
  font-family: 'Satisfy', cursive !important;
}
"""

os.makedirs('css', exist_ok=True)
with open('css/sucre-fonts.css', 'w', encoding='utf-8') as f:
    f.write(fonts_css)

old_font_url = r"https://fonts\.googleapis\.com/css2\?family=Fraunces[^\"']*"
new_font_url = "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&family=Lora:ital,wght@0,400..700;1,400..700&family=Satisfy&display=swap"

for filename in target_files:
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the google fonts URL
    content = re.sub(r"https://fonts\.googleapis\.com/css2\?family=[^\"']*", new_font_url, content)
    
    # Replace inline font names
    content = content.replace("Fraunces", "Lora")
    content = content.replace("Playfair Display", "Lora")
    content = content.replace("Plus Jakarta Sans", "DM Sans")
    content = content.replace("Sacramento", "Satisfy")
    
    # Inject sucre-fonts.css after style.css
    if 'css/sucre-fonts.css' not in content:
        content = content.replace('<link rel="stylesheet" href="css/style.css" />', 
                                  '<link rel="stylesheet" href="css/style.css" />\n  <link rel="stylesheet" href="css/sucre-fonts.css" />')
                                  
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated {filename}")

print("Done!")
