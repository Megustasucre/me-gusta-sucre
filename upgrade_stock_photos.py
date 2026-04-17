import os
import re

# Mapping of current generic IDs -> target high-end IDs
# Keys are the partial IDs currently in the HTML
replacements = {
    # Inn / Hospedaje
    "photo-1611892440504-42a792e24d32": "photo-1542314831-068cd1dbfeeb", # Hero patio
    "photo-1566665797739-1674de7a421a": "photo-1618773928121-c32242e63f39", # Suite Colonial
    "photo-1590490359683-658d3d23f972": "photo-1566665797739-1674de7a421a", # Patio Room
    "photo-1582719478250-c89cae4dc85b": "photo-1611892440504-42a792e24d32", # Standard Room
    "photo-1555854877-bab0e564b8d5": "photo-1555854877-bab0e564b8d5", # Shared Dorm (already good)
    
    # Café
    "photo-1554118811-1e0d58224f24": "photo-1521017432531-fbd92d744264", # Café urban cozy hero
    "photo-1528736235302-52922df5c122": "photo-1528736235302-52922df5c122", # Panino (keep)
    "photo-1601050690597-df0568f70950": "photo-1601050690597-df0568f70950", # Esfirra (keep)
    "photo-1586788224331-947f68671cf1": "photo-1586788224331-947f68671cf1", # Cake (keep)
    
    # Spanish School
    "photo-1517048676732-d65bc937f952": "photo-1517048676732-d65bc937f952", # Meeting (keep)
    "photo-1524178232363-1fb2b075b655": "photo-1517245386807-bb43f82c33c4", # School interaction
    
    # Merch
    "photo-1523906834658-6e24ef2386f9": "photo-1441984904996-e0b6ba687e04", # Merch Hero
}

# Common parameters for optimization
PARAMS = "&fm=webp&q=78&auto=format"

def upgrade_line(match):
    url = match.group(0)
    # Extract ID
    id_match = re.search(r'photo-([a-z0-9-]+)', url)
    if id_match:
        old_id = id_match.group(0)
        new_id = replacements.get(old_id, old_id) # Replace if in map
        
        # Strip existing params and rebuild
        base = url.split('?')[0].replace('"', '')
        base = base.replace(old_id, new_id)
        
        # Special width handling
        w = "1200"
        if "w=" in url:
            w_match = re.search(r'w=([0-9]+)', url)
            if w_match: w = w_match.group(1)
            
        return f'"{base}?w={w}{PARAMS}"'
    return url

base_dir = r"c:\pagina-web\me-gusta-sucre"
langs = ['en', 'es', 'fr']

for lang in langs:
    for root, _, files in os.walk(os.path.join(base_dir, lang)):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace img src and url() matches
                # Normalize double quotes first
                content = re.sub(r'"https://images\.unsplash\.com/[^"]+"', upgrade_line, content)
                content = re.sub(r"'https://images\.unsplash\.com/[^']+'", lambda m: upgrade_line(m).replace('"', "'"), content)
                
                # Fix the specific quote bug in CSS url("'...'")
                content = content.replace("url(\"'", "url('").replace("'\")", "')")
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Upgraded images in {path}")
