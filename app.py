import streamlit as st
import urllib.request
import json
import urllib.parse

# Configuración visual de la App
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro para escribir
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Daniela")

# Selector de idioma
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán"]
)

codigos_idiomas = {"Inglés": "en", "Francés": "fr", "Italiano": "it", "Alemán": "de"}

# Botón para traducir
if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        try:
            codigo_destino = codigos_idiomas[idioma_seleccionado]
            
            # Limpiamos el texto para que internet lo entienda sin errores
            texto_limpio = texto_usuario.strip()
            texto_codificado = urllib.parse.quote(texto_limpio)
            
            # Dirección web corregida sin el error de tipeo
            url = f"https://googleapis.com{codigo_destino}&dt=t&q={texto_codificado}"
            
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as response:
                datos = json.loads(response.read().decode())
                # Obtenemos solo el texto traducido limpio
                resultado = datos[0][0][0]
                
                st.success("¡Traducción exitosa!")
                st.info(resultado)
        except Exception as e:
            st.error(f"Error al conectar: {e}")

