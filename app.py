import streamlit as st
from database import *
from prompts import *
from ai_engine import *

st.set_page_config(
    page_title="HookCraft AI v2.0",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

/* ===== GLOBAL ===== */

.stApp{
    background:#F8F8FC;
}

.block-container{
    padding-top:1rem;
    max-width:1600px;
}

/* ===== HEADER ===== */

h1{
    font-size:42px !important;
    font-weight:700 !important;
}

/* ===== SIDEBAR ===== */

[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #ECECEC;
}

[data-testid="stSidebar"] h2{
    color:#6D28D9;
}

[data-testid="stSidebar"] .stMetric{
    background:#F8F8FC;
    padding:15px;
    border-radius:12px;
}

/* ===== TABS ===== */

.stTabs [data-baseweb="tab-list"]{
    gap:10px;
}

.stTabs [data-baseweb="tab"]{
    background:white;
    border-radius:12px;
    padding:10px 18px;
    border:1px solid #ECECEC;
}

.stTabs [aria-selected="true"]{
    background:#7C3AED !important;
    color:white !important;
}

/* ===== INPUT ===== */

.stTextInput input,
.stTextArea textarea{
    border-radius:12px !important;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:12px;
}

/* ===== BUTTON ===== */

.stButton button{
    width:100%;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        135deg,
        #6D28D9,
        #8B5CF6
    );
    color:white;
    font-weight:600;
    height:48px;
}
import streamlit as st
from database import *
from prompts import *
from ai_engine import *

st.set_page_config(
    page_title="HookCraft AI v2.0",
    page_icon="🚀",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background:#F8F8FC;
}

.block-container{
    padding-top:1rem;
    max-width:1600px;
}

h1{
    font-size:42px !important;
    font-weight:700 !important;
}

[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #ECECEC;
}

[data-testid="stSidebar"] h2{
    color:#6D28D9;
}

[data-testid="stSidebar"] .stMetric{
    background:#F8F8FC;
    padding:15px;
    border-radius:12px;
}

.stTabs [data-baseweb="tab-list"]{
    gap:10px;
}

.stTabs [data-baseweb="tab"]{
    background:white;
    border-radius:12px;
    padding:10px 18px;
    border:1px solid #ECECEC;
}

.stTabs [aria-selected="true"]{
    background:#7C3AED !important;
    color:white !important;
}

.stTextInput input,
.stTextArea textarea{
    border-radius:12px !important;
}

.stButton button{
    width:100%;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        135deg,
        #6D28D9,
        #8B5CF6
    );
    color:white;
    font-weight:600;
    height:48px;
}

.hook-card{
    background:white;
    border:1px solid #ECECEC;
    border-radius:16px;
    padding:20px;
    margin-bottom:15px;
    box-shadow:0 2px 6px rgba(0,0,0,.04);
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATABASE
# =========================

init_db()

FREE_LIMIT = 10
usage = get_daily_usage()

# =========================
# HEADER
# =========================

st.title("⚡ HookCraft AI")
st.caption(
    "Generate viral hooks, scripts, captions, dan analisis konten dengan AI."
)

st.markdown("""
<div style="
background:white;
padding:25px;
border-radius:20px;
border:1px solid #ECECEC;
margin-bottom:20px;
">
<h2 style="margin:0;color:#111827;">
Generate Viral Hooks
</h2>

<p style="color:#6B7280;margin-top:10px;">
Create scroll-stopping hooks for your content in seconds.
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

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

    topic = st.text_input("Topik")

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
            st.error("Kuota gratis hari ini habis.")
            st.stop()

        if not topic.strip():
            st.warning("Masukkan topik terlebih dahulu.")
            st.stop()

        with st.spinner("Meracik hook..."):

            result = generate_hooks(
                topic,
                style,
                HOOK_PROMPTS[style],
                amount
            )

            st.success("🔥 Hook Siap Digunakan")

            hooks = result.split("\n")

            for i, hook in enumerate(hooks, start=1):

                if hook.strip():

                    st.markdown(f"""
                    <div class="hook-card">
                        <span style="
                        background:#F3F0FF;
                        color:#6D28D9;
                        padding:8px 12px;
                        border-radius:10px;
                        font-weight:700;
                        margin-right:10px;
                        ">
                        {i}
                        </span>

                        {hook}
                    </div>
                    """, unsafe_allow_html=True)

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

st.divider()

st.subheader("🔥 Need More? Try Other AI Tools")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.info("""
    ✍ Hook Rewriter

    Rewrite your hook to make it stronger.
    """)

with c2:
    st.info("""
    📢 CTA Generator

    High converting CTA generator.
    """)

with c3:
    st.info("""
    🖼 Thumbnail Analyzer

    Analyze CTR potential.
    """)

with c4:
    st.info("""
    🚀 Explore All Tools

    Access premium features.
    """)

with tab9:

    history = get_history()

    for row in history:

        st.expander(
            f"{row[0]} | {row[3]}"
        ).write(row[2])
