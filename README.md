# 🚀 Dockerfile Generator with Streamlit & Cohere

Generate optimized Dockerfiles for your preferred programming language using AI!  
This app leverages [Cohere's AI API](https://cohere.com/) and a modern Streamlit UI to create Dockerfiles tailored to your stack—instantly.

---

## ✨ Features

- **AI-powered**: Generates best-practice Dockerfiles for any programming language.
- **Modern UI**: Built with [Streamlit](https://streamlit.io/) for a smooth, responsive user experience.
- **Customizable**: Easily adapt prompts or add more features.
- **Free to deploy**: Host on [Streamlit Community Cloud](https://streamlit.io/cloud) or run locally.

---

## 🌐 Live App

Check out the deployed Dockerfile Generator here:  
[https://dockerfile-generator.streamlit.app/](https://dockerfile-generator.streamlit.app/)

---

## 🖥️ Demo

![App Screenshot](https://github.com/its-me-Arijit/dockerfile-generator/raw/main/Screenshot%202025-06-21%20152523.png)

![App Screenshot](https://github.com/its-me-Arijit/dockerfile-generator/blob/main/Screenshot%202025-06-21%20152801.png)

---

## 🚦 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get your Cohere API key

- Sign up at [Cohere Dashboard](https://dashboard.cohere.com/) for a free API key.

### 4. Set up environment variables

Create a `.env` file in the project root:

```
COHERE_API_KEY=your_cohere_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

Open the provided `localhost` URL in your browser.

---

## 🛠️ Project Structure

```txt
.
├── app.py                   # Streamlit UI
├── generate_dockerfile.py   # Dockerfile generation logic (AI integration)
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
├── README.md                # This file
└── .github/
    └── app-screenshot.png   # (Optional) App screenshot
```

---

## 🧩 How It Works

1. **User inputs a programming language** in the Streamlit web UI.
2. **App sends a prompt** to Cohere's API to generate a Dockerfile.
3. **AI responds** with an optimized Dockerfile tailored to the language.
4. **User copies and uses** the Dockerfile for their project.

---

## 🌐 Deployment (Free!)

**Deploy on [Streamlit Community Cloud](https://streamlit.io/cloud):**

1. Push your code to a public GitHub repo.
2. Go to Streamlit Cloud and create a new app from your repo.
3. Add your `COHERE_API_KEY` in the app’s Secrets.
4. Click Deploy—done!

---

## 📝 Example Prompt & Output

**Prompt:**  
> Generate an ideal Dockerfile for Java with best practices.

**AI Output:**
```Dockerfile
# syntax=docker/dockerfile:1
FROM openjdk:11-slim
RUN apt-get update && apt-get install -y \
    curl git unzip \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
CMD ["java", "-jar", "your-app.jar"]
```

---

## 🤝 Contributing

Contributions welcome!  
- Open issues, suggest features, or submit PRs.

---

## 🙏 Credits

- [Streamlit](https://streamlit.io/)
- [Cohere](https://cohere.com/)
- [Arijit Ghosh](https://github.com/its-me-arijit) (Project Author)

---

*Built with ❤️ using AI!*
