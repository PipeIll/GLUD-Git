from fastapi import APIRouter   
from app.utils import read_json  

router = APIRouter(
    prefix="/routines",     
    tags=["routines"] 
)


@router.get("/")     
def get_routines():
    routines = read_json("app/data/routines.json")
    return routines