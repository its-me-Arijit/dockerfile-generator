import streamlit as st
from generate_dockerfile import generate_dockerfile

st.set_page_config(page_title="Dockerfile Generator", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #0072ff;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
        margin-top: 1em;
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background-color: #0059b2;
    }
    .stTextInput>div>div>input {
        border-radius: 6px;
        border: 1.5px solid #0072ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Dockerfile Generator")
st.write("Easily generate an optimized Dockerfile for your favorite programming language and framework.")

st.markdown("---")

# Input box with a placeholder
language = st.text_input(
    "What programming language or framework do you want a Dockerfile for?",
    placeholder="e.g. Python, Node.js, Java, Django, React..."
)

st.markdown("")

# Submit button centered
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("Generate Dockerfile", use_container_width=True)

if generate:
    if not language.strip():
        st.warning("⚠️ Please enter a programming language or framework.")
    else:
        with st.spinner("Generating your Dockerfile..."):
            try:
                result = generate_dockerfile(language)
                st.success("✅ Dockerfile generated!")
                st.code(result, language="dockerfile")
            except Exception as e:
                st.error("❌ Something went wrong while generating the Dockerfile.")
                st.exception(e)

st.markdown("---")
st.markdown(
    "<small style='color: #888;'>Built with ❤️ for developers. No AI provider mentioned.</small>",
    unsafe_allow_html=True
)
