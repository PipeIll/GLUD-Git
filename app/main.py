from fastapi import FastAPI
from app.routes.clients import router as clients_router
from app.routes.routines import router as routines_router
from app.routes.progress import router as progress_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(clients_router)
app.include_router(routines_router)
app.include_router(progress_router)