import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (PREMIUM MINIMALIST) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f1a !important;
    }

    /* Animasi Meteor Besar */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(5px 5px at 10% 10%, #ffffff, transparent),
            radial-gradient(4px 4px at 50% 40%, #ffffff, transparent),
            radial-gradient(6px 6px at 80% 20%, #ffffff, transparent),
            radial-gradient(4px 4px at 30% 70%, #ffffff, transparent);
        background-size: 800px 1000px;
        animation: meteor-rain 8s linear infinite;
        opacity: 0.3;
        z-index: 0;
    }

    @keyframes meteor-rain {
        from { transform: translateY(-1000px); }
        to { transform: translateY(1000px); }
    }

    /* Struktur Nama Aplikasi */
    .brand-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
    }

    .brand-top {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .brand-hookcraft {
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        color: #ffffff !important; /* Warna Putih */
        margin: 0;
        letter-spacing: -1px;
    }

    .brand-ai {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #ffffff !important; /* Warna Putih */
        margin-top: -10px;
    }

    .rocket-icon {
        font-size: 55px;
    }

    /* Kotak Deskripsi */
    .info-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-top: 10px;
        z-index: 10;
        position: relative;
    }

    /* Input Styling */
    input {
        color: #ffffff !important;
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    
    label p { color: #ffffff !important; opacity: 0.8; }

    .stButton>button {
        background: #ffffff !important;
        color: #0b0f1a !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM LOGIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def handle_login():
    if st.session_state.pwd_input == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Akses Ditolak!")

# --- TAMPILAN LOGIN ---
if not st.session_state["authenticated"]:
    # Desain Header Sesuai Permintaan
    st.markdown("""
        <div class="brand-container">
            <div class="brand-top">
                <span class="rocket-icon">🚀</span>
                <h1 class="brand-hookcraft">HookCraft</h1>
            </div>
            <div class="brand-ai">AI</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="info-box">
            <p style='color: white; font-weight: bold; text-align: center; margin-bottom: 10px;'>CORE SYSTEM ACTIVE</p>
            <p style='color: #94a3b8; font-size: 0.9rem; text-align: center;'>Generating high-retention hooks optimized for 2026 algorithms.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", on_change=handle_login)
    st.button("MASUK KE SISTEM", on_click=handle_login)
    st.stop()

# --- HALAMAN UTAMA ---
st.markdown("<h2 style='text-align: center; color: white;'>🚀 Dashboard</h2>", unsafe_allow_html=True)
st.success("Sistem Aktif. Selamat bekerja!")
