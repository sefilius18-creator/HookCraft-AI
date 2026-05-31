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

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Generator",
    "Analisis Hook",
    "Hook Scorer",
    "Script Generator",
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

    st.subheader("📈 Hook Scorer")

    hook_input = st.text_area(
        "Masukkan Hook yang ingin dinilai"
    )

    if st.button("Nilai Hook"):

        if not hook_input.strip():
            st.warning("Masukkan hook terlebih dahulu.")
        else:

            prompt = f"""
Kamu adalah pakar hook TikTok.

Nilai hook berikut:

{hook_input}

Aturan output:

# SKOR TOTAL
(0-100)

# DETAIL
Curiosity Gap: x/10
Emotional Trigger: x/10
Pattern Interrupt: x/10
CTR Potential: x/10

# KELEBIHAN
Maksimal 3 poin

# KEKURANGAN
Maksimal 3 poin

# VERSI LEBIH KUAT
Buat 3 versi hook yang lebih kuat.

Jawaban harus singkat dan langsung.
"""

            with st.spinner("Menganalisis hook..."):

                response = model.generate_content(
                    prompt
                )

                st.markdown(response.text)

with tab4:

    st.subheader("🎬 Script Generator")

    hook_script = st.text_area(
        "Masukkan Hook",
        placeholder="Contoh: Kulit glowing bukan karena serum, tapi karena ini"
    )

    duration = st.selectbox(
        "Durasi Video",
        [
            "30 Detik",
            "60 Detik",
            "90 Detik"
        ]
    )

    content_style = st.selectbox(
        "Gaya Konten",
        [
            "Edukasi",
            "Storytelling",
            "Affiliate",
            "Soft Selling",
            "Hard Selling"
        ]
    )

    if st.button("🎬 Buat Script Video"):

        if not hook_script.strip():
            st.warning("Masukkan hook terlebih dahulu.")
        else:

            prompt = f"""
            Kamu adalah script writer TikTok profesional.

            Buat script video berdasarkan:

            Hook:
            {hook_script}

            Durasi:
            {duration}

            Gaya:
            {content_style}

            FORMAT WAJIB:

            # HOOK

            # BODY

            # CTA

            # SHOT SUGGESTION

            Aturan:
            - Bahasa Indonesia
            - Natural
            - Tidak terdengar seperti AI
            - Cocok untuk TikTok
            - Fokus retensi penonton
            - Berikan script siap rekam
            """

            with st.spinner("Membuat script video..."):

                response = model.generate_content(
                    prompt
                )

                st.success(
                    "🎬 Script Siap Digunakan"
                )

                st.markdown(response.text)

                st.download_button(
                    "📥 Download Script",
                    response.text,
                    file_name="hookcraft_script.txt"
        )

with tab5:

    history = get_history()

    for row in history:

        st.expander(
            f"{row[0]} | {row[3]}"
        ).write(row[2])
