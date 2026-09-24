import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Daniela")

idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán"]
)

codigos_idiomas = {"Inglés": "en", "Francés": "fr", "Italiano": "it", "Alemán": "de"}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        try:
            codigo_destino = codigos_idiomas[idioma_seleccionado]
            url = f"https://googleapis.com{codigo_destino}&dt=t&q={urllib.parse.quote(texto_usuario)}"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                datos = json.loads(response.read().decode())
                resultado = datos[0][0][0] # Filtra el texto limpio de la traducción
                
                st.success("¡Traducción exitosa!")
                st.info(resultado)
        except Exception as e:
            st.error(f"Error al conectar: {e}")
