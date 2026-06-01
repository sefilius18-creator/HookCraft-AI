import streamlit as st

from services.gemini_service import generate_content
from database.db import save_history

st.title("📱 Caption Generator")

topic = st.text_input(
    "Topik Konten"
)

if st.button(
    "🚀 Generate Caption",
    use_container_width=True
):

    if not topic:
        st.warning("Masukkan topik.")
        st.stop()

    prompt = f"""
Buat caption Instagram viral.

Topik:
{topic}

Tambahkan hashtag relevan.

Bahasa Indonesia.
"""

    with st.spinner(
        "Sedang membuat caption..."
    ):

        result = generate_content(
            prompt
        )

    st.success(
        "Caption berhasil dibuat"
    )

    st.text_area(
        "Hasil Caption",
        value=result,
        height=300
    )

    save_history(
        "Caption Generator",
        prompt,
        result
    )
