from fastapi import FastAPI
from database import Base, engine
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from api.vehicles.main import vehicle_router, trim_router
from api.home.home import home_router

app = FastAPI(docs_url="/docs")
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(vehicle_router)
app.include_router(home_router)
app.include_router(trim_router)