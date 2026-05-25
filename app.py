import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (LIVE ANIMATED BACKGROUND & GLOWING LOGO) ---
st.markdown("""
    <style>
    /* Latar Belakang Gelap dengan Animasi Meteor */
    .stApp {
        background: radial-gradient(circle, #0f172a 0%, #0b0f1a 100%) !important;
        overflow: hidden;
    }
    
    /* Animasi Meteor Bergerak */
    .stApp::after {
        content: "";
        position: absolute;
        top: -100px;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px);
        background-size: 550px 550px, 350px 350px;
        background-position: 0 0, 40px 60px;
        animation: meteor-flow 15s linear infinite;
        opacity: 0.2; 
        z-index: -1;
    }

    @keyframes meteor-flow {
        from { background-position: 0 0, 40px 60px; }
        to { background-position: 550px 1100px, 390px 1160px; }
    }

    /* Hero Section (Logo & Judul Bercahaya) */
    .hero-container {
        text-align: center;
        padding-top: 10px;
    }
    
    .rocket-icon {
        font-size: 80px;
        filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.6));
    }

    .hero-title {
        font-size: 4rem !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.8);
        margin: -10px 0 0 0;
        letter-spacing: -2px;
    }

    /* Kotak Transparan Berisi Konten */
    .glass-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
    }

    .info-text {
        color: #e2e8f0 !important;
        font-size: 0.95rem;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }

    /* Warna Teks Input (Putih Terang agar Kelihatan di HP) */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    
    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
    }

    /* Tombol Biru Gradasi */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px !important;
        width: 100% !important;
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
        st.error("❌ Password Salah!")

# --- TAMPILAN LOGIN ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div class="hero-container">
            <div class="rocket-icon">🚀</div>
            <h1 class="hero-title">HookCraft AI</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Kotak yang diisi dengan Deskripsi Fitur
    st.markdown("""
        <div class="glass-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center; margin-bottom: 15px;'>SYSTEM CAPABILITIES</p>
            <div class="info-text">✨ <b>Neural Hook Engine</b> — Viral content generator.</div>
            <div class="info-text">📊 <b>Deep Analysis</b> — Optimized for 2026 algorithms.</div>
            <div class="info-text">🎭 <b>Multi-Tone</b> — Adapts to any creator personality.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="password_input", 
                 placeholder="Masukkan password rahasia...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.7rem; color:#475569; margin-top:20px;'>AUTHENTICATING SECURE SESSION...</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🚀 Control Center</h1>", unsafe_allow_html=True)
topik = st.text_input("💡 Topik Videomu:", placeholder="Contoh: Tips sukses di usia muda")
# ... (lanjutkan kode input seperti biasa)
