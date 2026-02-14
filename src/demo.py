from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.geometry.x, p.geometry.y)

# ------------------------------------------------------------------
# Test to_tuple() instance method
# ------------------------------------------------------------------

p = Point("A", 121.0, 14.6) 
print(p.id, p.geometry.x, p.geometry.y) 
print(p.to_tuple())

# ------------------------------------------------------------------
# Test distance_to() instance method (with AI support)
# ------------------------------------------------------------------
p1 = Point("A", 121.0, 14.6)
p2 = Point("B", 122.0, 15.0)

distance = p1.distance_to(p2)
print("Distance between p1 and p2:", distance, "meters")