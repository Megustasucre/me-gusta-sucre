import os
import re

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize whitespace for easier replacement
    # Adding lang-container to the div
    content = re.sub(
        r'(<!-- Language Selector -->\s+<div class="flex items-center gap-3 border-l) (border-white/20 pl-6 ml-2">)',
        r'\1 lang-container \2',
        content
    )

    # Adding lang-btn and active class to links
    # Case 1: Active link (full text-white)
    content = re.sub(
        r'(class="text-xs font-bold text-white hover:text-white/70 transition-colors uppercase")',
        r'class="text-xs font-bold text-white lang-btn active hover:text-white/70 transition-colors uppercase"',
        content
    )
    
    # Case 2: Inactive link (text-white/50)
    content = re.sub(
        r'(class="text-xs font-bold text-white/50 hover:text-white transition-colors uppercase")',
        r'class="text-xs font-bold text-white/50 lang-btn hover:text-white transition-colors uppercase"',
        content
    )

    # Adding lang-sep to separators
    content = re.sub(
        r'<span class="text-white/30 text-xs">\|</span>',
        r'<span class="text-white/30 text-xs lang-sep">|</span>',
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = r"c:\pagina-web\me-gusta-sucre"
dirs = ['en', 'es', 'fr']

for d in dirs:
    dir_path = os.path.join(base_dir, d)
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.endswith('.html'):
                print(f"Fixing {d}/{f}...")
                fix_file(os.path.join(dir_path, f))
