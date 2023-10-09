import streamlit as st
from deep_translator import GoogleTranslator
from summarizer import textrank

# Streamlit app layout
st.title("Hindi Text Summarizer")

# Input area for the document
document = st.text_area("Enter the Hindi document")

# Generate summary button
if st.button("Generate Summary"):
    # Check if document is provided
    if document:
        # Translate Hindi text to English
        translator = GoogleTranslator(source='hi', target='en', timeout=10)
        engText = translator.translate(document)

        # Generate summary in English
        engSum = textrank(engText)

        # Translate each sentence back to Hindi
        hinSum = []
        for sentence in engSum:
            hinSent = GoogleTranslator(source='en', target='hi').translate(sentence)
            hinSum.append(hinSent)

        # Display the generated summary
        st.subheader("Summary")
        for sentence in hinSum:
            st.write(sentence)
    else:
        st.warning("Please enter a document.")
