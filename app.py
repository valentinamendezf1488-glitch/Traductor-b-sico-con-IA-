import streamlit as st

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo para el usuario
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Como estas")

# Selector con los 5 idiomas principales
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# 📚 BASE DE DATOS DE FRASES ESTRUCTURADAS UNIFICADA (¡Con tus nuevas peticiones!)
base_frases = {
    # Nuevas frases solicitadas por Daniela
    "como estas": {
        "Inglés": "How are you?", "Francés": "Comment ça va?", 
        "Italiano": "Come stai?", "Alemán": "Wie geht es dir?", "Portugués": "Como você está?"
    },
    "como te ha ido": {
        "Inglés": "How has it been going?", "Francés": "Comment ça s'est passé?", 
        "Italiano": "Come ti va?", "Alemán": "Wie es dir ergangen ist?", "Portugués": "Como tem pasado?"
    },
    "todo bien": {
        "Inglés": "All good / Everything is fine", "Francés": "Tout va bien", 
        "Italiano": "Tutto bene", "Alemán": "Alles gut", "Portugués": "Tudo bem"
    },
    "gracias": {
        "Inglés": "Thank you", "Francés": "Merci", 
        "Italiano": "Grazie", "Alemán": "Danke", "Portugués": "Obrigado"
    },
    "perdon": {
        "Inglés": "Sorry / Excuse me", "Francés": "Pardon / Désolé", 
        "Italiano": "Scusa / Perdono", "Alemán": "Entschuldigung", "Portugués": "Desculpe / Perdão"
    },

    # Expresiones de Disculpa y Sentimientos anteriores
    "no es mi culpa": {
        "Inglés": "It's not my fault", "Francés": "Ce n'est pas de ma faute", 
        "Italiano": "Non es colpa mia", "Alemán": "Es ist nicht meine Schuld", "Portugués": "Não é minha culpa"
    },
    "lo siento mucho": {
        "Inglés": "I am so sorry", "Francés": "Je suis vraiment désolé", 
        "Italiano": "Mi dispiace molto", "Alemán": "Es tut mir sehr leid", "Portugués": "Sinto muito"
    },
    "no te preocupes": {
        "Inglés": "Don't worry", "Francés": "Ne t'inquiète pas", 
        "Italiano": "Non ti preoccupare", "Alemán": "Mach dir keine Sorgen", "Portugués": "Não se preocupe"
    },
    
    # Presentaciones y Saludos cotidianos
    "hola mi nombre es daniela": {
        "Inglés": "Hello, my name is Daniela", "Francés": "Bonjour, je m'appelle Daniela", 
        "Italiano": "Ciao, mi chiamo Daniela", "Alemán": "Hallo, mein Name ist Daniela", "Portugués": "Olá, meu nome é Daniela"
    },
    "hola mi nombre es cristian": {
        "Inglés": "Hello, my name is Cristian", "Francés": "Bonjour, je m'appelle Cristian", 
        "Italiano": "Ciao, mi chiamo Cristian", "Alemán": "Hallo, mein Name ist Cristian", "Portugués": "Olá, meu nome é Cristian"
    },
    "buenos dias como estas": {
        "Inglés": "Good morning, how are you?", "Francés": "Bonjour, comment ça va?", 
        "Italiano": "Buongiorno, come stai?", "Alemán": "Guten Morgen, wie geht es dir?", "Portugués": "Bom dia, como você está?"
    },
    "mucho gusto en conocerte": {
        "Inglés": "Nice to meet you", "Francés": "Enchanté de vous rencontrer", 
        "Italiano": "Piacere di conoscerti", "Alemán": "Freut mich, dich kennenzulernen", "Portugués": "Muito prazer en conhecê-lo"
    },
    
    # Gustos y canciones
    "hola mi cancion favorita es lola la vaca": {
        "Inglés": "Hello, my favorite song is Lola the cow", "Francés": "Bonjour, ma chanson préférée est Lola la vache", 
        "Italiano": "Ciao, la mia canzone preferita è Lola la mucca", "Alemán": "Hallo, mein Lieblingslied ist Lola die Kuh", "Portugués": "Olá, minha música favorita é Lola a vaca"
    },
    "me gusta el helado de chocolate": {
        "Inglés": "I like chocolate ice cream", "Francés": "J'aime la glace au chocolat", 
        "Italiano": "Mi piace il gelato al cioccolato", "Alemán": "Ich mag Schokoladeneis", "Portugués": "Eu gosto de sorvete de chocolate"
    },
    
    # Necesidad y Ayuda
    "donde esta el baño": {
        "Inglés": "Where is the bathroom?", "Francés": "Où sont les toilettes?", 
        "Italiano": "Dov'è il bagno?", "Alemán": "Wo ist die Toilette?", "Portugués": "Onde fica o banheiro?"
    }
}

# 📖 Diccionario complementario palabra por palabra
diccionario_palabras = {
    "hola": {"Inglés": "Hello", "Francés": "Bonjour", "Italiano": "Ciao", "Alemán": "Hallo", "Portugués": "Olá"},
    "no": {"Inglés": "no", "Francés": "non", "Italiano": "no", "Alemán": "nein", "Portugués": "não"},
    "es": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "é"},
    "mi": {"Inglés": "my", "Francés": "mon", "Italiano": "mio", "Alemán": "mein", "Portugués": "meu"},
    "culpa": {"Inglés": "fault", "Francés": "faute", "Italiano": "colpa", "Alemán": "Schuld", "Portugués": "culpa"},
    "adios": {"Inglés": "goodbye", "Francés": "au revoir", "Italiano": "arrivederci", "Alemán": "auf Wiedersehen", "Portugués": "adeus"}
}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        # Limpieza estándar eliminando acentos/tildes para evitar fallas al escribir
        texto_limpio = texto_usuario.lower().replace(",", "").replace(".", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").strip()
        
        # 1. Buscar frase exacta
        if texto_limpio in base_frases:
            resultado_final = base_frases[texto_limpio][idioma_seleccionado]
            st.success("¡Traducción Inteligente Exitosa!")
            st.info(resultado_final)
            
        # 2. Armar palabra por palabra si es compuesta
        else:
            palabras = texto_limpio.split()
            traduccion_armada = []
            for p in palabras:
                if p in diccionario_palabras:
                    traduccion_armada.append(diccionario_palabras[p][idioma_seleccionado])
                else:
                    traduccion_armada.append(p)
            
            resultado_final = " ".join(traduccion_armada).capitalize()
            st.success("¡Traducción Modular Exitosa!")
            st.info(resultado_final)
    else:
        st.warning("Por favor, escribe una frase primero.")
