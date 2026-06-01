import streamlit as st

from services.gemini_service import generate_content
from services.prompts import hook_prompt
from database.db import save_history

st.title("🎯 Hook Generator")

topic = st.text_input(
    "Topik Konten"
)

hook_type = st.selectbox(
    "Tipe Hook",
    [
        "FOMO",
        "Curiosity",
        "Storytelling",
        "Problem"
    ]
)

if st.button("Generate Hook"):

    prompt = hook_prompt(
        topic,
        hook_type
    )

    result = generate_content(prompt)

    st.write(result)

    save_history(
        "Hook Generator",
        prompt,
        result
    )
