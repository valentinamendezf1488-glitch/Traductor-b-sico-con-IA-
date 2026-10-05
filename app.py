import streamlit as st

# =====================================================
# BASE DE DATOS MAESTRA - TRADUCTOR MULTILINGÜE
# Idiomas: Español, Inglés, Francés, Coreano, Portugués, Kaqchikel
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
        # Frases adicionales personalizadas en Kaqchikel:
        {"es": "Buenos días a todos", "en": "Good morning everyone", "fr": "Bonjour tout le monde", "ko": "여러분 안녕하십니까", "pt": "Bom dia a todos", "cak": "Utz laq'ab' chi re konojel"},
        {"es": "¿Cómo te llamas?", "en": "What is your name?", "fr": "Comment tu t'appelles?", "ko": "이름이 뭡니까?", "pt": "Qual é o seu nome?", "cak": "¿La bi'aj awach?"},
        {"es": "Estoy bien", "en": "I am fine", "fr": "Je vais bien", "ko": "저는 잘 지냅니다", "pt": "Eu estou bem", "cak": "Utz in k'olic"}
    ]
}

# Configuración de la interfaz en Streamlit
st.set_page_config(
    page_title="Traductor Multilingüe con IA",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Traductor Multilingüe (Español, Inglés, Francés, Coreano, Portugués, Kaqchikel)")
st.write("Selecciona los idiomas y escribe o busca una palabra o frase en tu base de datos.")

# Opciones de idiomas
idiomas = ["Español", "Inglés", "Francés", "Coreano", "Portugués", "Kaqchikel"]

col1, col2 = st.columns(2)
with col1:
    idioma_origen = st.selectbox("Idioma de origen", idiomas)
with col2:
    idioma_destino = st.selectbox("Idioma de destino", idiomas)

# Entrada de texto del usuario
texto_usuario = st.text_input("Escribe una palabra o frase para traducir:")

if st.button("Traducir"):
    if texto_usuario.strip() != "":
        st.success(f"Traduciendo '{texto_usuario}' de {idioma_origen} a {idioma_destino}...")
        # Aquí se integrará la lógica de búsqueda en el diccionario y google-genai
    else:
        st.warning("Por favor, ingresa una palabra o frase válida.")
