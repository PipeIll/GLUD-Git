from fastapi import FastAPI
from app.routes.clients import router as clients_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API running"}


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(clients_router)