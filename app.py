import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Traductor Multilingüe con IA", page_icon="🌍", layout="centered")

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")

# Cargar la clave automáticamente desde los Secrets de Streamlit Cloud
if "GEMINI_API_KEY" in st.secrets:
    api_key_activa = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ No se encontró la 'GEMINI_API_KEY' en los Secrets de Streamlit. Por favor, configúrala en el panel.")
    st.stop()

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
    if not texto_usuario.strip():
        st.warning("⚠️ Por favor, ingresa una palabra o frase para traducir.")
    else:
        try:
            genai.configure(api_key=api_key_activa)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("Traduciendo con IA..."):
                prompt = (
                    f"Eres un traductor experto y preciso, especializado también en lenguas mayas como el Kaqchikel. "
                    f"Traduce el siguiente texto del idioma '{idioma_origen}' al idioma '{idioma_destino}'. "
                    f"Devuelve únicamente la traducción exacta, sin explicaciones adicionales:\n\n{texto_usuario}"
                )
                
                response = model.generate_content(prompt)
                
                st.success("¡Traducción completada!")
                st.markdown("### Resultado:")
                st.write(response.text)
                
        except Exception as e:
            st.error(f"Ocurrió un error al conectar con la API: {e}")
