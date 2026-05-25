import streamlit as st
import random # Digunakan untuk force refresh CSS

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS DENGAN FORCE REFRESH ---
# Kita menambahkan angka acak di akhir ID agar browser dipaksa memuat ulang CSS baru
ver = random.randint(1, 1000)

st.markdown(f"""
    <style>
    /* Latar Belakang Utama dengan Animasi Meteor yang Lebih Jelas */
    .stApp {{
        background: #050b18 !important;
        background-image: 
            radial-gradient(circle at 50% 50%, #0f172a 0%, #050b18 100%) !important;
        position: relative;
    }}
    
    /* Layer Animasi Meteor (Menggunakan Pseudo-element) */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: transparent;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40px 70px, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 50px 160px, #ddd, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 90px 40px, #fff, rgba(0,0,0,0));
        background-size: 200px 200px;
        animation: stars-animation 10s linear infinite;
        opacity: 0.5;
        z-index: 0;
    }}

    @keyframes stars-animation {{
        from {{ transform: translateY(0); }}
        to {{ transform: translateY(200px); }}
    }}

    /* Container Utama agar Konten berada di atas Meteor */
    [data-testid="stVerticalBlock"] {{
        position: relative;
        z-index: 1;
    }}

    /* Judul HookCraft AI dengan Efek Glow */
    .hero-title {{
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #38bdf8 !important;
        text-align: center;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
        margin-top: -20px;
    }}

    /* Kotak Glassmorphism (System Capabilities) */
    .capabilities-box {{
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
    }}

    /* Memperbaiki Warna Input di Mobile */
    input {{
        color: white !important;
        -webkit-text-fill-color: white !important;
    }}

    /* CSS Version: {ver} */
    </style>
    """, unsafe_allow_html=True)

# --- HALAMAN LOGIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    # Logo Roket
    st.markdown("<h1 style='text-align: center; font-size: 80px; margin-bottom: 0;'>🚀</h1>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>HookCraft AI</div>", unsafe_allow_html=True)
    
    # Isi Box System Capabilities
    st.markdown("""
        <div class="capabilities-box">
            <p style='color: #38bdf8; font-weight: bold; text-align: center; font-size: 0.8rem; letter-spacing: 2px;'>SYSTEM CAPABILITIES</p>
            <div style='color: white; font-size: 0.9rem; margin: 10px 0;'>✨ <b>Neural Hook Engine</b> — Viral content generator.</div>
            <div style='color: white; font-size: 0.9rem; margin: 10px 0;'>📊 <b>Deep Analysis</b> — Optimized for 2026 algorithms.</div>
            <div style='color: white; font-size: 0.9rem; margin: 10px 0;'>🎭 <b>Multi-Tone</b> — Adapts to any creator personality.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Input Password
    pwd = st.text_input("PASSWORD AKSES:", type="password", placeholder="Ketik di sini...")
    
    if st.button("Masuk"):
        if pwd == "Sefilius18":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Password Salah!")
    st.stop()

# --- HALAMAN UTAMA ---
st.success("Akses Diterima. Selamat Datang!")
