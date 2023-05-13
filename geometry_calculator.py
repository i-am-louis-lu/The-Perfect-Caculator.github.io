import math
import streamlit as st

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius ** 2

def cube_volume(side):
    return side ** 3

def sphere_volume(radius):
    return 4 / 3 * math.pi * radius ** 3

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

def geometry_calculator():
    st.header("Geometry Calculator")
    
    # Define available shapes
    shapes = {
        "Triangle": ["base", "height"],
        "Rectangle": ["length", "width"],
        "Circle": ["radius"],
        "Cube": ["side"],
        "Sphere": ["radius"],
        "Cylinder": ["radius", "height"]
    }
    
    # Select shape to calculate
    shape = st.selectbox("Select a shape", list(shapes.keys()), index=0)
    
    # Get user inputs for shape calculation
    inputs = {}
    for input_name in shapes[shape]:
        inputs[input_name] = st.number_input(f"Enter {input_name}", value=0.0, step=None, format="%f", key=input_name)
    
    # Calculate area/volume based on selected shape
    if shape == "Triangle":
        result = triangle_area(inputs["base"], inputs["height"])
    elif shape == "Rectangle":
        result = rectangle_area(inputs["length"], inputs["width"])
    elif shape == "Circle":
        result = circle_area(inputs["radius"])
    elif shape == "Cube":
        result = cube_volume(inputs["side"])
    elif shape == "Sphere":
        result = sphere_volume(inputs["radius"])
    elif shape == "Cylinder":
        result = cylinder_volume(inputs["radius"], inputs["height"])
    
    # Display result to user
    st.write(f"{shape} area/volume: {result}")

if __name__ == "__main__":
    geometry_calculator()
