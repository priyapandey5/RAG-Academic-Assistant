from fastapi import FastAPI

from api.chat_v2 import router as chat_router
from api.upload_v3 import router as upload_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(upload_router)


@app.get("/")
def health():
    return {"status": "ok"}