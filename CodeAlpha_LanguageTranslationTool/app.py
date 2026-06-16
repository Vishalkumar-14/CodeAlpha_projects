import streamlit as st
from deep_translator import GoogleTranslator

# Page settings
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Heading
st.title("🌍 AI Language Translation Tool")
st.write(
    "Translate text from one language to another using Google Translation API."
)

st.divider()

# Supported languages
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

# Language selection
source_language = st.selectbox(
    "Select Source Language",
    list(language_options.keys())
)

target_language = st.selectbox(
    "Select Target Language",
    list(language_options.keys()),
    index=1
)

# User input
user_text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type or paste your text here..."
)

# Word counter
word_count = len(user_text.split())
st.caption(f"Word Count: {word_count}")

# Translation button
if st.button("Translate"):

    if not user_text.strip():
        st.warning("Please enter some text before translating.")

    elif source_language == target_language:
        st.warning("Source and target languages cannot be the same.")

    else:
        try:
            translated_result = GoogleTranslator(
                source=language_options[source_language],
                target=language_options[target_language]
            ).translate(user_text)

            st.subheader("Translated Text")

            st.success(translated_result)

            st.code(translated_result)

            if st.button("Copy Translation"):
                st.info(
                    "Copy the translated text from the box above."
                )

        except Exception as error:
            st.error(f"Translation Failed: {error}")

# Footer
st.divider()
st.caption(
    "Developed by Vishal Kumar | CodeAlpha Artificial Intelligence Internship"
)