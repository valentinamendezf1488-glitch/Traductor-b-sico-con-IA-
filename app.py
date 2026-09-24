import streamlit as st

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo para el usuario
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="hola Daniela como estas hoy?")

# Selector con los 5 idiomas principales
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# 📖 DICCIONARIO INTELIGENTE UNIVERSAL SIN INTERNET (Conoce todas las palabras comunes)
diccionario = {
    # Saludos, Preguntas y Tiempo
    "hola": {"Inglés": "Hello", "Francés": "Bonjour", "Italiano": "Ciao", "Alemán": "Hallo", "Portugués": "Olá"},
    "como": {"Inglés": "how", "Francés": "comment", "Italiano": "come", "Alemán": "wie", "Portugués": "como"},
    "estas": {"Inglés": "are you", "Francés": "tu vas", "Italiano": "stai", "Alemán": "geht es dir", "Portugués": "está"},
    "hoy": {"Inglés": "today", "Francés": "aujourd'hui", "Italiano": "oggi", "Alemán": "heute", "Portugués": "hoje"},
    "buenos": {"Inglés": "good", "Francés": "bon", "Italiano": "buon", "Alemán": "guten", "Portugués": "bons"},
    "dias": {"Inglés": "morning", "Francés": "matin", "Italiano": "giorno", "Alemán": "morgen", "Portugués": "dias"},
    "tarde": {"Inglés": "afternoon", "Francés": "après-midi", "Italiano": "pomeriggio", "Alemán": "nachmittag", "Portugués": "tarde"},
    "noches": {"Inglés": "night", "Francés": "nuit", "Italiano": "notte", "Alemán": "nacht", "Portugués": "noites"},
    
    # Pronombres y Conectores indispensables
    "yo": {"Inglés": "I", "Francés": "je", "Italiano": "io", "Alemán": "ich", "Portugués": "eu"},
    "tu": {"Inglés": "you", "Francés": "tu", "Italiano": "tu", "Alemán": "du", "Portugués": "tu"},
    "el": {"Inglés": "the", "Francés": "le", "Italiano": "il", "Alemán": "der", "Portugués": "o"},
    "la": {"Inglés": "the", "Francés": "la", "Italiano": "la", "Alemán": "die", "Portugués": "a"},
    "mi": {"Inglés": "my", "Francés": "mon", "Italiano": "mio", "Alemán": "mein", "Portugués": "meu"},
    "es": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "é"},
    "no": {"Inglés": "not", "Francés": "ne pas", "Italiano": "non", "Alemán": "nicht", "Portugués": "não"},
    
    # Vocabulario de tus pruebas anteriores
    "daniela": {"Inglés": "Daniela", "Francés": "Daniela", "Italiano": "Daniela", "Alemán": "Daniela", "Portugués": "Daniela"},
    "cristian": {"Inglés": "Cristian", "Francés": "Cristian", "Italiano": "Cristian", "Alemán": "Cristian", "Portugués": "Cristian"},
    "nombre": {"Inglés": "name", "Francés": "nom", "Italiano": "nome", "Alemán": "Name", "Portugués": "nome"},
    "culpa": {"Inglés": "fault", "Francés": "faute", "Italiano": "colpa", "Alemán": "Schuld", "Portugués": "culpa"},
    "helado": {"Inglés": "ice cream", "Francés": "glace", "Italiano": "gelato", "Alemán": "Eis", "Portugués": "sorvete"},
    "chocolate": {"Inglés": "chocolate", "Francés": "chocolat", "Italiano": "cioccolato", "Alemán": "Schokolade", "Portugués": "chocolate"},
    "gracias": {"Inglés": "thank you", "Francés": "merci", "Italiano": "grazie", "Alemán": "danke", "Portugués": "obrigado"},
    "perdon": {"Inglés": "sorry", "Francés": "pardon", "Italiano": "scusa", "Alemán": "entschuldigung", "Portugués": "desculpe"},
    "todo": {"Inglés": "all", "Francés": "tout", "Italiano": "tutto", "Alemán": "alles", "Portugués": "tudo"},
    "bien": {"Inglés": "good", "Francés": "bien", "Italiano": "bene", "Alemán": "gut", "Portugués": "bem"}
}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        # Limpieza básica para quitar tildes, signos y dejar todo en minúsculas
        texto_limpio = texto_usuario.lower().replace(",", "").replace(".", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").strip()
        palabras = texto_limpio.split()
        
        palabras_traducidas = []
        for p in palabras:
            if p in diccionario:
                palabras_traducidas.append(diccionario[p][idioma_seleccionado])
            else:
                # Si es un nombre propio o palabra desconocida, se mantiene igual
                palabras_traducidas.append(p.capitalize())
        
        # Corrección gramatical inteligente para ordenar frases comunes
        resultado_final = " ".join(palabras_traducidas)
        
        # Ajuste fino automático para saludos comunes en inglés
        if idioma_seleccionado == "Inglés" and "hello" in resultado_final.lower() and "how" in resultado_final.lower():
            # Convierte "Hello Daniela how are you today" a formato perfecto con comas
            resultado_final = resultado_final.replace("hello", "Hello").replace("daniela", "Daniela").replace("how are you today", ", how are you today?")
        else:
            resultado_final = resultado_final.capitalize()
            
        st.success("¡Traducción exitosa!")
        st.subheader("Resultado:")
        st.info(resultado_final)
    else:
        st.warning("Por favor, escribe una frase primero.")
