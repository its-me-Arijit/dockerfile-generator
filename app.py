import streamlit as st
from generate_dockerfile import generate_dockerfile

st.set_page_config(page_title="Dockerfile Generator", layout="centered")

st.title("🚀 Dockerfile Generator with Gemini")
st.write("Generate an optimized Dockerfile based on your preferred programming language using Google's Gemini API.")

# Input box
language = st.text_input("Enter the programming language:", "")

# Submit button
if st.button("Generate Dockerfile"):
    if not language.strip():
        st.warning("⚠️ Please enter a programming language.")
    else:
        with st.spinner("Generating Dockerfile..."):
            try:
                result = generate_dockerfile(language)
                st.success("✅ Dockerfile generated successfully!")
                st.code(result, language="dockerfile")
            except Exception as e:
                st.error(f"❌ Error: {e}")
