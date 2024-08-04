import streamlit as st
from deep_translator import GoogleTranslator

def translate_text(text, src_lang='auto', dest_lang='en'):
    translator = GoogleTranslator(source=src_lang, target=dest_lang)
    return translator.translate(text)

# Streamlit app
st.title('Text Translator')

# Prompt the user for the text to be translated
text_to_translate = st.text_input('Enter the text you want to translate:')

# Prompt the user for the source language (default is 'auto')
src_lang = st.text_input('Enter the source language code (or leave blank to detect automatically):', '')

# Prompt the user for the destination language (default is 'en')
dest_lang = st.text_input('Enter the destination language code (default is \'en\'):', 'en')

# Perform the translation when the user presses the button
if st.button('Translate'):
    if not text_to_translate:
        st.error('Please enter text to translate')
    else:
        if not src_lang:
            src_lang = 'auto'
        if not dest_lang:
            dest_lang = 'en'
        translated_text = translate_text(text_to_translate, src_lang=src_lang, dest_lang=dest_lang)
        
        # Display the original and translated text
        st.write('**Original text:**', text_to_translate)
        st.write('**Translated text:**', translated_text)
