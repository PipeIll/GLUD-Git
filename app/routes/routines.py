from fastapi import APIRouter   
from app.utils import read_json, write_json    
from pydantic import BaseModel 

router = APIRouter(
    prefix="/routines",     
    tags=["routines"] 
)

class Routine(BaseModel):
    name: str
    description: str
    client_id: int

@router.get("/")     
def get_routines():
    routines = read_json("app/data/routines.json")
    return routines

@router.post("/")
def create_routine(routine: Routine):
    routines = read_json("app/data/routines.json")

    new_routine = {
        "id": len(routines) + 1,
        "name": routine.name,
        "description": routine.description,
        "client_id": routine.client_id
    }

    routines.append(new_routine)

    write_json("app/data/routines.json", routines)

    return {
        "message": "Routine created successfully",
        "routine": new_routine
    }