from fastapi import APIRouter
from app.utils import read_json, write_json
from pydantic import BaseModel

router = APIRouter(
    prefix="/progress",
    tags=["progress"]
)


class Progress(BaseModel):
    client_id: int
    note: str


@router.post("/")
def create_progress(progress: Progress):
    all_progress = read_json("app/data/progress.json")

    new_entry = {
        "id": len(all_progress) + 1,
        "client_id": progress.client_id,
        "note": progress.note
    }

    all_progress.append(new_entry)
    write_json("app/data/progress.json", all_progress)

    return {
        "message": "Progress registered successfully",
        "progress": new_entry
    }
    
@router.get("/{client_id}")
def get_progress(client_id: int):
    all_progress = read_json("app/data/progress.json")
    
    client_progress = [entry for entry in all_progress if entry["client_id"] == client_id]
    
    return client_progress  