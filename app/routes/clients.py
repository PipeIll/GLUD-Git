from fastapi import APIRouter
from app.utils import read_json

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)


@router.get("/")
def get_clients():
    clients = read_json("app/data/clients.json")
    return clients