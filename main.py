from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os

app = FastAPI()

# Serve index.html manually from static folder
@app.get("/", response_class=HTMLResponse)
async def serve_html():
    file_path = os.path.join("static", "index.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# API route for /reply
@app.post("/reply")
async def reply(data: dict):
    message = data.get("message", "").lower()
    if "bye" in message:
        return JSONResponse(content={"reply": "Goodbye!"})
    return JSONResponse(content={"reply": "Okay, bye!"})
