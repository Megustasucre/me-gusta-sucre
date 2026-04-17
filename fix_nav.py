import os, re

html_files = ['index.html', 'guia.html', 'cafe.html', 'clases.html', 'hospedaje.html', 'merchandising.html', 'contacto.html']
folders = ['en', 'es', 'fr']

for folder in folders:
    for file in html_files:
        filepath = os.path.join(folder, file)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine active styles
        act_en = 'text-gray-900' if folder == 'en' else 'text-gray-400 hover:text-gray-900'
        act_es = 'text-gray-900' if folder == 'es' else 'text-gray-400 hover:text-gray-900'
        act_fr = 'text-gray-900' if folder == 'fr' else 'text-gray-400 hover:text-gray-900'
        
        mobile_lang = f'''
      <!-- Mobile Language Selector -->
      <div class="py-4 mt-2 border-t border-b border-gray-100 relative mb-4">
        <p class="text-[10px] font-bold text-gray-400 mb-3 uppercase tracking-wider">Language / Idioma</p>
        <div class="flex items-center gap-5">
          <a href="../en/{file}" class="text-sm font-bold {act_en} transition-colors">EN</a>
          <span class="text-gray-300">|</span>
          <a href="../es/{file}" class="text-sm font-bold {act_es} transition-colors">ES</a>
          <span class="text-gray-300">|</span>
          <a href="../fr/{file}" class="text-sm font-bold {act_fr} transition-colors">FR</a>
        </div>
      </div>
      '''
      
        # Inject just before the CTA btn-red in the mobile menu, or if not found, before </div> of mobile menu
        # Look for the last link before the CTA
        match = re.search(r'(<a href="[^"]*" class="btn-red block text-center mt-4">[^<]*</a>)', content)
        if match:
            # Check if it was already injected
            if "<!-- Mobile Language Selector -->" not in content:
                content = content.replace(match.group(1), mobile_lang + match.group(1))
        
        # Make sure desktop selector visually indicates which language is active for better UX
        # Current pattern: class="text-xs font-bold text-white hover:text-white/70 transition-colors uppercase"
        if folder == 'en':
             content = content.replace('href="../en/' + file + '" class="text-xs font-bold text-white/50 hover:text-white', 'href="../en/' + file + '" class="text-xs font-bold text-white hover:text-white/70')
             content = content.replace('href="../es/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../es/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
             content = content.replace('href="../fr/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../fr/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
        elif folder == 'es':
             content = content.replace('href="../en/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../en/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
             content = content.replace('href="../es/' + file + '" class="text-xs font-bold text-white/50 hover:text-white', 'href="../es/' + file + '" class="text-xs font-bold text-white hover:text-white/70')
             content = content.replace('href="../fr/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../fr/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
        elif folder == 'fr':
             content = content.replace('href="../en/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../en/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
             content = content.replace('href="../es/' + file + '" class="text-xs font-bold text-white hover:text-white/70', 'href="../es/' + file + '" class="text-xs font-bold text-white/50 hover:text-white')
             content = content.replace('href="../fr/' + file + '" class="text-xs font-bold text-white/50 hover:text-white', 'href="../fr/' + file + '" class="text-xs font-bold text-white hover:text-white/70')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
print("Updated all mobile and desktop selectors.")
