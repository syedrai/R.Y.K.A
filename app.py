import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Setup Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")

# FastAPI App
app = FastAPI()

# Mount static folder if you want to serve HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        with open("index.html", "r", encoding="utf-8") as file:
            return HTMLResponse(content=file.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)

@app.post("/chat")
async def chat(request: Request):
    try:
        body = await request.json()
        prompt = body.get("prompt")
        if not prompt:
            return JSONResponse(status_code=400, content={"error": "Prompt missing."})

        response = model.generate_content(prompt)
        return {"response": response.text.strip()}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
