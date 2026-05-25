import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (KEMBALI KE SIMBOL LAMA + JUDUL REQUEST) ---
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
            radial-gradient(4px 4px at 10% 10%, #ffffff, transparent),
            radial-gradient(5px 5px at 50% 40%, #ffffff, transparent),
            radial-gradient(4px 4px at 80% 20%, #ffffff, transparent);
        background-size: 800px 1000px;
        animation: meteor-rain 10s linear infinite;
        opacity: 0.2;
        z-index: 0;
    }

    @keyframes meteor-rain {
        from { transform: translateY(-1000px); }
        to { transform: translateY(1000px); }
    }

    /* --- JUDUL: ROKET SAMPING, AI DI BAWAH (WARNA PUTIH) --- */
    .brand-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px;
        position: relative;
        z-index: 10;
    }

    .brand-top {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .brand-hookcraft {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin: 0;
    }

    .brand-ai {
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin-top: -15px;
    }

    .rocket-icon {
        font-size: 60px;
    }

    /* --- KOTAK DESKRIPSI GAYA LAMA (TANPA CEKLIS) --- */
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
        text-align: left;
        position: relative;
        z-index: 10;
    }

    .info-item {
        color: white;
        font-size: 1rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* --- TOMBOL BIRU GRADASI --- */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 15px !important;
        width: 100% !important;
        margin-top: 20px;
    }

    /* Input & Label */
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
    # Judul: Roket samping HookCraft, AI di bawah tengah
    st.markdown("""
        <div class="brand-container">
            <div class="brand-top">
                <span class="rocket-icon">🚀</span>
                <h1 class="brand-hookcraft">HookCraft</h1>
            </div>
            <div class="brand-ai">AI</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Kotak deskripsi dengan simbol ✨ (Bukan Ceklis)
    st.markdown("""
        <div class="info-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center; margin-bottom: 15px;'>CORE SYSTEM ACTIVE</p>
            <div class="info-item">✨ <b>Neural Hook Engine</b> — Viral content generator.</div>
            <div class="info-item">✨ <b>Deep Analysis</b> — Optimized for 2026 algorithms.</div>
            <div class="info-item">✨ <b>Psychology Hooks</b> — Based on viral patterns.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", on_change=do_login)
    st.button("MASUK KE SISTEM", on_click=do_login)
    st.stop()

# --- HALAMAN UTAMA ---
st.markdown("<h1 style='text-align:center; color:#38bdf8;'>🚀 HookCraft Dashboard</h1>", unsafe_allow_html=True)
st.success("Akses Diterima.")
