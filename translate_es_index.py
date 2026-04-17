import re

with open('es/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

translations = {
    # Head
    "Discover Bolivia's White City": "Descubre la Ciudad Blanca de Bolivia",
    "Experience Sucre — Bolivia's UNESCO World Heritage city. Spanish classes, boutique inn, specialty coffee, and unforgettable activities in the heart of the White City.": "Experimenta Sucre — la ciudad Patrimonio de la Humanidad de Bolivia. Clases de español, posada boutique, café de especialidad y actividades inolvidables en el corazón de la Ciudad Blanca.",
    "Experience Sucre — the heart of Bolivia. Colonial architecture, UNESCO heritage, Spanish classes, local cuisine and warm hospitality.": "Experimenta Sucre — el corazón de Bolivia. Arquitectura colonial, patrimonio de la UNESCO, clases de español, gastronomía local y cálida hospitalidad.",
    
    # Top bar
    "Complete your Sucre Experience: Stay at our Boutique Inn &amp; Learn Spanish with native teachers.": "Completa tu Experiencia en Sucre: Alójate en nuestra Posada Boutique y Aprende Español con profesores nativos.",
    "See Spanish Classes": "Ver Clases de Español",
    
    # Nav
    ">Spanish Classes<": ">Clases de Español<",
    ">Café<": ">Café<",
    ">City Guide<": ">Guía de la Ciudad<",
    ">Stay<": ">Hospedaje<",
    ">Contact<": ">Contacto<",
    ">Book a Stay<": ">Reservar<",
    
    # Hero
    "La Ciudad Blanca": "La Ciudad Blanca",
    "Discover<br/><span style=\"color:#c9252d;font-style:italic\">Sucre</span>": "Descubre<br/><span style=\"color:#c9252d;font-style:italic\">Sucre</span>",
    "Bolivia's constitutional capital and UNESCO World Heritage city. A place of colonial beauty, vibrant culture, and warm people — waiting to be discovered.": "Capital constitucional de Bolivia y Patrimonio de la Humanidad. Un lugar de belleza colonial, cultura vibrante y gente cálida — esperando ser descubierto.",
    "Book Your Stay": "Reserva tu Estadía",
    "Altitude": "Altitud",
    "Independence": "Independencia",
    "World Heritage": "Patrimonio de la Humanidad",
    "Avg. Climate": "Clima Promedio",
    
    # Ticker
    "THE WHITE CITY OF BOLIVIA": "LA CIUDAD BLANCA DE BOLIVIA",
    "UNESCO WORLD HERITAGE SINCE 1991": "PATRIMONIO DE LA HUMANIDAD DESDE 1991",
    "CONSTITUTIONAL CAPITAL OF BOLIVIA": "CAPITAL CONSTITUCIONAL DE BOLIVIA",
    "DINOSAUR FOOTPRINTS · CAL ORCKO": "HUELLAS DE DINOSAURIO · CAL ORCKO",
    "SPANISH CLASSES · BOUTIQUE INN · CAFÉ": "CLASES DE ESPAÑOL · POSADA BOUTIQUE · CAFÉ",
    
    # Why Sucre
    "Why Sucre?": "¿Por qué Sucre?",
    "Bolivia's<br/><span class=\"accent\">Most Beautiful</span><br/>City": "La Ciudad<br/><span class=\"accent\">Más Hermosa</span><br/>de Bolivia",
    "Sucre is a city frozen in time — in the best possible way. Its gleaming white colonial buildings, broad plazas, and baroque churches earned it a UNESCO World Heritage designation in 1991. But it's more than just beautiful architecture.": "Sucre es una ciudad detenida en el tiempo, en el mejor sentido posible. Sus relucientes edificios coloniales blancos, amplias plazas e iglesias barrocas le valieron la designación como Patrimonio de la Humanidad en 1991. Pero es más que una hermosa arquitectura.",
    "At 2,810 meters above sea level, Sucre enjoys a mild, spring-like climate year-round. The city blends indigenous traditions with Spanish colonial heritage, creating a cultural richness that's impossible to find anywhere else.": "A 2.810 metros sobre el nivel del mar, Sucre disfruta de un clima templado y primaveral todo el año. La ciudad mezcla tradiciones indígenas con la herencia colonial española, creando una riqueza cultural imposible de encontrar en otro lugar.",
    "Spring Climate": "Clima Primaveral",
    "Founded 1538": "Fundada en 1538",
    
    # Attractions
    "Must See": "Imperdibles",
    "Top <span class=\"accent\">Attractions</span>": "Principales <span class=\"accent\">Atracciones</span>",
    "From ancient dinosaur footprints to breathtaking viewpoints — Sucre never disappoints.": "Desde antiguas huellas de dinosaurio hasta vistas impresionantes: Sucre nunca decepciona.",
    "City Center": "Centro Histórico",
    "The heart of Sucre. Colonial buildings surround this grand plaza where locals gather, history lives, and the Cathedral towers above.": "El corazón de Sucre. Edificios coloniales rodean esta gran plaza donde los locales se reúnen, la historia vive y la Catedral se alza.",
    "Explore →": "Explorar →",
    "Unique": "Único",
    "Cal Orcko Dinosaurs": "Dinosaurios en Cal Orcko",
    "Home to the world's largest collection of dinosaur footprints — over 5,000 tracks from 294 species on a single limestone wall.": "Hogar de la mayor colección de huellas de dinosaurio del mundo: más de 5.000 rastros de 294 especies en una sola pared de piedra caliza.",
    "Viewpoint": "Mirador",
    "A 16th-century convent perched on a hill with panoramic views over Sucre's white rooftops. The best sunset spot in the city.": "Un convento del siglo XVI situado en una colina con vistas panorámicas de los tejados blancos de Sucre. El mejor atardecer de la ciudad.",
    "Open City Guide": "Abrir Guía de la Ciudad",
    
    # Cafe
    "Coffee &amp; Good Food<br/><span style=\"color:#c9252d;font-style:italic\">in the Heart of Sucre</span>": "Café y Buena Comida<br/><span style=\"color:#c9252d;font-style:italic\">en el Corazón de Sucre</span>",
    "Start your morning with a Bolivian espresso and homemade pastries on our colonial patio. Me Gusta Café is where locals and travelers meet — relaxed, warm, and genuinely good.": "Empieza tu mañana con un espresso boliviano y bollería casera en nuestro patio colonial. Me Gusta Café es donde locales y viajeros se encuentran — un lugar relajado, cálido y auténtico.",
    "Open Mon–Sat 8am–8pm. Free WiFi, power outlets, vegetarian options, and a pet-friendly terrace at Bolivar #603 — steps from the main plaza.": "Abierto Lun–Sáb de 8am–8pm. WiFi gratis, enchufes, opciones vegetarianas y terraza pet-friendly en Bolívar #603 — a pasos de la plaza principal.",
    "Bolivian Coffee": "Café Boliviano",
    "Pastries": "Repostería",
    "Free WiFi": "WiFi Gratis",
    "Colonial Patio": "Patio Colonial",
    "See the Menu": "Ver el Menú",
    
    # Spanish School
    "Learn Spanish<br/><span style=\"color:#c9252d;font-style:italic\">While You Travel</span>": "Aprende Español<br/><span style=\"color:#c9252d;font-style:italic\">Mientras Viajas</span>",
    "Sucre is one of the best cities in South America to learn Spanish — the accent is neutral, the city is safe, and life here moves at the right pace for language learning.": "Sucre es una de las mejores ciudades de Sudamérica para aprender español: el acento es neutro, la ciudad es segura y la vida transcurre al ritmo perfecto para aprender.",
    "Me Gusta Spanish offers private, duo, and group programs with native Bolivian teachers. One week or several months — every class is planned around you.": "Me Gusta Spanish ofrece programas privados, en pareja y grupales con profesores nativos bolivianos. Una semana o varios meses: tú decides el ritmo.",
    "Students": "Estudiantes",
    "Countries": "Países",
    "Programs": "Programas",
    "See All Courses": "Ver Todos los Cursos",
    "School Website ↗": "Web de la Escuela ↗",
    
    # Brands
    "Stay, Eat, <span class=\"accent\">Learn</span> &amp; Shop": "Hospedaje, Café, <span class=\"accent\">Clases</span> y Tienda",
    "Four experiences in the heart of Sucre, designed for travelers who want more than just a hotel.": "Cuatro experiencias en el corazón de Sucre, diseñadas para viajeros que buscan más que un hotel.",
    "Native Bolivian teachers, 750+ students from 50+ countries. Face-to-face &amp; online.": "Profesores nativos de Bolivia, más de 750 estudiantes de 50 países. Presencial y online.",
    "See Courses →": "Ver Cursos →",
    "A cozy boutique inn in the historic district. Personal service, the best location in Sucre.": "Una acogedora posada boutique en el distrito histórico. Servicio personalizado en la mejor ubicación.",
    "Book a Room →": "Reservar Habitación →",
    "Bolivian coffee, homemade pastries, and a colonial patio. Open Mon–Sat 8am–8pm.": "Café boliviano, repostería casera y un patio colonial. Abierto Lun–Sáb de 8am a 8pm.",
    "See the Menu →": "Ver el Menú →",
    "T-shirts, tote bags, mugs, and more. Take a piece of Sucre home with you.": "Camisetas, ecobolsas, tazas y más. Llévate un pedazo de Sucre a casa contigo.",
    "Shop Now →": "Comprar Ahora →",
    
    # CTA Banner
    "Come visit us": "Ven a visitarnos",
    "Your Sucre Adventure<br/>Starts Here": "Tu Aventura en Sucre<br/>Comienza Aquí",
    "Book your stay, plan your visit, or sign up for Spanish classes — we're here to make your Sucre experience unforgettable.": "Reserva tu hospedaje, planifica tu visita o regístrate en clases de español. Estamos aquí para que tu experiencia sea inolvidable.",
    "Contact Us": "Contáctanos",
    
    # Footer
    "Your gateway to Bolivia's most beautiful city — Spanish classes, boutique inn, café, and city experiences.": "Tu puerta de entrada a la ciudad más hermosa de Bolivia — clases de español, posada boutique, café y experiencias urbanas.",
    "Explore</p>": "Explorar</p>",
    ">Café &amp; Menu<": ">Café y Menú<",
    "Me Gusta</p>": "Me Gusta</p>",
    ">Inn — Boutique Hotel<": ">Posada — Hotel Boutique<",
    ">Find Us</p>": ">Encuéntranos</p>",
    "All rights reserved.": "Todos los derechos reservados."
}

for eng, spa in translations.items():
    text = text.replace(eng, spa)

with open('es/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Translated es/index.html")
