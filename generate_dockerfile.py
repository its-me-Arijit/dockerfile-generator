import os
from dotenv import load_dotenv

load_dotenv()

USE_GEMINI = False  # Set to True if you want to use Gemini

if USE_GEMINI:
    import google.generativeai as genai
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("❌ GOOGLE_API_KEY not found in environment variables or .env file.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    import cohere
    cohere_api_key = os.getenv("COHERE_API_KEY")
    if not cohere_api_key:
        raise ValueError("❌ COHERE_API_KEY not found in environment variables or .env file.")
    co = cohere.Client(cohere_api_key)

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    prompt = PROMPT.format(language=language)
    if USE_GEMINI:
        response = model.generate_content(prompt)
        return response.text
    else:
        response = co.generate(
            model="command-r-plus",  # Use Cohere's best available model
            prompt=prompt,
            max_tokens=512,
            temperature=0.5
        )
        return response.generations[0].text.strip()

if __name__ == '__main__':
    try:
        language = input("Enter the programming language: ").strip()
        if not language:
            raise ValueError("⚠️ Programming language input cannot be empty.")
        dockerfile = generate_dockerfile(language)
        print("\nGenerated Dockerfile:\n")
        print(dockerfile)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")