import database
from database import models

db = database.SessionLocal()

dmax = models.Vehicle(
    name="ISUZU D-MAX",
    type="Truck",
    year=2025,
    price=35000,
    description="The ISUZU D-MAX 2025 is a rugged, reliable pickup truck with powerful diesel performance.",
    model3d="dmax.glb"
)

# --- Add trims with unique specs and colors ---
sahara = models.Trim(
    name="Sahara",
    price=42000,
    engine="3.0L Turbo Diesel",
    transmission="6-Speed Automatic",
    drive_type="4x4",
    specs={
        "Power": "190 hp @ 3600 rpm",
        "Torque": "450 Nm @ 1600–2600 rpm",
        "Fuel Consumption": "8.0 L/100 km",
        "Ground Clearance": "240 mm",
        "Towing Capacity": "3500 kg",
        "Infotainment": "9-inch touchscreen, Apple CarPlay/Android Auto",
        "Safety": "6 airbags, Lane Assist, Hill Descent Control"
    },
    colors=["#ffffff", "#4f4f4f", "#1a3b8b", "#8b0000"],  # 🔹 Sahara colors
    vehicle=dmax
)

oksus = models.Trim(
    name="Oksus",
    price=37000,
    engine="1.9L Turbo Diesel",
    transmission="6-Speed Manual",
    drive_type="4x2",
    specs={
        "Power": "150 hp @ 3600 rpm",
        "Torque": "350 Nm @ 1800–2600 rpm",
        "Fuel Consumption": "7.3 L/100 km",
        "Ground Clearance": "235 mm",
        "Towing Capacity": "3000 kg",
        "Infotainment": "7-inch touchscreen, Bluetooth, USB",
        "Safety": "Dual airbags, ABS, EBD"
    },
    colors=["#ffffff", "#c0c0c0", "#6e6e6e"],  # 🔹 Oksus colors
    vehicle=dmax
)

db.add(dmax)
db.add_all([sahara, oksus])
db.commit()
db.close()

print("✅ ISUZU D-MAX and trims added successfully!")
