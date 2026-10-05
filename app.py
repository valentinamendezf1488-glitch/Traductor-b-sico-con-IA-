import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Diagnóstico de Modelos", page_icon="🔍")
st.title("🔍 Diagnóstico de Modelos Gemini")

if "GEMINI_API_KEY" in st.secrets:
    api_key_activa = st.secrets["GEMINI_API_KEY"]
else:
    st.error("⚠️ Falta configurar la GEMINI_API_KEY en los Secrets.")
    st.stop()

if st.button("Ver modelos disponibles para mi clave"):
    try:
        genai.configure(api_key=api_key_activa)
        st.write("Conectando con Google para listar modelos permitidos...")
        
        # Consultamos directamente a la API qué modelos acepta tu clave
        modelos_disponibles = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        st.success("¡Conexión exitosa! Estos son los modelos que SÍ puedes usar:")
        for modelo in modelos_disponibles:
            st.code(modelo)
            
    except Exception as e:
        st.error(f"Error de conexión: {e}")
