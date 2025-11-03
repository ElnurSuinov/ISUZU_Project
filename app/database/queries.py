from app.database import get_db
from app.database.models import Vehicle, Trim
from app.api.vehicles.schemas import VehicleOut, Specs


def create_vehicle_db(vehicle_out: VehicleOut):
    db = next(get_db())
    vehicle_data = vehicle_out.model_dump()
    new_info = Vehicle(**vehicle_data)
    db.add(new_info)
    db.commit()
    return True


def add_specs_db(specs: Specs):
    db = next(get_db())
    specs_data = specs.model_dump()
    new_specs = Trim(**specs_data)
    db.add(new_specs)
    db.commit()
    return True


def get_vehicle_db(vehicle_id: int):
    db = next(get_db())
    vehicle = db.query(Vehicle).filter_by(id=vehicle_id).first()
    if vehicle:
        return vehicle
    return False


def get_all_vehicles_db():
    db = next(get_db())
    vehicles = db.query(Vehicle).all()
    if vehicles:
        return vehicles
    return False
