import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (LIVE ANIMATED BACKGROUND & LOGO GLOW) ---
st.markdown("""
    <style>
    /* 1. Animasi Background Bergerak */
    .stApp {
        background: linear-gradient(-45deg, #0b0f1a, #1e293b, #0f172a, #0b0f1a) !important;
        background-size: 400% 400% !important;
        animation: gradientBG 15s ease infinite !important;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 2. Hero Section (Logo & Judul Versi 2 yang Kamu Suka) */
    .hero-container {
        text-align: center;
        padding-top: 10px;
    }
    
    .rocket-icon {
        font-size: 90px;
        filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.6));
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    .hero-title {
        font-size: 3.8rem !important; /* Ukuran besar seperti versi 2 */
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 30px rgba(56, 189, 248, 0.8);
        margin: -15px 0 0 0;
        letter-spacing: -2px;
    }

    /* 3. Kotak Transparan Berisi Fitur */
    .glass-feature-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 25px;
        padding: 30px;
        margin: 30px 0;
        position: relative;
        overflow: hidden;
    }

    /* Robot Bayangan di Background Kotak */
    .bg-robot {
        position: absolute;
        right: -20px;
        bottom: -20px;
        font-size: 120px;
        opacity: 0.05;
        transform: rotate(-15deg);
        pointer-events: none;
    }

    .feature-text {
        color: #e2e8f0 !important;
        font-size: 1rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* 4. Form Styling */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: 900 !important;
        border-radius: 15px !important;
        border: none !important;
        padding: 15px !important;
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.4);
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA AUTH ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state.get("password_input") == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Access Denied!")

# --- TAMPILAN LOGIN (CYBER-LIVE) ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div class="hero-container">
            <div class="rocket-icon">🚀</div>
            <h1 class="hero-title">HookCraft AI</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-feature-box">
            <div class="bg-robot">🤖</div>
            <p style='color: #38bdf8; font-weight: bold; font-size: 1.2rem; margin-bottom: 20px;'>SYSTEM OVERVIEW:</p>
            <div class="feature-text">✅ <b>Neural Hook Engine</b> - Generating high-retention hooks.</div>
            <div class="feature-text">✅ <b>Deep Analysis</b> - Optimized for 2026 Viral Algorithms.</div>
            <div class="feature-text">✅ <b>Multi-Tone</b> - Adaptive AI personality scaling.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("🔑 DECRYPT ACCESS KEY:", type="password", key="password_input", 
                 placeholder="Type secret password...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.7rem; color:#475569; margin-top:40px; letter-spacing: 2px;'>ENCRYPTION ACTIVE • SECURE CONNECTION</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA ---
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title" style="font-size: 2.5rem !important;">🚀 HookCraft AI</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:#94a3b8;'>The Master Key to Content Virality.</p>", unsafe_allow_html=True)
st.markdown("---")

# Form Input
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Cara cuan dari HP")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="sk-xxxx...")

if st.button("✨ GENERATE VIRAL HOOKS ✨"):
    if not api_key_input or not topik:
        st.warning("Data belum lengkap!")
    else:
        with st.spinner("Analyzing trends..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a viral hook master."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Viral Hooks Generated!")
                st.markdown(f"""
                <div class="glass-feature-box" style="margin-top:10px;">
                {response.choices[0].message.content}
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
