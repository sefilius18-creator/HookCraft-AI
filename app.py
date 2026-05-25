import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (ANTI PUTIH & METEOR GEDE) ---
st.markdown("""
    <style>
    /* Latar Belakang Dasar */
    .stApp {
        background-color: #0b0f1a !important;
    }

    /* Efek Meteor Besar */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: transparent;
        /* Membuat bulatan meteor lebih besar (8px) */
        background-image: 
            radial-gradient(4px 4px at 50px 100px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(3px 3px at 200px 300px, #38bdf8, rgba(0,0,0,0)),
            radial-gradient(5px 5px at 350px 500px, #ffffff, rgba(0,0,0,0)),
            radial-gradient(4px 4px at 100px 600px, #38bdf8, rgba(0,0,0,0));
        background-size: 600px 800px;
        animation: move-meteor 10s linear infinite;
        z-index: 0;
    }

    @keyframes move-meteor {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }

    /* Container Konten */
    .main-container {
        position: relative;
        z-index: 10;
        text-align: center;
    }

    /* Nama Aplikasi (Besar & Menyala Biru) */
    .app-title {
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 25px rgba(56, 189, 248, 1);
        margin: 0;
        line-height: 1;
    }

    /* Kotak Deskripsi */
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
        text-align: left;
    }

    /* Memaksa Teks Input Putih Terang */
    input {
        color: #ffffff !important;
        background-color: rgba(15, 23, 42, 0.8) !important;
        border: 1px solid #38bdf8 !important;
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
        padding: 15px !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM LOGIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def do_login():
    if st.session_state.pwd_input == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Password Salah!")

# --- HALAMAN LOGIN ---
if not st.session_state["authenticated"]:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 80px;">🚀</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="app-title">HookCraft AI</h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center; margin-bottom: 15px;'>CORE SYSTEM ACTIVE</p>
            <p style='color: white;'>✅ <b>Neural Hook Engine</b> — Viral content generator.</p>
            <p style='color: white;'>✅ <b>Deep Analysis</b> — Optimized for 2026 algorithms.</p>
            <p style='color: white;'>✅ <b>Psychology Hooks</b> — Based on viral patterns.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", placeholder="Masukkan password...", on_change=do_login)
    st.button("LOGIN SYSTEM", on_click=do_login)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown("<h1 style='text-align:center; color:#38bdf8;'>🚀 HookCraft Dashboard</h1>", unsafe_allow_html=True)
st.write("Selamat! Anda sudah masuk ke sistem.")
