from shapely.geometry import Polygon
from spatial import Parcel, Point

# Challenge 1: Point.from_dict()
valid_row = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}
invalid_row = {"id": "B", "lon": 999, "lat": 14.6, "name": "Invalid", "tag": "POI"}

try:
    p = Point.from_dict(valid_row)
    print("Successfully created Point from dictionary:")
    print("As dict:", {
        "id": p.id,
        "lon": p.geometry.x,
        "lat": p.geometry.y,
        "name": p.name,
        "tag": p.tag
    })
except ValueError as e:
    print("Failed to create Point:", e)

try:
    p_invalid = Point.from_dict(invalid_row)
    print("Successfully created Point from invalid dictionary (should not happen):")
    print(p_invalid.to_tuple())
except ValueError as e:
    print("Caught error for invalid dictionary:", e)

#Challenge 2: Dictionary Output: as_dict() (Structured Data Export)

print("\nPoint as dictionary:")
print(p.as_dict())

geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)

print("\nParcel as dictionary:")
print(parcel.as_dict())