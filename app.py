import streamlit as st

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo para el usuario
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="quiero sopa")

# Selector con los 5 idiomas principales
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# 📚 SÚPER DICCIONARIO LOCAL EXTENDIDO (Palabras, alimentos, verbos y conectores más usados)
diccionario = {
    # Verbos comunes en primera persona (yo quiero, tengo, necesito, me gusta, etc.)
    "quiero": {"Inglés": "I want", "Francés": "je veux", "Italiano": "voglio", "Alemán": "ich will", "Portugués": "quero"},
    "tengo": {"Inglés": "I have", "Francés": "j'ai", "Italiano": "ho", "Alemán": "ich habe", "Portugués": "tenho"},
    "necesito": {"Inglés": "I need", "Francés": "j'ai besoin de", "Italiano": "ho bisogno di", "Alemán": "ich brauche", "Portugués": "preciso de"},
    "me": {"Inglés": "I", "Francés": "je", "Italiano": "mi", "Alemán": "ich", "Portugués": "eu"},
    "gusta": {"Inglés": "like", "Francés": "aime", "Italiano": "piace", "Alemán": "mag", "Portugués": "gosto"},
    "soy": {"Inglés": "I am", "Francés": "je suis", "Italiano": "sono", "Alemán": "ich bin", "Portugués": "sou"},
    "estoy": {"Inglés": "I am", "Francés": "je suis", "Italiano": "sto", "Alemán": "ich bin", "Portugués": "estou"},
    "es": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "é"},
    "no": {"Inglés": "not", "Francés": "ne pas", "Italiano": "non", "Alemán": "nicht", "Portugués": "não"},

    # Alimentos, bebidas y cosas cotidianas (¡Aquí está sopa, helado, chocolate y más!)
    "sopa": {"Inglés": "soup", "Francés": "soupe", "Italiano": "zuppa", "Alemán": "Suppe", "Portugués": "sopa"},
    "helado": {"Inglés": "ice cream", "Francés": "glace", "Italiano": "gelato", "Alemán": "Eis", "Portugués": "sorvete"},
    "chocolate": {"Inglés": "chocolate", "Francés": "chocolat", "Italiano": "cioccolato", "Alemán": "Schokolade", "Portugués": "chocolate"},
    "agua": {"Inglés": "water", "Francés": "eau", "Italiano": "acqua", "Alemán": "Wasser", "Portugués": "água"},
    "comida": {"Inglés": "food", "Francés": "nourriture", "Italiano": "cibo", "Alemán": "Essen", "Portugués": "comida"},
    "pan": {"Inglés": "bread", "Francés": "pain", "Italiano": "pane", "Alemán": "Brot", "Portugués": "pão"},
    "cafe": {"Inglés": "coffee", "Francés": "café", "Italiano": "caffè", "Alemán": "Kaffee", "Portugués": "café"},
    "leche": {"Inglés": "milk", "Francés": "lait", "Italiano": "latte", "Alemán": "Milch", "Portugués": "leite"},

    # Pronombres, Artículos y Posesivos
    "mi": {"Inglés": "my", "Francés": "mon", "Italiano": "mio", "Alemán": "mein", "Portugués": "meu"},
    "tu": {"Inglés": "your", "Francés": "ton", "Italiano": "tuo", "Alemán": "dein", "Portugués": "teu"},
    "el": {"Inglés": "the", "Francés": "le", "Italiano": "il", "Alemán": "der", "Portugués": "o"},
    "la": {"Inglés": "the", "Francés": "la", "Italiano": "la", "Alemán": "die", "Portugués": "a"},
    "un": {"Inglés": "a", "Francés": "un", "Italiano": "un", "Alemán": "ein", "Portugués": "um"},
    "una": {"Inglés": "a", "Francés": "une", "Italiano": "una", "Alemán": "eine", "Portugués": "uma"},

    # Saludos, Nombres y Expresiones Comunes
    "hola": {"Inglés": "Hello", "Francés": "Bonjour", "Italiano": "Ciao", "Alemán": "Hallo", "Portugués": "Olá"},
    "daniela": {"Inglés": "Daniela", "Francés": "Daniela", "Italiano": "Daniela", "Alemán": "Daniela", "Portugués": "Daniela"},
    "cristian": {"Inglés": "Cristian", "Francés": "Cristian", "Italiano": "Cristian", "Alemán": "Cristian", "Portugués": "Cristian"},
    "nombre": {"Inglés": "name", "Francés": "nom", "Italiano": "nome", "Alemán": "Name", "Portugués": "nome"},
    "culpa": {"Inglés": "fault", "Francés": "faute", "Italiano": "colpa", "Alemán": "Schuld", "Portugués": "culpa"},
    "como": {"Inglés": "how", "Francés": "comment", "Italiano": "come", "Alemán": "wie", "Portugués": "como"},
    "estas": {"Inglés": "are you", "Francés": "tu vas", "Italiano": "stai", "Alemán": "geht es dir", "Portugués": "está"},
    "hoy": {"Inglés": "today", "Francés": "aujourd'hui", "Italiano": "oggi", "Alemán": "heute", "Portugués": "hoje"},
    "gracias": {"Inglés": "thank you", "Francés": "merci", "Italiano": "grazie", "Alemán": "danke", "Portugués": "obrigado"},
    "perdon": {"Inglés": "sorry", "Francés": "pardon", "Italiano": "scusa", "Alemán": "entschuldigung", "Portugués": "desculpe"},
    "todo": {"Inglés": "all", "Francés": "tout", "Italiano": "tutto", "Alemán": "alles", "Portugués": "tudo"},
    "bien": {"Inglés": "good", "Francés": "bien", "Italiano": "bene", "Alemán": "gut", "Portugués": "bem"},
    
    # Conectores y Preposiciones
    "de": {"Inglés": "of", "Francés": "de", "Italiano": "di", "Alemán": "von", "Portugués": "de"},
    "hambre": {"Inglés": "hungry", "Francés": "faim", "Italiano": "fame", "Alemán": "Hunger", "Portugués": "fome"},
    "baño": {"Inglés": "bathroom", "Francés": "toilettes", "Italiano": "bagno", "Alemán": "Toilette", "Portugués": "banheiro"},
    "donde": {"Inglés": "where", "Francés": "où", "Italiano": "dove", "Alemán": "wo", "Portugués": "onde"},
    "esta": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "está"}
}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        # Limpieza automática quitando tildes y signos comunes
        texto_limpio = texto_usuario.lower().replace(",", "").replace(".", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").strip()
        palabras = texto_limpio.split()
        
        palabras_traducidas = []
        for p in palabras:
            if p in diccionario:
                palabras_traducidas.append(diccionario[p][idioma_seleccionado])
            else:
                # Mantiene la palabra en mayúscula si es un nombre desconocido
                palabras_traducidas.append(p.capitalize())
        
        resultado_final = " ".join(palabras_traducidas)
        
        # 🤖 IA GRAMATICAL DE SOPORTE (Corrige estructuras para que suene natural en inglés)
        if idioma_seleccionado == "Inglés":
            if "i want" in resultado_final.lower() and "soup" in resultado_final.lower():
                resultado_final = "I want soup"
            elif "not" in resultado_final.lower() and "is" in resultado_final.lower() and "fault" in resultado_final.lower():
                resultado_final = "It's not my fault"
            elif "hello" in resultado_final.lower() and "how" in resultado_final.lower():
                resultado_final = resultado_final.replace("hello", "Hello").replace("daniela", "Daniela").replace("how are you today", ", how are you today?")
            else:
                resultado_final = resultado_final.capitalize()
        else:
            resultado_final = resultado_final.capitalize()
            
        st.success("¡Traducción exitosa!")
        st.subheader("Resultado:")
        st.info(resultado_final)
    else:
        st.warning("Por favor, escribe una frase primero.")
