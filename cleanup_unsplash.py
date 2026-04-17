import os
import re

base_dir = r"c:\pagina-web\me-gusta-sucre"

def cleanup_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the double nested quotes and duplicated params in url()
    # url(''https://...&fm=webp&q=78&auto=format'&fm=webp&q=60&auto=format")
    content = re.sub(
        r"url\(''([^']+)&fm=webp&q=60&auto=format'\)",
        r"url('\1')",
        content
    )
    
    # Check for cases where my fix earlier might have left slightly different debris
    # Like index.html: <img src="https://images.unsplash.com/photo-...?w=500&fm=webp&q=78&auto=format&fm=webp&q=60&auto=format"
    content = re.sub(r'(&fm=webp&q=60&auto=format)+', '&fm=webp&q=60&auto=format', content)
    content = content.replace('&fm=webp&q=78&auto=format&fm=webp&q=60&auto=format', '&fm=webp&q=75&auto=format')
    
    # Fix the specific quote mess in hospedaje hero
    content = content.replace("url(''https", "url('https").replace("format')", "format')")
    
    # General cleanup of double quote strings to single URL
    content = re.sub(r'src="https://images\.unsplash\.com/([^"]+)&fm=webp&q=60&auto=format"', 
                     r'src="https://images.unsplash.com/\1&fm=webp&q=75&auto=format"', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

for root, _, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            cleanup_file(p)
            print(f"Cleaned {p}")
