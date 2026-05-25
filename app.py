import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (METEOR JATUH & JUDUL MENYALA) ---
st.markdown("""
    <style>
    /* Latar Belakang Gelap */
    .stApp {
        background-color: #0b0f1a !important;
    }

    /* Animasi Meteor Jatuh */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: transparent;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 150px 150px, #38bdf8, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 300px 100px, #ffffff, rgba(0,0,0,0));
        background-size: 400px 600px;
        animation: meteor-animation 8s linear infinite;
        z-index: 0;
    }

    @keyframes meteor-animation {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }

    /* Judul HookCraft AI (Versi Gambar yang Kamu Suka) */
    .hero-container {
        text-align: center;
        padding: 10px;
        position: relative;
        z-index: 10;
    }

    .hero-title {
        font-size: 4rem !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.9);
        margin: 0;
        line-height: 1.1;
    }

    /* Kotak Transparan Berisi Fitur */
    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 20px;
        padding: 25px;
        margin: 20px 0;
        position: relative;
        z-index: 10;
    }

    /* Memaksa Teks Input Putih Terang */
    input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
    }

    /* Tombol Biru */
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

# --- LOGIKA LOGIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    if st.session_state.pwd_input == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Password Salah!")

# --- TAMPILAN LOGIN ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div class="hero-container">
            <div style="font-size: 80px;">🚀</div>
            <h1 class="hero-title">HookCraft<br>AI</h1>
        </div>
        <div class="glass-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center;'>SYSTEM CAPABILITIES</p>
            <p style='color: white;'>✨ <b>Neural Hook Engine</b> — Viral content generator.</p>
            <p style='color: white;'>📊 <b>Deep Analysis</b> — Optimized for 2026 algorithms.</p>
            <p style='color: white;'>🎭 <b>Multi-Tone</b> — Adapts to any creator personality.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", on_change=login)
    st.button("MASUK", on_click=login)
    st.stop()

# --- HALAMAN UTAMA ---
st.markdown("<h1 style='text-align:center; color:#38bdf8;'>🚀 Control Center</h1>", unsafe_allow_html=True)
st.write("Berhasil login! Selamat datang.")
