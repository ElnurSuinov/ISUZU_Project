from pydantic import BaseModel
from typing import Optional, Union, List, Dict

class VehicleOut(BaseModel):
    id: int
    name: str
    type: str
    year: int
    price: float
    img: Optional[str]
    description: str
    model3d: str
    # specs: str

    class Config:
        orm_mode = True

class VehicleRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]

class Specs(BaseModel):
    name: str
    price: int
    engine: str
    transmission: str
    drive_type: str
    specs: Dict[str, str]
    colors: List[str]
    vehicle_id: int

    class Config:
        orm_mode = True

class SpecsRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]
