import streamlit as st
from google import genai

# Reemplaza con tu clave de API de Google AI Studio
API_KEY = "TU_API_KEY_AQUI"
client = genai.Client(api_key=API_KEY)

# Configuración de la interfaz web
st.set_page_config(page_title="Traductor IA Multilingüe con Kaqchikel", page_icon="🌐")
st.title("🌐 Traductor Inteligente con Kaqchikel Avanzado")

# Lista completa de idiomas
idiomas = [
    "Español", "Inglés", "Kaqchikel", "Francés", "Alemán", 
    "Italiano", "Japonés", "Portugués", "Chino Mandarín", "Ruso"
]

col1, col2 = st.columns(2)
with col1:
    idioma_origen = st.selectbox("Idioma de origen:", idiomas, index=0)
with col2:
    idioma_destino = st.selectbox("Idioma a traducir:", idiomas, index=1)

texto_usuario = st.text_area("Escribe el texto aquí para traducir:", height=150)

if st.button("Traducir", type="primary"):
    if not texto_usuario.strip():
        st.warning("Por favor, ingresa un texto para traducir.")
    else:
        # Prompt con un glosario y base de conocimiento masiva incrustada para el Kaqchikel
        prompt = f"""
        Eres un lingüista experto y traductor profesional nativo especializado en el idioma maya Kaqchikel (normado estrictamente por la ALMG) y en los demás idiomas del mundo. 
        Tu objetivo es traducir el texto de manera perfecta, fluida y sin ningún tipo de malentendido, aplicando la gramática, los saltillos (') y las glotalizaciones correctas.

        Usa como base de referencia estricta el siguiente repertorio masivo de vocabulario, raíces y pronombres en Kaqchikel para asegurar coherencia absoluta:
        - Pronombres / Sujetos: Rin/In (Yo), Rat (Tú), Rja' (Él/Ella), Oj (Nosotros), Ix (Ustedes), Rje' (Ellos/Ellas).
        - Naturaleza y Entorno: Ab'äj (Piedra), Ch'umil (Estrella), Ik' (Luna), Q'ij (Sol), Ya' (Agua), K'iche' (Bosque/Selva), Juyu' (Cerro/Montaña), Kaqiq' (Viento), Xar (Cielo), Q'aq' (Fuego).
        - Familia y Sociedad: Ach'alal (Familiares), Achi (Hombre), Ixöq ( Mujer ), Alab'ëts (Joven), Ak'al (Niño/Niña), Mama' (Anciano/Abuelo), Ixnam (Anciana/Abuela), Tijonel (Maestro), Ajkun (Médico tradicional/Curandero).
        - Anatomía: Jolomaj (Cabeza), Wa'ch (Ostra/Cara), Aq'oman (Medicina), Q'ab'aj (Mano), Xikin (Orejá), B'aqil (Hueso).
        - Alimentos y Objetos: Wa (Tortilla/Comida), Kape (Café), Ixkun (Olla), Ch'atäl (Mesa), K'olib'äl (Silla), Po't (Huipil), Xüt (Corte).
        - Verbos comunes y Acciones: Tijon (Estudiar), Tzijon (Hablar), Choman (Pensar), B'iyin (Caminar), Waran (Dormir), Tijin (Comer), Chakun (Trabajar), K'asän (Vivir), Kaminaq (Muerto).
        - Números base: Jun (1), Ka'i' (2), Oxi' (3), Kaji' (4), Waqi' (6), Wuqu' (7), Waxaqi' (8), B'eleje' (9), Lajuj (10).

        Instrucciones estrictas:
        1. Traduce fielmente el siguiente texto de {idioma_origen} a {idioma_destino}.
        2. Respeta rigurosamente los marcadores de posesión y persona en Kaqchikel (prefixación ergativa y absolutiva).
        3. No inventes palabras; utiliza términos tradicionales y académicos válidos.
        4. Devuelve ÚNICAMENTE la traducción final limpia, sin notas, explicaciones ni comentarios adicionales.

        Texto a traducir: {texto_usuario}
        """
        
        with st.spinner("Procesando traducción de alta precisión..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
        st.subheader("Traducción:")
        st.success(response.text)
