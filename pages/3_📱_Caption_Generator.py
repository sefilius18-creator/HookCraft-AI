import streamlit as st

from services.gemini_service import generate_content
from database.db import save_history

st.title("📱 Caption Generator")

topic = st.text_input(
    "Topik"
)

if st.button("Generate Caption"):

    prompt = f"""
Buat caption Instagram viral.

Topik:
{topic}

Tambahkan hashtag.
"""

    result = generate_content(prompt)

    st.write(result)

    save_history(
        "Caption Generator",
        prompt,
        result
    )
