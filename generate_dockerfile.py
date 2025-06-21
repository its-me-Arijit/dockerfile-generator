import os
import google.generativeai as genai

# 1️⃣ Load the Gemini API key from environment variable (recommended over hardcoding)
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in environment variables or .env file.")


# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

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
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

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
