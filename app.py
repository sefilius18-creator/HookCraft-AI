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

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Generator",
    "Analisis Hook",
    "Hook Scorer",
    "Script Generator",
    "Hook Rewriter PRO",
    "Thumbnail Analyzer",
    "CTA Optimizer",
    "Caption Generator",
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
Kamu adalah content strategist TikTok profesional.

Buat script berdasarkan:

HOOK:
{hook_script}

DURASI:
{duration}

GAYA:
{content_style}

ATURAN:

- Bahasa Indonesia
- Tidak terdengar seperti AI
- Maksimal sesuai durasi
- Langsung ke inti
- Cocok untuk TikTok/Reels/Shorts

FORMAT WAJIB:

# HOOK

(tampilkan hook)

# BODY

Buat 3-5 poin singkat.

# CTA

1 kalimat CTA.

# SHOT LIST

5 ide visual singkat.

Jangan membuat narasi presenter panjang.
Jangan membuat paragraf panjang.
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

    st.subheader("♻️ Hook Rewriter PRO")

    original_hook = st.text_area(
        "Masukkan Hook",
        key="pro_rewriter"
    )

    if st.button("🚀 Rewrite PRO"):

        prompt = f"""
        Kamu adalah copywriter TikTok elite.

        Hook asli:
        {original_hook}

        Buat:

        # FOMO
        5 hook

        # Curiosity
        5 hook

        # Storytelling
        5 hook

        # Affiliate
        5 hook

        # Soft Selling
        5 hook

        # Hard Selling
        5 hook

        # Shock Value
        5 hook

        Aturan:

        - Bahasa Indonesia
        - Maksimal 15 kata
        - Viral
        - Tidak generik
        - Output markdown rapi
        """

        with st.spinner("Mengoptimalkan hook..."):

            response = model.generate_content(prompt)

            st.markdown(response.text)

with tab6:

    st.subheader("🎯 Thumbnail Analyzer")

    thumbnail_text = st.text_input(
        "Masukkan Judul Thumbnail",
        key="thumbnail_analyzer"
    )

    if st.button("🎯 Analisis Thumbnail"):

        prompt = f"""
        Analisis thumbnail berikut:

        {thumbnail_text}

        Berikan:

        # CTR SCORE (0-100)

        # KELEBIHAN

        # KEKURANGAN

        # PSYCHOLOGY TRIGGER

        # 5 VERSI LEBIH KUAT

        Jawaban singkat dan profesional.
        """

        with st.spinner("Menganalisis thumbnail..."):

            response = model.generate_content(prompt)

            st.markdown(response.text)

with tab7:

    st.subheader("📢 CTA Optimizer")

    cta_input = st.text_area(
        "Masukkan CTA",
        key="cta_optimizer"
    )

    if st.button("📢 Optimalkan CTA"):

        prompt = f"""
        Analisis CTA berikut:

        {cta_input}

        Berikan:

        # ENGAGEMENT SCORE

        # KELEBIHAN

        # KEKURANGAN

        # FOLLOW CTA

        # COMMENT CTA

        # SHARE CTA

        # SAVE CTA

        # AFFILIATE CTA

        Buat lebih kuat dan natural.
        """

        with st.spinner("Mengoptimalkan CTA..."):

            response = model.generate_content(prompt)

            st.markdown(response.text)

with tab8:

    st.subheader("📝 Caption Generator")

    caption_topic = st.text_input(
        "Topik Konten",
        key="caption_generator"
    )

    caption_style = st.selectbox(
        "Gaya Caption",
        [
            "Affiliate",
            "Storytelling",
            "Edukasi",
            "Soft Selling",
            "Hard Selling"
        ]
    )

    if st.button("📝 Generate Caption"):

        prompt = f"""
        Buat caption TikTok profesional.

        Topik:
        {caption_topic}

        Gaya:
        {caption_style}

        Format:

        # CAPTION

        # CTA

        # HASHTAG

        Aturan:

        - Bahasa Indonesia
        - Maksimal 150 kata
        - Natural
        - Tidak terdengar seperti AI
        - 10 hashtag relevan
        """

        with st.spinner("Membuat caption..."):

            response = model.generate_content(prompt)

            st.markdown(response.text)

with tab9:

    history = get_history()

    for row in history:

        st.expander(
            f"{row[0]} | {row[3]}"
        ).write(row[2])
