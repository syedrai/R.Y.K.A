# 🤖 Ryka AI - Lightweight FastAPI Gemini Assistant

Ryka is a minimal FastAPI application powered by Google's Gemini AI. You can ask questions or generate content using a POST request.

## 🔧 Requirements

- Python 3.10+
- Gemini API key (https://ai.google.dev/)

## 🚀 Setup

1. Clone the repo
2. Create a `.env` file with your API key:

3. Install dependencies:

```bash
pip install -r requirements.txt
Run the app:

4.bash

uvicorn main:app --reload

5.Visit http://127.0.0.1:8000

```bash
git init
git add main.py requirements.txt README.md
git commit -m "Initial Ryka AI CLI version with FastAPI and Gemini"
git remote add origin https://github.com/syedrai/ryka-ai.git
git push -u origin main
