from fastapi import APIRouter, Request
import database
from database import models
from api.vehicles.main import templates

home_router = APIRouter()

@home_router.get("/")
def home(request: Request):
    db = database.SessionLocal()
    vehicles = db.query(models.Vehicle).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "vehicles": vehicles})
