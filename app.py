import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS ---
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

    /* --- STRUKTUR BRAND BARU --- */
    .brand-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 30px;
        position: relative;
        z-index: 10;
        margin-top: 20px;
    }
    
    .brand-row {
        display: flex;
        align-items: center;
        gap: 15px; /* Jarak roket ke tulisan */
    }

    .rocket-icon { font-size: 50px; }

    .brand-hookcraft {
        font-size: 3.5rem;
        font-weight: 800;
        color: #ffffff !important; /* Warna Putih */
        margin: 0;
    }

    .brand-ai {
        font-size: 2.5rem;
        font-weight: 800;
        color: #ffffff !important; /* Warna Putih */
        margin-top: -5px;
    }

    /* Kotak Deskripsi */
    .info-box {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
        position: relative;
        z-index: 10;
        text-align: left;
    }

    .info-item { color: white; margin-bottom: 15px; display: flex; align-items: center; gap: 12px; }

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

# --- LOGIN LOGIC ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def do_login():
    if st.session_state.pwd_input == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Password Salah!")

# --- TAMPILAN ---
if not st.session_state["authenticated"]:
    # Judul dengan Roket di samping HookCraft dan AI di bawahnya
    st.markdown("""
        <div class="brand-container">
            <div class="brand-row">
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
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", placeholder="Masukkan password...", on_change=do_login)
    st.button("MASUK KE SISTEM", on_click=do_login)
    st.stop()

st.success("Akses Diterima.")
