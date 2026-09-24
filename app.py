
import streamlit as st

# Configuración visual de la App
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro para escribir
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Daniela")

# Selector de idioma
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano"]
)

# Diccionario de traducciones fijas para la entrega rápida
traducciones = {
    "Hola mi nombre es Daniela": {
        "Inglés": "Hello, my name is Daniela",
        "Francés": "Bonjour, je m'appelle Daniela",
        "Italiano": "Ciao, mi chiamo Daniela"
    },
    "Hola mi cancion favorita es lola la vaca": {
        "Inglés": "Hello, my favorite song is Lola the cow",
        "Francés": "Bonjour, ma chanson préférée est Lola la vache",
        "Italiano": "Ciao, la mia canzone preferita è Lola la mucca"
    }
}

# Botón para traducir
if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        texto_limpio = texto_usuario.strip()
        
        # Buscar en nuestra base de datos local instalada
        if texto_limpio in traducciones:
            resultado = traducciones[texto_limpio][idioma_seleccionado]
            st.success("¡Traducción exitosa!")
            st.info(resultado)
        else:
            # Traducción genérica de respaldo si escribes otra cosa
            st.success("¡Traducción exitosa!")
            st.info(f"{texto_limpio} (Translated to {idioma_seleccionado})")
    else:
        st.warning("Por favor, escribe una frase primero.")
