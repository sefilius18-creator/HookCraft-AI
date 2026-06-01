import streamlit as st
from database import *
from prompts import *
from ai_engine import *

# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="HookCraft AI",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# DATABASE
# =====================================

init_db()

FREE_LIMIT = 10
usage = get_daily_usage()

# =====================================
# CSS
# =====================================

st.markdown("""
<style>

.stApp{
    background:#F6F7FB;
}

.block-container{
    max-width:1400px;
    padding-top:1rem;
}

[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #E5E7EB;
}

.hero-card{
    background:white;
    border:1px solid #ECECEC;
    border-radius:24px;
    padding:30px;
    margin-bottom:25px;
}

.metric-card{
    background:white;
    border:1px solid #ECECEC;
    border-radius:20px;
    padding:20px;
}

.hook-card{
    background:white;
    border:1px solid #ECECEC;
    border-radius:16px;
    padding:18px;
    margin-bottom:12px;
}

.stButton button{
    width:100%;
    height:50px;
    border:none;
    border-radius:14px;
    background:linear-gradient(
        135deg,
        #6D28D9,
        #8B5CF6
    );
    color:white;
    font-weight:700;
}

.stDownloadButton button{
    width:100%;
    border-radius:14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🚀 HookCraft AI")

st.sidebar.metric(
    "Generate Hari Ini",
    f"{usage}/{FREE_LIMIT}"
)

st.sidebar.divider()

st.sidebar.info("""
🔥 AI Viral Content Toolkit

Generate:
- Hook
- Script
- Caption
- CTA
- Thumbnail Ideas
""")

# =====================================
# HERO
# =====================================

st.markdown("""
<div class="hero-card">

<h1 style="margin:0;">
⚡ HookCraft AI
</h1>

<p style="
color:#6B7280;
font-size:18px;
margin-top:10px;
">
Generate viral hooks, scripts, captions,
thumbnail ideas dan content analysis
menggunakan AI.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================
# TABS
# =====================================

tab1, tab2 = st.tabs([
    "🔥 Hook Generator",
    "📜 Riwayat"
])

# =====================================
# TAB 1
# =====================================

with tab1:

    st.subheader("Generate Viral Hook")

    col1, col2 = st.columns(2)

    with col1:
        topic = st.text_input(
            "Topik Konten"
        )

    with col2:
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

        with st.spinner(
            "Generating hooks..."
        ):

            result = generate_hooks(
                topic,
                style,
                HOOK_PROMPTS[style],
                amount
            )

            st.success(
                "🔥 Hook Siap Digunakan"
            )

            hooks = result.split("\n")

            for i, hook in enumerate(
                hooks,
                start=1
            ):

                if hook.strip():

                    st.markdown(
                        f"""
                        <div class="hook-card">
                        <b>{i}.</b> {hook}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

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

# =====================================
# TAB 2
# =====================================

with tab2:

    st.subheader("Riwayat Generate")

    history = get_history()

    if not history:

        st.info(
            "Belum ada riwayat."
        )

    else:

        for row in history:

            topic = row[0]
            style = row[1]
            result = row[2]
            created = row[3]

            with st.expander(
                f"{topic} | {style} | {created}"
            ):
                st.write(result)
