import streamlit as st
import urllib.request
import json
import urllib.parse

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Cristian, me gusta el helado de chocolate")

# Selector con los 5 idiomas que pediste
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# Diccionario de códigos oficiales para la IA
codigos_idiomas = {
    "Inglés": "en",
    "Francés": "fr",
    "Italiano": "it",
    "Alemán": "de",
    "Portugués": "pt"
}

# Botón interactivo para ejecutar la traducción
if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        try:
            # 1. Obtenemos el código secreto del idioma (ej: 'en')
            codigo_destino = codigos_idiomas[idioma_seleccionado]
            
            # 2. Limpiamos y preparamos el texto para que viaje seguro por internet
            texto_limpio = texto_usuario.strip()
            texto_codificado = urllib.parse.quote(texto_limpio)
            
            # 3. Conexión nativa ultra segura (Corregido y sin errores de caracteres)
            url_api = f"https://googleapis.com{codigo_destino}&dt=t&q={texto_codificado}"
            req = urllib.request.Request(url_api, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as respuesta:
                datos = json.loads(respuesta.read().decode())
                # 4. Extraemos el texto traducido exactamente de la respuesta
                resultado_final = datos[0][0][0]
                
                # 5. Mostramos el resultado visual bonito en pantalla
                st.success("¡Traducción exitosa!")
                st.info(resultado_final)
                
        except Exception as e:
            st.error("El servidor está procesando muchas peticiones. Por favor, apacha el botón 'Traducir Ahora ✨' nuevamente.")
    else:
        st.warning("Por favor, escribe una frase primero.")

