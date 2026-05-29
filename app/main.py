from fastapi import FastAPI
from app.routes.clients import router as clients_router
from app.routes.routines import router as routines_router
from app.routes.progress import router as progress_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/frontend/index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(clients_router)
app.include_router(routines_router)
app.include_router(progress_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")