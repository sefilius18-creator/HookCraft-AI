import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

def generate_content(prompt):

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"ERROR: {str(e)}"
