from typing import Any

from fastapi import Body, FastAPI, Request

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/echo")
async def echo(request: Request, payload: Any = Body(...)):
    return {
        "headers": dict(request.headers),
        "body": payload,
    }
