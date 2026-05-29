from fastapi import APIRouter
from app.utils import read_json
from pydantic import BaseModel
from app.utils import write_json

router = APIRouter(
    prefix="/clients",
    tags=["clients"]
)


class Client(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    goal: str

@router.get("/")
def get_clients():
    clients = read_json("app/data/clients.json")
    return clients

@router.post("/")
def create_client(client: Client):
    clients = read_json("app/data/clients.json")

    new_client = {
        "id": len(clients) + 1,
        "name": client.name,
        "age": client.age,
        "weight": client.weight,
        "height": client.height,
        "goal": client.goal
    }

    clients.append(new_client)

    write_json("app/data/clients.json", clients)

    return {
        "message": "Client created successfully",
        "client": new_client
    }