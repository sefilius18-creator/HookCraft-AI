import streamlit as st

from services.gemini_service import generate_content
from services.prompts import hook_prompt
from database.db import save_history

st.set_page_config(
    page_title="Hook Generator",
    page_icon="🎯"
)

st.title("🎯 Hook Generator")

st.markdown(
    "Buat hook viral untuk TikTok, Reels, dan Shorts."
)

topic = st.text_input(
    "Topik Konten",
    placeholder="Contoh: Affiliate Shopee untuk pemula"
)

hook_type = st.selectbox(
    "Tipe Hook",
    [
        "FOMO",
        "Curiosity",
        "Storytelling",
        "Problem",
        "Affiliate"
    ]
)

if st.button(
    "🚀 Generate Hook",
    use_container_width=True
):

    if not topic:
        st.warning("Masukkan topik terlebih dahulu.")
        st.stop()

    prompt = hook_prompt(
        topic,
        hook_type
    )

    with st.spinner(
        "Sedang membuat hook viral..."
    ):

        result = generate_content(prompt)

    st.success("Hook berhasil dibuat")

    st.text_area(
        "Hasil",
        value=result,
        height=350
    )

    save_history(
        "Hook Generator",
        prompt,
        result
    )
