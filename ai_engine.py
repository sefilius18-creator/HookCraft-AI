import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_hooks(
    topic,
    style,
    prompt_style,
    amount
):

    prompt = f"""
    Kamu adalah ahli hook TikTok.

    Topik:
    {topic}

    Gaya:
    {style}

    Instruksi:
    {prompt_style}

    Buat {amount} hook.

    Aturan:
    - Bahasa Indonesia
    - Maksimal 15 kata
    - Format bernomor
    - Viral
    - Memancing rasa penasaran
    """

    response = model.generate_content(prompt)

    return response.text
