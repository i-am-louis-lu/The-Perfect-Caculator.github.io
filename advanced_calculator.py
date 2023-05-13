import os
import math
import streamlit as st
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the available options in the dropdown menu
options = {
    "Advanced Calculator": "advanced_calculator",
    "Geometry Calculator": "geometry_calculator",
    "Word Problem Solver": "word_problem_solver"
}

# Set the default option in the dropdown menu
default_option = "advanced_calculator"

# Create the dropdown menu with the options and default option
selected_option = st.sidebar.selectbox("Select an option", options.keys(), index=list(options.values()).index(default_option))

# Conditionally execute code based on the selected option
if options[selected_option] == "advanced_calculator":
    def calculator():
        st.header("Advanced Calculator")
        
        # Get user inputs for calculation
        num1 = st.number_input("Enter first number", value=0.0, step=None, format="%f", key="num1")
        num2 = st.number_input("Enter second number", value=0.0, step=None, format="%f", key="num2")
        
        # Define available operations
        operations = {
            "Addition": "+",
            "Subtraction": "-",
            "Multiplication": "*",
            "Division": "/",
            "Exponentiation": "**",
            "Modulus": "%",
            "Floor Division": "//",
            "Logarithm": "log",
            "Square Root": "sqrt",
            "Trigonometry": "trig"
        }
        
        # Select operation to perform
        operation = st.selectbox("Select operation", list(operations.keys()), index=0)
        
        # Calculate result based on selected operation
        if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Modulus", "Floor Division"]:
            result = eval(f"{num1} {operations[operation]} {num2}")
        elif operation == "Logarithm":
            result = math.log(num2, num1)
        elif operation == "Square Root":
            result = math.sqrt(num1)
        elif operation == "Trigonometry":
            trig_operations = {
                "Sine": "sin",
                "Cosine": "cos",
                "Tangent": "tan",
                "Inverse Sine": "asin",
                "Inverse Cosine": "acos",
                "Inverse Tangent": "atan",
                "Hyperbolic Sine": "sinh",
                "Hyperbolic Cosine": "cosh",
                "Hyperbolic Tangent": "tanh",
                "Inverse Hyperbolic Sine": "asinh",
                "Inverse Hyperbolic Cosine": "acosh",
                "Inverse Hyperbolic Tangent": "atanh"
            }
            trig_operation = st.selectbox("Select operation", list(trig_operations.keys()), index=0)
            result = eval(f"math.{trig_operations[trig_operation]}(num1)")
            
        # Display result to user
        st.write(f"Result: {result}")
    
    if __name__ == "__main__":
        calculator()