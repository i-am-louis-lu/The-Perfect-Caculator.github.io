import streamlit as st
#from Calculator_Project.advanced_calculator import calculator as advanced_calculator
#from Calculator_Project.geometry_calculator import geometry_calculator
#from Calculator_Project.word_problem_solver import solve_word_problem

import advanced_calculator
import geometry_calculator
import word_problem_solver

# Define the available options in the dropdown menu
options = {
    "Advanced Calculator": "advanced_calculator",
    "Geometry Calculator": "geometry_calculator",
    "Word Problem Solver": "word_problem_solver"
}

# Set the default option in the dropdown menu
default_option = "advanced_calculator"

# Create the dropdown menu with the options and default option
selected_option = st.sidebar.selectbox("Select an option", options.keys(), index=list(options.values()).index(default_option), key="option_select")

# Conditionally execute code based on the selected option
if options[selected_option] == "advanced_calculator":
    advanced_calculator.calculator()
elif options[selected_option] == "geometry_calculator":
    geometry_calculator.geometry_calculator()
elif options[selected_option] == "word_problem_solver":
    problem_text = st.text_input("Enter your word problem here:")
    if st.button("Solve"):
        solution = word_problem_solver.solve_word_problem(problem_text)
        st.write(solution)
