from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from database.queries import get_vehicle_db, get_all_vehicles_db, create_vehicle_db, add_specs_db
from api.vehicles.schemas import VehicleRead, VehicleOut, Specs, SpecsRead

def result_message(result):
    if result:
        return {"status": 1, "message": "succesful"}
    return {"status": 0, "message": "error"}

vehicle_router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)
templates = Jinja2Templates(directory="templates")


trim_router = APIRouter(
    prefix="/trims",
    tags=["Trims"]
)


@vehicle_router.post("/create_vehicle", response_model=VehicleRead)
def create_vehicle_api(vehicle: VehicleOut):
    result = create_vehicle_db(vehicle)
    return result_message(result)


@trim_router.post("/create_trim", response_model=SpecsRead)
def create_trim_api(trim: Specs):
    result = add_specs_db(trim)
    return result_message(result)

@vehicle_router.get("/all", response_class=HTMLResponse)
def get_all_vehicles_api(request: Request):
    result = get_all_vehicles_db()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "vehicles": result})

@vehicle_router.get("/{vehicle_id}", response_class=HTMLResponse)
def get_vehicle_api(request: Request, vehicle_id: int=0):
     result = get_vehicle_db(vehicle_id)
     if not result:
         return RedirectResponse(url="/")
     return templates.TemplateResponse("vehicle_detail.html",
                                       {"request": request, "vehicle": result})


