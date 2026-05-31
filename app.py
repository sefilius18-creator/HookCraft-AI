import streamlit as st
from database import *
from prompts import *
from ai_engine import *

st.set_page_config(
    page_title="HookCraft AI v2.0",
    page_icon="🚀",
    layout="wide"
)

init_db()

FREE_LIMIT = 10

st.title("🚀 HookCraft AI v2.0")
st.caption("AI Hook Generator untuk TikTok, Reels & Shorts")

usage = get_daily_usage()

st.sidebar.markdown("## 📊 Status")
st.sidebar.metric(
    "Generate Hari Ini",
    f"{usage}/{FREE_LIMIT}"
)

tab1, tab2, tab3 = st.tabs([
    "Generator",
    "Analisis Hook",
    "Riwayat"
])

with tab1:

    topic = st.text_input(
        "Topik"
    )

    style = st.selectbox(
        "Tipe Hook",
        list(HOOK_PROMPTS.keys())
    )

    amount = st.slider(
        "Jumlah Hook",
        5,
        20,
        10
    )

    if st.button("✨ Generate Hook"):

        if usage >= FREE_LIMIT:
            st.error(
                "Kuota gratis hari ini habis."
            )
            st.stop()

        if not topic.strip():
            st.warning(
                "Masukkan topik terlebih dahulu."
            )
            st.stop()

        with st.spinner("Meracik hook..."):

            result = generate_hooks(
                topic,
                style,
                HOOK_PROMPTS[style],
                amount
            )

            st.success(
                "🔥 Hook Siap Digunakan"
            )

            st.markdown(result)

            save_history(
                topic,
                style,
                result
            )

            increase_usage()

            st.download_button(
                "📥 Download TXT",
                result,
                file_name="hookcraft_result.txt"
            )

with tab2:

    competitor = st.text_area(
        "Paste Hook Kompetitor"
    )

    if st.button(
        "🔍 Analisis Hook"
    ):

        analysis = generate_hooks(
            competitor,
            "Analisis",
            """
            Analisis:
            - Trigger psikologi
            - Curiosity gap
            - Kelebihan
            - Kekurangan
            - Skor 1-100
            """,
            1
        )

        st.write(analysis)

with tab3:

    history = get_history()

    for row in history:

        st.expander(
            f"{row[0]} | {row[3]}"
        ).write(row[2])
