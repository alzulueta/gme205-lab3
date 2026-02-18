# GmE 205 Lab 3 Spatial Object Systems: Shapely, Inheritance, and Structured Data
# How to set up the virtual environment
1. Open the VS Code Terminal
2. Create the virtual environment: python3 -m venv .venv
3. Activate the environment: source .venv/bin/activate
4. Install packages: pip install pandas matplotlib
5. Saved installed packages: pip freeze > requirements.txt
# How to run Python scripts
Make sure the virtual environment is activated ((.venv) shows in the terminal)

## B.5 Conceptual Reflection
- The internal representation of Point changed from storing coordinates as separate .lon and .lat attributes to using a Shapely Point object stored in self.geometry.
- The external behavior of the class did not change: it still provides coordinate access, tuple conversion, and distance computation.
- All spatial computation now lives within the geometry object, allowing the Point class to delegate coordinate handling and distance calculations to Shapely.

## C.3.Verify Shared Behavior
3. The Point class does not define bbox() itself, but it inherits this method from SpatialObject. This allows a Point to call bbox(), and for a single point, the bounding box simply has the same min and max values.

## C.6 Conceptual Reflection
- SpatialObject is an abstraction because it represents the general concept of any object that exists in space, such as points, parcels, or buildings, without specifying details.
- Inheritance allows these classes to share common properties and methods, like geometry storage and bounding box computation, so the same code does not need to be rewritten in each class.
- Using a dictionary organizes semantic data in a flexible structure without defining how the object behaves.
- All subclasses automatically gain the new method because they inherit the behavior of the base class.
- It allows new spatial types to reuse existing structure and behavior, reducing duplication and making the system easier to extend.

# Reflection: Challenge Exercises
## Challenge 1 - from_dict() (Data -> Object Boundary)
1. from_dict() should delegate validation to the constructor because constructor is the single source of truth for creating valid objects. This is to avoid duplicating validation logic and ensurs consistency and any changes to coordinate rules only need to be updated in one place. It also naturally raise errors for invalid dictionaries without extra code in from_dict().
## Challenge 2 - as_dict() (Structured Output)
2. as_dict() is implemented inside the object because the object “owns” its data and knows its structure. Placing it inside the class keeps responsibility with the object rather than scattering logic in scripts like run_lab3.py. This makes the system more maintainable and object-oriented.
3. as_dict() must return only primitive data types (numbers, strings, booleans, tuples, dicts) because these types are JSON-serializable and can be easily exported or saved. Shapely geometry objects are complex and not directly serializable, so including them would break structured data output.
## Challenge 3 - intersects() in SpatialObject (Inheritance)
4. intersects() belongs in the base class because it is a spatial operation shared by all spatial objects. Defining it once in SpatialObject avoids duplication, simplifies maintenance, and ensures all subclasses automatically inherit it.
5. If you add a new spatial subclass like Building, no changes are required to support intersects() because it inherits all methods from SpatialObject. As long as Building has a geometry attribute, it automatically gains the ability to intersect with other spatial objects.