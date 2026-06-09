import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

st.title("🌐 Language Translation Tool")

st.write(
    "Translate text between multiple languages using AI-powered translation."
)

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

translate_button = st.button("Translate")

if translate_button:

    if text.strip():

        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.subheader("Translated Text")

        st.text_area(
            "Result",
            translated_text,
            height=100
        )

        # Text-to-Speech
        tts = gTTS(
            text=translated_text,
            lang=languages[target_lang]
        )

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as fp:

            tts.save(fp.name)

            audio_file = open(fp.name, "rb")
            audio_bytes = audio_file.read()

        st.audio(
            audio_bytes,
            format="audio/mp3"
        )

    else:
        st.warning(
            "Please enter some text to translate."
        )