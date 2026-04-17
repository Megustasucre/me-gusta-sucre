import os, shutil, re

html_files = ['index.html', 'guia.html', 'cafe.html', 'clases.html', 'hospedaje.html', 'merchandising.html', 'contacto.html']
folders = ['en', 'es', 'fr']

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Process EN folder first
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update relative paths for static assets
    content = content.replace('href="css/', 'href="../css/')
    content = content.replace('src="js/', 'src="../js/')
    content = content.replace('src="images/', 'src="../images/')
    content = content.replace('href="images/', 'href="../images/')
    content = content.replace('src="imagenes/', 'src="../imagenes/')
    content = content.replace('href="imagenes/', 'href="../imagenes/')
    
    # Update internal links to point to same folder
    # Example: href="guia.html" -> keep as is.
    # What about a href="index.html"? Keep as is, it navigates within the folder.
    
    # We will inject the language selector programmatically to avoid mistakes
    # Find the right links section in the desktop navbar
    nav_right_desktop = r'<div class="hidden md:flex items-center justify-end gap-7" style="flex:1">([\s\S]*?)</div>'
    def insert_lang_selector(match):
        inner_content = match.group(1)
        lang_selector = f'''
        <!-- Language Selector -->
        <div class="flex items-center gap-3 border-l border-white/20 pl-6 ml-2">
          <a href="../en/{file}" class="text-xs font-bold text-white hover:text-white/70 transition-colors uppercase">EN</a>
          <span class="text-white/30 text-xs">|</span>
          <a href="../es/{file}" class="text-xs font-bold text-white/50 hover:text-white transition-colors uppercase">ES</a>
          <span class="text-white/30 text-xs">|</span>
          <a href="../fr/{file}" class="text-xs font-bold text-white/50 hover:text-white transition-colors uppercase">FR</a>
        </div>
        '''
        return f'<div class="hidden md:flex items-center justify-end gap-5" style="flex:1">{inner_content}{lang_selector}</div>'

    content = re.sub(nav_right_desktop, insert_lang_selector, content)
    
    # Save to EN
    with open(os.path.join('en', file), 'w', encoding='utf-8') as f:
        f.write(content)

# Copy EN to ES and FR
for file in html_files:
    en_file = os.path.join('en', file)
    shutil.copy(en_file, os.path.join('es', file))
    shutil.copy(en_file, os.path.join('fr', file))

print('File structure and basic layout created successfully.')
