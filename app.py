import streamlit as st
import google.generativeai as genai

# Configuración de la interfaz
st.set_page_config(page_title="Traductor Multilingüe con IA", page_icon="🌍", layout="centered")

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")
st.write("Selecciona los idiomas, escribe tu texto y obtén la traducción al instante.")

# Inicializar estado de la sesión para la clave
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

with st.sidebar:
    st.header("Configuración")
    api_key_input = st.text_input(
        "Gemini API Key:", 
        value=st.session_state["api_key"], 
        type="password"
    )
    if api_key_input:
        st.session_state["api_key"] = api_key_input
    st.info("Pega tu clave de API aquí.")

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
    clave_activa = st.session_state.get("api_key", "").strip()
    
    if not clave_activa:
        st.warning("⚠️ Por favor, ingresa tu clave en la barra lateral izquierda.")
    elif not texto_usuario.strip():
        st.warning("⚠️ Por favor, ingresa una palabra o frase para traducir.")
    else:
        try:
            # Configurar con la clave ingresada
            genai.configure(api_key=clave_activa)
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
