from fastapi import FastAPI
from app.api.status_endpoints import router as status_router

app = FastAPI(title="Data Collectors API")

app.include_router(status_router, prefix="/status")