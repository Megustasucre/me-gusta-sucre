import os

html_files = ['guia.html', 'cafe.html', 'clases.html', 'hospedaje.html', 'merchandising.html', 'contacto.html']

es_common = {
    ">Spanish Classes<": ">Clases de Español<",
    ">Café<": ">Café<",
    ">City Guide<": ">Guía de la Ciudad<",
    ">Stay<": ">Hospedaje<",
    ">Contact<": ">Contacto<",
    "Book a Stay": "Reservar Habitación",
    "Explore</p>": "Explorar</p>",
    ">Café &amp; Menu<": ">Café y Menú<",
    "Me Gusta</p>": "Me Gusta</p>",
    ">Inn — Boutique Hotel<": ">Posada — Hotel Boutique<",
    ">Find Us</p>": ">Encuéntranos</p>",
    "All rights reserved.": "Todos los derechos reservados.",
    "Come visit us": "Ven a visitarnos",
    "Contact Us": "Contáctanos",
    "Language / Idioma": "Idioma / Language"
}

fr_common = {
    ">Spanish Classes<": ">Cours d'Espagnol<",
    ">Café<": ">Café<",
    ">City Guide<": ">Guide de la Ville<",
    ">Stay<": ">Hébergement<",
    ">Contact<": ">Contact<",
    "Book a Stay": "Réserver",
    "Explore</p>": "Explorer</p>",
    ">Café &amp; Menu<": ">Café et Menu<",
    "Me Gusta</p>": "Me Gusta</p>",
    ">Inn — Boutique Hotel<": ">Hébergement — Hôtel Boutique<",
    ">Find Us</p>": ">Nous Trouver</p>",
    "All rights reserved.": "Tous droits réservés.",
    "Come visit us": "Venez nous rendre visite",
    "Contact Us": "Contactez-nous",
    "Language / Idioma": "Langue / Language"
}

def translate_files(folder, trans_dict):
    for file in html_files:
        filepath = os.path.join(folder, file)
        if not os.path.exists(filepath): continue
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        for eng, trans in trans_dict.items():
            content = content.replace(eng, trans)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

translate_files('es', es_common)
translate_files('fr', fr_common)

print("Common UI translated successfully")
