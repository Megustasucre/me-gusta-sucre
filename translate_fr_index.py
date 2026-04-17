import re

with open('fr/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

translations = {
    # Head
    "Discover Bolivia's White City": "Découvrez la Ville Blanche de Bolivie",
    "Experience Sucre — Bolivia's UNESCO World Heritage city. Spanish classes, boutique inn, specialty coffee, and unforgettable activities in the heart of the White City.": "Découvrez Sucre — la ville de Bolivie classée par l'UNESCO. Cours d'espagnol, auberge de charme, café de spécialité et activités inoubliables au cœur de la Ville Blanche.",
    "Experience Sucre — the heart of Bolivia. Colonial architecture, UNESCO heritage, Spanish classes, local cuisine and warm hospitality.": "Découvrez Sucre — le cœur de la Bolivie. Architecture coloniale, patrimoine de l'UNESCO, cours d'espagnol, cuisine locale et hospitalité chaleureuse.",
    
    # Top bar
    "Complete your Sucre Experience: Stay at our Boutique Inn &amp; Learn Spanish with native teachers.": "Complétez votre expèrience à Sucre: Séjournez dans notre Auberge Boutique et Apprenez l'espagnol avec des professeurs natifs.",
    "See Spanish Classes": "Voir les Cours d'Espagnol",
    
    # Nav
    ">Spanish Classes<": ">Cours d'Espagnol<",
    ">Café<": ">Café<",
    ">City Guide<": ">Guide de la Ville<",
    ">Stay<": ">Hébergement<",
    ">Contact<": ">Contact<",
    ">Book a Stay<": ">Réserver<",
    
    # Hero
    "La Ciudad Blanca": "La Ville Blanche",
    "Discover<br/><span style=\"color:#c9252d;font-style:italic\">Sucre</span>": "Découvrez<br/><span style=\"color:#c9252d;font-style:italic\">Sucre</span>",
    "Bolivia's constitutional capital and UNESCO World Heritage city. A place of colonial beauty, vibrant culture, and warm people — waiting to be discovered.": "Capitale constitutionnelle de la Bolivie et joyau patrimonial de l'UNESCO. Un lieu de beauté coloniale, de culture vibrante et de gens chaleureux — n'attend que d'être découvert.",
    "Book Your Stay": "Réservez votre Séjour",
    "Altitude": "Altitude",
    "Independence": "Indépendance",
    "World Heritage": "Patrimoine Mondial",
    "Avg. Climate": "Climat Moyen",
    
    # Ticker
    "THE WHITE CITY OF BOLIVIA": "LA VILLE BLANCHE DE BOLIVIE",
    "UNESCO WORLD HERITAGE SINCE 1991": "PATRIMOINE MONDIAL DE L'UNESCO DEPUIS 1991",
    "CONSTITUTIONAL CAPITAL OF BOLIVIA": "CAPITALE CONSTITUTIONNELLE DE LA BOLIVIE",
    "DINOSAUR FOOTPRINTS · CAL ORCKO": "EMPREINTES DE DINOSAURES · CAL ORCKO",
    "SPANISH CLASSES · BOUTIQUE INN · CAFÉ": "COURS D'ESPAGNOL · AUBERGE BOUTIQUE · CAFÉ",
    
    # Why Sucre
    "Why Sucre?": "Pourquoi Sucre ?",
    "Bolivia's<br/><span class=\"accent\">Most Beautiful</span><br/>City": "La Ville<br/><span class=\"accent\">La Plus Belle</span><br/>de Bolivie",
    "Sucre is a city frozen in time — in the best possible way. Its gleaming white colonial buildings, broad plazas, and baroque churches earned it a UNESCO World Heritage designation in 1991. But it's more than just beautiful architecture.": "Sucre est une ville figée dans le temps. Ses bâtiments coloniaux d'un blanc étincelant, ses vastes places et ses églises baroques lui ont valu d'être désignée au patrimoine mondial de l'UNESCO. Mais c'est bien plus qu'une belle architecture.",
    "At 2,810 meters above sea level, Sucre enjoys a mild, spring-like climate year-round. The city blends indigenous traditions with Spanish colonial heritage, creating a cultural richness that's impossible to find anywhere else.": "À 2 810 mètres d'altitude, Sucre bénéficie d'un climat printanier tout au long de l'année. La ville allie traditions indigènes et héritage colonial espagnol, créant une richesse culturelle inégalée.",
    "Spring Climate": "Climat Printanier",
    "Founded 1538": "Fondée en 1538",
    
    # Attractions
    "Must See": "À ne pas manquer",
    "Top <span class=\"accent\">Attractions</span>": "Principales <span class=\"accent\">Attractions</span>",
    "From ancient dinosaur footprints to breathtaking viewpoints — Sucre never disappoints.": "Des empreintes de dinosaures aux points de vue incomparables — Sucre ne déçoit jamais.",
    "City Center": "Centre Ville",
    "The heart of Sucre. Colonial buildings surround this grand plaza where locals gather, history lives, and the Cathedral towers above.": "Le cœur de Sucre. Des bâtiments coloniaux entourent cette grande place où l'histoire vit et la majestueuse cathédrale vous contemple.",
    "Explore →": "Explorer →",
    "Unique": "Unique",
    "Cal Orcko Dinosaurs": "Dinosaures à Cal Orcko",
    "Home to the world's largest collection of dinosaur footprints — over 5,000 tracks from 294 species on a single limestone wall.": "La plus grande collection d'empreintes de dinosaures au monde : plus de 5 000 traces sur une seule paroi calcaire.",
    "Viewpoint": "Point de Vue",
    "A 16th-century convent perched on a hill with panoramic views over Sucre's white rooftops. The best sunset spot in the city.": "Un couvent du XVIe siècle perché sur une colline avec des vues panoramiques sur les toits blancs de Sucre. Le meilleur endroit pour le coucher du soleil.",
    "Open City Guide": "Ouvrir le Guide de la Ville",
    
    # Cafe
    "Coffee &amp; Good Food<br/><span style=\"color:#c9252d;font-style:italic\">in the Heart of Sucre</span>": "Café et Bonne Cuisine<br/><span style=\"color:#c9252d;font-style:italic\">au Cœur de Sucre</span>",
    "Start your morning with a Bolivian espresso and homemade pastries on our colonial patio. Me Gusta Café is where locals and travelers meet — relaxed, warm, and genuinely good.": "Commencez votre journée par un espresso bolivien et nos pâtisseries maison dans notre charmant patio colonial. Un lieu de rencontre authentique.",
    "Open Mon–Sat 8am–8pm. Free WiFi, power outlets, vegetarian options, and a pet-friendly terrace at Bolivar #603 — steps from the main plaza.": "Ouvert Lun–Sam 8h–20h. WiFi gratuit, prises électriques, options végétariennes et terrasse aménagée, à quelques pas de la place principale.",
    "Bolivian Coffee": "Café Bolivien",
    "Pastries": "Pâtisseries",
    "Free WiFi": "WiFi Gratuit",
    "Colonial Patio": "Patio Colonial",
    "See the Menu": "Voir le Menu",
    
    # Spanish School
    "Learn Spanish<br/><span style=\"color:#c9252d;font-style:italic\">While You Travel</span>": "Apprenez L'espagnol<br/><span style=\"color:#c9252d;font-style:italic\">En Voyageant</span>",
    "Sucre is one of the best cities in South America to learn Spanish — the accent is neutral, the city is safe, and life here moves at the right pace for language learning.": "Sucre est l'une des meilleures villes d'Amérique du Sud pour l'apprentissage de la langue — l'accent y est neutre et la ville extrêmement sûre.",
    "Me Gusta Spanish offers private, duo, and group programs with native Bolivian teachers. One week or several months — every class is planned around you.": "Me Gusta Spanish propose des programmes privés et en groupe avec des professeurs natifs certifiés boliviens. ",
    "Students": "Étudiants",
    "Countries": "Pays",
    "Programs": "Programmes",
    "See All Courses": "Voir les Cours",
    "School Website ↗": "Site de l'école ↗",
    
    # Brands
    "Stay, Eat, <span class=\"accent\">Learn</span> &amp; Shop": "Dormir, Manger, <span class=\"accent\">Apprendre</span> et Acheter",
    "Four experiences in the heart of Sucre, designed for travelers who want more than just a hotel.": "Quatre activités au cœur de Sucre pour des voyageurs qui recherchent plus qu'un simple hôtel.",
    "Native Bolivian teachers, 750+ students from 50+ countries. Face-to-face &amp; online.": "Des enseignants boliviens natifs, plus de 750 étudiants de 50 pays. En face-à-face et en ligne.",
    "See Courses →": "Les Cours →",
    "A cozy boutique inn in the historic district. Personal service, the best location in Sucre.": "Une auberge de charme dans le quartier historique. Un service de prestige unique.",
    "Book a Room →": "Réserver une Chambre →",
    "Bolivian coffee, homemade pastries, and a colonial patio. Open Mon–Sat 8am–8pm.": "Café exclusif, pâtisseries et le charme d'un patio colonial. Heures : 8h–20h.",
    "See the Menu →": "Le Menu →",
    "T-shirts, tote bags, mugs, and more. Take a piece of Sucre home with you.": "T-shirts exclusifs, sacs intemporels, tasses. Emportez un de nos souvenirs mémorables de Sucre avec vous.",
    "Shop Now →": "Boutique en Ligne →",
    
    # CTA Banner
    "Come visit us": "Venez nous rendre visite",
    "Your Sucre Adventure<br/>Starts Here": "Votre Aventure à Sucre<br/>Commence Ici",
    "Book your stay, plan your visit, or sign up for Spanish classes — we're here to make your Sucre experience unforgettable.": "Réservez votre séjour, organisez votre visite ou enregistrez-vous à nos activités exclusivités. Nous sommes là pour que l'aventure soit incroyable.",
    "Contact Us": "Contactez-nous",
    
    # Footer
    "Your gateway to Bolivia's most beautiful city — Spanish classes, boutique inn, café, and city experiences.": "Votre porte d'entrée vers la magnifique ville de Bolivie — des écoles exclusives, des hébergements de qualité et expériences fantastiques.",
    "Explore</p>": "Explorer</p>",
    ">Café &amp; Menu<": ">Café et Menu<",
    "Me Gusta</p>": "Me Gusta</p>",
    ">Inn — Boutique Hotel<": ">Hébergement — Hôtel Boutique<",
    ">Find Us</p>": ">Nous Trouver</p>",
    "All rights reserved.": "Tous droits réservés."
}

for eng, text_fr in translations.items():
    text = text.replace(eng, text_fr)

with open('fr/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Translated fr/index.html")
