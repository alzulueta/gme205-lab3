# GmE 205 Lab 3 Spatial Object Systems: Shapely, Inheritance, and Structured Data
# How to set up the virtual environment
1. Open the VS Code Terminal
2. Create the virtual environment: python3 -m venv .venv
3. Activate the environment: source .venv/bin/activate
4. Install packages: pip install pandas matplotlib
5. Saved installed packages: pip freeze > requirements.txt
# How to run Python scripts
Make sure the virtual environment is activated ((.venv) shows in the terminal)

## Conceptual Reflection
1. The internal representation of Point changed from storing coordinates as separate .lon and .lat attributes to using a Shapely Point object stored in self.geometry.
2. The external behavior of the class did not change: it still provides coordinate access, tuple conversion, and distance computation.
3. All spatial computation now lives within the geometry object, allowing the Point class to delegate coordinate handling and distance calculations to Shapely.