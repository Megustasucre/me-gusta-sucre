import os
import re

base_dir = r"c:\pagina-web\me-gusta-sucre"

def final_fix(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The specific mess: url('https://...format'&fm=webp&q=60&auto=format")
    # Should be: url('https://...format')
    content = re.sub(
        r"url\('([^']+)'&fm=webp&q=60&auto=format\"\)",
        r"url('\1')",
        content
    )
    
    # Also this possible variant: url('https://...format'&fm=webp&q=60&auto=format')
    content = re.sub(
        r"url\('([^']+)'&fm=webp&q=60&auto=format'\)",
        r"url('\1')",
        content
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            final_fix(p)
            print(f"Final Fix in {p}")
