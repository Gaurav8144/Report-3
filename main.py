from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI()

# Serve static HTML file
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# API endpoint
@app.post("/reply")
async def reply(request: Request):
    data = await request.json()
    user_message = data.get("message", "").lower()
    return JSONResponse(content={"reply": "bye"})
