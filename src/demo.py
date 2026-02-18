from spatial import Point

#p = Point("A", 121.0, 14.6)
#print(p.id, p.geometry.x, p.geometry.y)
#print("BBox:", p.bbox())

# ------------------------------------------------------------------
# Test to_tuple() instance method
# ------------------------------------------------------------------

#p = Point("A", 121.0, 14.6) 
#print(p.id, p.geometry.x, p.geometry.y) 
#print(p.to_tuple())

#print("Tuple:", p.to_tuple())

# ------------------------------------------------------------------
# Test distance_to() instance method (with AI support)
# ------------------------------------------------------------------
#p1 = Point("A", 121.0, 14.6)
#p2 = Point("B", 122.0, 15.0)

#distance = p1.distance_to(p2)
#print("Distance between p1 and p2:", distance, "meters")

from shapely.geometry import Polygon
from spatial import Parcel
# a simple rectangle polygon sample
geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

# Dictionary for added structure
attrs = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}
parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs)
print("Parcel BBox:", parcel.bbox())
print("Parcel Zone:", parcel.attributes["zone"])

# Challenge 1: Constructing from Dictionary: Point.from_dict(d)
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

