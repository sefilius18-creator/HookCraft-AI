import streamlit as st

from services.gemini_service import generate_content
from database.db import save_history

st.title("📝 Script Generator")

hook = st.text_area(
    "Masukkan Hook",
    height=120
)

if st.button(
    "🚀 Generate Script",
    use_container_width=True
):

    if not hook:
        st.warning("Masukkan hook terlebih dahulu.")
        st.stop()

    prompt = f"""
Buat script video TikTok.

Hook:
{hook}

Format:

HOOK

BODY

CTA

Bahasa Indonesia.
"""

    with st.spinner(
        "Sedang membuat script..."
    ):

        result = generate_content(
            prompt
        )

    st.success(
        "Script berhasil dibuat"
    )

    st.text_area(
        "Hasil Script",
        value=result,
        height=450
    )

    save_history(
        "Script Generator",
        prompt,
        result
    )
