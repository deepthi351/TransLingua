import streamlit as st
from transformers import pipeline

# Streamlit App Setup
st.set_page_config(page_title="TransLingua - AI Translator", layout="centered")
st.title("🌍 TransLingua: AI-Powered Language Translation")
st.write("Translate text seamlessly between multiple languages using AI.")

# Input Text
st.markdown("### ✍️ Enter the text you want to translate:")
user_input = st.text_area("Enter text here", "", height=150)

# Language Selection
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es"
}

source_lang = st.selectbox("🌐 Select source language:", list(languages.keys()))
target_lang = st.selectbox("🎯 Select target language:", list(languages.keys()))

# Ensure source and target languages are different
if source_lang == target_lang:
    st.warning("⚠️ Please select different source and target languages.")

# Translation Button
if st.button("🔄 Translate"):
    if user_input.strip() == "":
        st.error("❌ Please enter text to translate.")
    else:
        # Hugging Face models for translation
        model_map = {
            ("English", "French"): "Helsinki-NLP/opus-mt-en-fr",
            ("French", "English"): "Helsinki-NLP/opus-mt-fr-en",
            ("English", "Spanish"): "Helsinki-NLP/opus-mt-en-es",
            ("Spanish", "English"): "Helsinki-NLP/opus-mt-es-en",
            ("French", "Spanish"): "Helsinki-NLP/opus-mt-fr-es",
            ("Spanish", "French"): "Helsinki-NLP/opus-mt-es-fr"
        }

        model_name = model_map.get((source_lang, target_lang))

        if model_name:
            try:
                translator = pipeline("translation", model=model_name)
                translated_text = translator(user_input, max_length=100)[0]['translation_text']
                st.success(f"✅ Translated Text:\n\n{translated_text}")
            except Exception as e:
                st.error(f"⚠️ Error in translation: {str(e)}")
        else:
            st.error("⚠️ Translation model for selected language pair is not available.")