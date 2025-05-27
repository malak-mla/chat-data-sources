from fastapi import APIRouter
from app.models.collector_status import get_all_statuses

router = APIRouter()

@router.get("/")
def list_statuses():
    return get_all_statuses()