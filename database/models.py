from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base


class Trim(Base):
    __tablename__ = "trims"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    price = Column(Float)
    engine = Column(String(100))
    transmission = Column(String(100))
    drive_type = Column(String(50))
    specs = Column(JSON)   # unique specs per complectation
    colors = Column(JSON)  # 👈 allowed colors per complectation
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))

    vehicle = relationship("Vehicle", back_populates="trims")


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    type = Column(String(50))
    year = Column(Integer)
    price = Column(Float)
    img = Column(String)
    description = Column(String)
    model3d = Column(String(255))  # path to .glb file

    trims = relationship("Trim", back_populates="vehicle")
