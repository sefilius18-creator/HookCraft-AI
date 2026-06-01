import streamlit as st

from services.gemini_service import generate_content
from database.db import save_history

st.title("📝 Script Generator")

hook = st.text_area(
    "Masukkan Hook"
)

if st.button("Generate Script"):

    prompt = f"""
Buat script video TikTok.

Hook:
{hook}

Format:

HOOK

BODY

CTA
"""

    result = generate_content(prompt)

    st.write(result)

    save_history(
        "Script Generator",
        prompt,
        result
    )
