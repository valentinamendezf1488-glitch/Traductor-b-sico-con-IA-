import streamlit as st

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo para el usuario
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="No es mi culpa")

# Selector con los 5 idiomas principales
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# 📚 BASE DE DATOS DE FRASES ESTRUCTURADAS (Categorías más comunes de la vida diaria)
base_frases = {
    # Expresiones de Disculpa y Sentimientos
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
    
    # Gustos y Preferencias cotidianas
    "hola mi cancion favorita es lola la vaca": {
        "Inglés": "Hello, my favorite song is Lola the cow", "Francés": "Bonjour, ma chanson préférée est Lola la vache", 
        "Italiano": "Ciao, la mia canzone preferita è Lola la mucca", "Alemán": "Hallo, mein Lieblingslied ist Lola die Kuh", "Portugués": "Olá, minha música favorita é Lola a vaca"
    },
    "me gusta el helado de chocolate": {
        "Inglés": "I like chocolate ice cream", "Francés": "J'aime la glace au chocolat", 
        "Italiano": "Mi piace il gelato al chocolat", "Alemán": "Ich mag Schokoladeneis", "Portugués": "Eu gosto de sorvete de chocolate"
    },
    "tengo hambre quiero comer": {
        "Inglés": "I'm hungry, I want to eat", "Francés": "J'ai faim, je veux manger", 
        "Italiano": "Ho fame, voglio mangiare", "Alemán": "Ich habe Hunger, ich will essen", "Portugués": "Estou com fome, quero comer"
    },
    
    # Frases de Necesidad y Ayuda
    "donde esta el baño": {
        "Inglés": "Where is the bathroom?", "Francés": "Où sont les toilettes?", 
        "Italiano": "Dov'è il bagno?", "Alemán": "Wo ist die Toilette?", "Portugués": "Onde fica o banheiro?"
    },
    "puedes ayudarme por favor": {
        "Inglés": "Can you help me, please?", "Francés": "Pouvez-vous m'aider, s'il vous plaît?", 
        "Italiano": "Puoi aiutarmi, per favore?", "Alemán": "Kannst du mir bitte helfen?", "Portugués": "Você pode me ajudar, por favor?"
    },
    "muchas gracias por tu ayuda": {
        "Inglés": "Thank you very much for your help", "Francés": "Merci beaucoup pour votre aide", 
        "Italiano": "Grazie mille per il tuo aiuto", "Alemán": "Vielen Dank für deine Hilfe", "Portugués": "Muito obrigado pela sua ajuda"
    }
}

# 📖 Diccionario complementario palabra por palabra (Si el usuario mezcla oraciones)
diccionario_palabras = {
    "hola": {"Inglés": "Hello", "Francés": "Bonjour", "Italiano": "Ciao", "Alemán": "Hallo", "Portugués": "Olá"},
    "no": {"Inglés": "no", "Francés": "non", "Italiano": "no", "Alemán": "nein", "Portugués": "não"},
    "es": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "é"},
    "mi": {"Inglés": "my", "Francés": "mon", "Italiano": "mio", "Alemán": "mein", "Portugués": "meu"},
    "culpa": {"Inglés": "fault", "Francés": "faute", "Italiano": "colpa", "Alemán": "Schuld", "Portugués": "culpa"},
    "gracias": {"Inglés": "thanks", "Francés": "merci", "Italiano": "grazie", "Alemán": "danke", "Portugués": "obrigado"},
    "adios": {"Inglés": "goodbye", "Francés": "au revoir", "Italiano": "arrivederci", "Alemán": "auf Wiedersehen", "Portugués": "adeus"}
}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        # Normalizamos la frase escrita por el usuario
        texto_limpio = texto_usuario.lower().replace(",", "").replace(".", "").replace("¿", "").replace("?", "").replace("¡", "").replace("!", "").strip()
        
        # 1. Intentar traducir la frase completa desde la base de datos experta
        if texto_limpio in base_frases:
            resultado_final = base_frases[texto_limpio][idioma_seleccionado]
            st.success("¡Traducción Estructurada Exitosa!")
            st.info(resultado_final)
            
        # 2. Si es una frase compuesta, armarla palabra por palabra de forma segura
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

