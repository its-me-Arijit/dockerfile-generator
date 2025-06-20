import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up model
model = genai.GenerativeModel("gemini-1.5-pro")

PROMPT = """
Generate an optimized Dockerfile for a {language} application.
Include:
- Base image
- Dependency installation
- Working directory
- Copying source code
- CMD to run the app
Add inline comments and avoid any extra explanation.
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text.strip()

if __name__ == "__main__":
    lang = input("Enter programming language: ")
    print("\nGenerated Dockerfile:\n")
    print(generate_dockerfile(lang))
