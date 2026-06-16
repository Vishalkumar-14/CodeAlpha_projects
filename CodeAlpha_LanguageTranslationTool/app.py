import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

# Page Configuration
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Language Translation Tool")
st.write(
    "Translate text between multiple languages using Google Translation API."
)

st.divider()

# Supported Languages
language_options = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Italian": "it"
}

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(language_options.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(language_options.keys()),
        index=1
    )

# User Input
input_text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# Word Count
word_count = len(input_text.split())
st.caption(f"Word Count: {word_count}")

translated_text = ""

# Translate Button
if st.button("Translate"):

    if not input_text.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Source and target languages cannot be the same.")

    else:
        try:
            translator = GoogleTranslator(
                source=language_options[source_language],
                target=language_options[target_language]
            )

            translated_text = translator.translate(input_text)

            st.subheader("Translated Text")

            st.text_area(
                "Result",
                translated_text,
                height=180
            )

            # Store Translation
            st.session_state["translated_text"] = translated_text

        except Exception as error:
            st.error(f"Translation Failed: {error}")

# Copy Button
if "translated_text" in st.session_state:

    if st.button("📋 Copy Translation"):

        pyperclip.copy(st.session_state["translated_text"])

        st.success("Translation copied successfully!")

# Footer
st.divider()

st.caption(
    "Developed by Vishal Kumar | CodeAlpha Artificial Intelligence Internship"
)