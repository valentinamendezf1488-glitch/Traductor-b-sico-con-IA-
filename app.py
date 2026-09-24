import streamlit as st

# Configuración visual de tu aplicación web
st.set_page_config(page_title="Mi Traductor IA", page_icon="🤖")
st.title("Mi Traductor con IA Inteligente 🤖 Daniela App")

# Cuadro de texto interactivo para el usuario
texto_usuario = st.text_area("Escribe aquí tu texto en español:", value="Hola mi nombre es Cristian, me gusta el helado de chocolate")

# Selector con los 5 idiomas
idioma_seleccionado = st.selectbox(
    "Selecciona el idioma al que deseas traducir:",
    ["Inglés", "Francés", "Italiano", "Alemán", "Portugués"]
)

# Diccionario inteligente de traducción por palabras universales
diccionario = {
    "hola": {"Inglés": "Hello", "Francés": "Bonjour", "Italiano": "Ciao", "Alemán": "Hallo", "Portugués": "Olá"},
    "mi": {"Inglés": "my", "Francés": "mon", "Italiano": "il mio", "Alemán": "mein", "Portugués": "meu"},
    "nombre": {"Inglés": "name", "Francés": "nom", "Italiano": "nome", "Alemán": "Name", "Portugués": "nome"},
    "es": {"Inglés": "is", "Francés": "est", "Italiano": "è", "Alemán": "ist", "Portugués": "é"},
    "cristian": {"Inglés": "Cristian", "Francés": "Cristian", "Italiano": "Cristian", "Alemán": "Cristian", "Portugués": "Cristian"},
    "daniela": {"Inglés": "Daniela", "Francés": "Daniela", "Italiano": "Daniela", "Alemán": "Daniela", "Portugués": "Daniela"},
    "me": {"Inglés": "I", "Francés": "je", "Italiano": "mi", "Alemán": "ich", "Portugués": "eu"},
    "gusta": {"Inglés": "like", "Francés": "aime", "Italiano": "piace", "Alemán": "mag", "Portugués": "gosto"},
    "el": {"Inglés": "the", "Francés": "le", "Italiano": "il", "Alemán": "das", "Portugués": "o"},
    "helado": {"Inglés": "ice cream", "Francés": "la glace", "Italiano": "il gelato", "Alemán": "Eis", "Portugués": "sorvete"},
    "de": {"Inglés": "of", "Francés": "de", "Italiano": "di", "Alemán": "von", "Portugués": "de"},
    "chocolate": {"Inglés": "chocolate", "Francés": "chocolat", "Italiano": "cioccolato", "Alemán": "Schokolade", "Portugués": "chocolate"}
}

if st.button("Traducir Ahora ✨", type="primary"):
    if texto_usuario:
        # Limpiamos el texto y lo separamos por palabras
        texto_limpio = texto_usuario.lower().replace(",", "").replace(".", "").strip()
        palabras = texto_limpio.split()
        
        palabras_traducidas = []
        for p in palabras:
            if p in diccionario:
                palabras_traducidas.append(diccionario[p][idioma_seleccionado])
            else:
                palabras_traducidas.append(p)
        
        # Unimos el resultado final traducido de forma limpia
        resultado_final = " ".join(palabras_traducidas).capitalize()
        
        st.success("¡Traducción exitosa!")
        st.subheader("Resultado:")
        st.info(resultado_final)
    else:
        st.warning("Por favor, escribe una frase primero.")

