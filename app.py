import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (DIPERBAIKI AGAR TIDAK PUTIH) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f1a !important;
    }

    /* Animasi Meteor */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            radial-gradient(4px 4px at 10% 10%, #ffffff, transparent),
            radial-gradient(6px 6px at 50% 40%, #ffffff, transparent),
            radial-gradient(4px 4px at 80% 20%, #ffffff, transparent);
        background-size: 800px 1000px;
        animation: meteor-rain 12s linear infinite;
        opacity: 0.2;
        z-index: 0;
    }

    /* Layout Judul Putih */
    .brand-container {
        display: flex;
        flex-direction: column;
        align-items: center;
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
        font-size: 3.5rem;
        font-weight: 800;
        color: #ffffff;
        margin: 0;
    }

    .brand-ai {
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        margin-top: -10px;
    }

    .rocket-icon { font-size: 60px; }

    /* Kotak Deskripsi */
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
        position: relative;
        z-index: 10;
    }

    .info-item {
        color: white;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    /* Tombol Biru */
    div.stButton > button {
        background: linear-gradient(90deg, #38bdf8, #2563eb);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 15px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def do_login():
    if st.session_state.pwd_input == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Password Salah!")

# --- TAMPILAN ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div class="brand-container">
            <div class="brand-top">
                <div class="rocket-icon">🚀</div>
                <h1 class="brand-hookcraft">HookCraft</h1>
            </div>
            <div class="brand-ai">AI</div>
        </div>
        <div class="info-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center; margin-bottom: 20px;'>CORE SYSTEM ACTIVE</p>
            <div class="info-item">🔹 <b>Neural Hook Engine</b> — Viral content generator.</div>
            <div class="info-item">🔹 <b>Deep Analysis</b> — Optimized for 2026 algorithms.</div>
            <div class="info-item">🔹 <b>Psychology Hooks</b> — Based on viral patterns.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", on_change=do_login)
    st.button("MASUK KE SISTEM", on_click=do_login)
    st.stop()

st.success("Akses Diterima.")
