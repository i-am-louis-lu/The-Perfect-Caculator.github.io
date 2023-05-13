import os
import streamlit as st
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.header("Word Problem Solver")
def solve_word_problem(problem_text):
    prompt = f"Solve the following word problem:\n{problem_text}\nSolution:"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message

def main():
    st.title("Word Problem Solver")
    
    problem_text = st.text_input("Enter your word problem here:")
    
    if st.button("Solve"):
        solution = solve_word_problem(problem_text)
        st.write(solution)

if __name__ == "__main__":
    main()
