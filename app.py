import streamlit as st
import google.generativeai as genai

# Configuración de la interfaz
st.set_page_config(page_title="Traductor Multilingüe con IA", page_icon="🌍", layout="centered")

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")
st.write("Selecciona los idiomas, escribe tu texto y obtén la traducción al instante.")

# Configuración automática de la API Key para evitar errores
# (Si prefieres dejarla fija aquí entre las comillas, puedes hacerlo)
API_KEY_FIJA = ""  # O déjala vacía si prefieres usar la barra lateral

with st.sidebar:
    st.header("Configuración")
    api_key_input = st.text_input("Gemini API Key:", value=API_KEY_FIJA, type="password")
    st.info("Traductor configurado y listo para usar.")

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
    clave_a_usar = api_key_input if api_key_input else API_KEY_FIJA
    
    if not clave_a_usar.strip() or clave_a_usar == "PEGA_AQUÍ_TU_CLAVE":
        st.warning("⚠️ Por favor, ingresa tu clave válida.")
    elif not texto_usuario.strip():
        st.warning("⚠️ Por favor, ingresa una palabra o frase para traducir.")
    else:
        try:
            genai.configure(api_key=clave_a_usar.strip())
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
