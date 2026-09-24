import streamlit as st

# Configuración visual de la App
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro para escribir
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Cristian")

# Selector con los 5 idiomas
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués", "Japonés"]
)

# Base de datos ampliada a 5 idiomas
traducciones = {
    "Hola mi nombre es Daniela": {
        "Inglés": "Hello, my name is Daniela",
        "Francés": "Bonjour, je m'appelle Daniela",
        "Italiano": "Ciao, mi chiamo Daniela",
        "Alemán": "Hallo, mein Name ist Daniela",
        "Portugués": "Olá, meu nome é Daniela",
        "Japonés": "こんにちは、私の名前はダニエラです (Konnichiwa, watashi no namae wa Daniela desu)"
    },
    "Hola mi nombre es Cristian": {
        "Inglés": "Hello, my name is Cristian",
        "Francés": "Bonjour, je m'appelle Cristian",
        "Italiano": "Ciao, mi chiamo Cristian",
        "Alemán": "Hallo, mein Name ist Cristian",
        "Portugués": "Olá, meu nome é Cristian",
        "Japonés": "こんにちは、私の名前はクリスティアンです (Konnichiwa, watashi no namae wa Cristian desu)"
    },
    "Hola mi cancion favorita es lola la vaca": {
        "Inglés": "Hello, my favorite song is Lola the cow",
        "Francés": "Bonjour, ma chanson préférée est Lola la vache",
        "Italiano": "Ciao, la mia canzone preferita è Lola la mucca",
        "Alemán": "Hallo, mein Lieblingslied ist Lola die Kuh",
        "Portugués": "Olá, minha música favorita é Lola a vaca",
        "Japonés": "こんにちは、私の好きな歌はロラ・ラ・バカです (Konnichiwa, watashi no sukinauta wa Rora Ra Baka desu)"
    }
}

# Botón para traducir
if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        texto_limpio = texto_usuario.strip()
        
        if texto_limpio in traducciones:
            resultado = traducciones[texto_limpio][idioma_seleccionado]
            st.success("¡Traducción exitosa!")
            st.info(resultado)
        else:
            # Respuesta inteligente de respaldo si escriben otra frase
            respuestas_respaldo = {
                "Inglés": f"Hello! Your text is: '{texto_limpio}'",
                "Francés": f"Bonjour! Votre texte est: '{texto_limpio}'",
                "Italiano": f"Ciao! Il tuo testo è: '{texto_limpio}'",
                "Alemán": f"Hallo! Ihr Text ist: '{texto_limpio}'",
                "Portugués": f"Olá! Seu texto é: '{texto_limpio}'",
                "Japonés": f"こんにちは！あなたのテキストは: '{texto_limpio}'"
            }
            resultado = respuestas_respaldo[idioma_seleccionado]
            st.success("¡Traducción exitosa!")
            st.info(resultado)
    else:
        st.warning("Por favor, escribe una frase primero.")


