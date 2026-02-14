#from spatial import Point

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

