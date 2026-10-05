import streamlit as st
from google import genai

# =====================================================
# CONFIGURACIÓN DE LA IA (GOOGLE-GENAI)
# =====================================================
# Nota: Streamlit busca la API Key en st.secrets["GEMINI_API_KEY"]
# Si prefieres probar localmente con una variable de entorno, asegúrate de configurarla.
try:
    client = genai.Client(api_key=st.secrets.get("GEMINI_API_KEY"))
except Exception:
    client = None

# =====================================================
# BASE DE DATOS MAESTRA (Opcional para referencias)
# =====================================================
traductor_base_datos = {
    "familia": [
        {"es": "Madre", "en": "Mother", "fr": "Mère", "ko": "어머니 (eomeoni)", "pt": "Mãe", "cak": "Nan"},
        {"es": "Padre", "en": "Father", "fr": "Père", "ko": "아버지 (abeoji)", "pt": "Pai", "cak": "Tat"},
        {"es": "Hermano", "en": "Brother", "fr": "Frère", "ko": "형제 (hyeongje)", "pt": "Irmão", "cak": "Atz'ih"}
    ],
    "saludos_cortesía": [
        {"es": "Hola", "en": "Hello", "fr": "Bonjour", "ko": "안녕하세요 (annyeonghaseyo)", "pt": "Olá", "cak": "Saqarik' / Ali'j"},
        {"es": "Buenos días", "en": "Good morning", "fr": "Bonjour", "ko": "좋은 아침입니다 (joeun achimimnida)", "pt": "Bom dia", "cak": "Utz laq'ab'"},
        {"es": "Gracias", "en": "Thank you", "fr": "Merci", "ko": "감사합니다 (gamsahamnida)", "pt": "Obrigado", "cak": "Matyox"}
    ],
    "preguntas_frecuentes": [
        {"es": "¿Cómo estás?", "en": "How are you?", "fr": "Comment ça va?", "ko": "어떻게 지내세요? (eotteoke jinaeseyo?)", "pt": "Como você está?", "cak": "¿La utz ratz'ib'?"},
        {"es": "¿Cuál es tu nombre?", "en": "What is your name?", "fr": "Quel est votre nom?", "ko": "성함이 어떻게 되세요? (seonghami eotteoke doeseyo?)", "pt": "Qual é o seu nome?", "cak": "¿Bi'aj awach?"}
    ],
    "frases": [
        {"es": "Mucho gusto", "en": "Nice to meet you", "fr": "Enchanté(e)", "ko": "만나서 반갑습니다", "pt": "Muito prazer", "cak": "Utzilem ri k'olic"},
        {"es": "Por favor", "en": "Please", "fr": "S'il vous plaît", "ko": "제발", "pt": "Por favor", "cak": "Tab'ij chawe"},
        {"es": "Adiós", "en": "Goodbye", "fr": "Au revoir", "ko": "안녕히 가세요", "pt": "Tchau", "cak": "Utz rub'ey"},
        {"es": "Buenos días a todos", "en": "Good morning everyone", "fr": "Bonjour tout le monde", "ko": "여러분 안녕하십니까", "pt": "Bom dia a todos", "cak": "Utz laq'ab' chi re konojel"},
        {"es": "¿Cómo te llamas?", "en": "What is your name?", "fr": "Comment tu t'appelles?", "ko": "이름이 뭡니까?", "pt": "Qual é o seu nome?", "cak": "¿La bi'aj awach?"},
        {"es": "Estoy bien", "en": "I am fine", "fr": "Je vais bien", "ko": "저는 잘 지냅니다", "pt": "Eu estou bem", "cak": "Utz in k'olic"}
    ]
}

# =====================================================
# CONFIGURACIÓN DE LA INTERFAZ EN STREAMLIT
# =====================================================
st.set_page_config(
    page_title="Traductor Multilingüe con IA",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")
st.write("Selecciona los idiomas y escribe el texto que deseas traducir con la IA.")

# Opciones de idiomas
idiomas = ["Español", "Inglés", "Francés", "Coreano", "Portugués", "Kaqchikel"]

col1, col2 = st.columns(2)
with col1:
    idioma_origen = st.selectbox("Idioma de origen", idiomas)
with col2:
    idioma_destino = st.selectbox("Idioma de destino", idiomas)

# Entrada de texto del usuario
texto_usuario = st.text_input("Escribe una palabra o frase para traducir:")

# Botón de traducción funcional
if st.button("Traducir"):
    if not texto_usuario.strip():
        st.warning("Por favor, ingresa una palabra o frase válida.")
    elif not client:
        st.error("No se encontró la API Key de Google GenAI configurada en st.secrets['GEMINI_API_KEY'].")
    else:
        with st.spinner("Traduciendo con IA..."):
            try:
                # Prompt estructurado para guiar al modelo
                prompt = (
                    f"Eres un traductor experto y preciso, especializado también en lenguas mayas como el Kaqchikel. "
                    f"Traduce el siguiente texto del idioma '{idioma_origen}' al idioma '{idioma_destino}'. "
                    f"Devuelve únicamente la traducción exacta, sin explicaciones adicionales:\n\n{texto_usuario}"
                )
                
                # Llamada al modelo gemini-2.5-flash (o el estándar recomendado)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                
                st.success("¡Traducción completada!")
                st.markdown(f"### Resultado:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Ocurrió un error al conectar con la IA: {e}")
