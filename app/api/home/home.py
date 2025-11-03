from fastapi import APIRouter, Request
from app import database
from app.database import models
from app.api.vehicles.main import templates

home_router = APIRouter()

@home_router.get("/")
def home(request: Request):
    db = database.SessionLocal()
    vehicles = db.query(models.Vehicle).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "vehicles": vehicles})