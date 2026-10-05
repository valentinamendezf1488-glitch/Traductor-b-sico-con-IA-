import streamlit as st
from google import genai

# Configuración de la interfaz
st.set_page_config(page_title="Traductor Multilingüe con IA", page_icon="🌍", layout="centered")

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")
st.write("Selecciona los idiomas, escribe tu texto y obtén la traducción al instante.")

# Pedir la API Key directamente en la barra lateral para ahorrar tiempo
with st.sidebar:
    st.header("Configuración")
    api_key_input = st.text_input("Ingresa tu Gemini API Key:", type="password")
    st.info("Pega aquí tu clave de API de Google GenAI para activar el traductor.")

# Opciones de idiomas
idiomas = ["Español", "Inglés", "Francés", "Coreano", "Portugués", "Kaqchikel"]

col1, col2 = st.columns(2)
with col1:
    idioma_origen = st.selectbox("Idioma de origen", idiomas)
with col2:
    idioma_destino = st.selectbox("Idioma de destino", idiomas)

# Entrada de texto del usuario
texto_usuario = st.text_input("Escribe una palabra o frase para traducir:")

# Botón de traducción
if st.button("Traducir"):
    if not api_key_input.strip():
        st.warning("⚠️ Por favor, ingresa tu Gemini API Key en la barra lateral izquierda.")
    elif not texto_usuario.strip():
        st.warning("⚠️️ Por favor, ingresa una palabra o frase para traducir.")
    else:
        try:
            # Inicializar el cliente con la clave ingresada
            client = genai.Client(api_key=api_key_input)
            
            with st.spinner("Traduciendo con IA..."):
                prompt = (
                    f"Eres un traductor experto y preciso, especializado también en lenguas mayas como el Kaqchikel. "
                    f"Traduce el siguiente texto del idioma '{idioma_origen}' al idioma '{idioma_destino}'. "
                    f"Devuelve únicamente la traducción exacta, sin explicaciones adicionales:\n\n{texto_usuario}"
                )
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                
                st.success("¡Traducción completada!")
                st.markdown("### Resultado:")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
