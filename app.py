import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman (Harus di baris pertama)
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (PREMIUM MOBILE FIX) ---
st.markdown("""
    <style>
    /* Latar Belakang Digital Mewah dengan Meteor yang Lebih Besar */
    .stApp {
        background-color: #0f172a !important;
        background-image: 
            radial-gradient(circle, #1e293b 0%, #0f172a 100%) !important;
        position: relative;
        overflow: hidden;
    }
    
    /* FIX: MEMPERBESAR DAN MEMPERJELAS METEOR */
    .stApp::after {
        content: "";
        position: absolute;
        top: -100px;
        left: 0;
        width: 100%;
        height: 100%;
        /* Menggunakan gradien yang lebih besar untuk efek meteor */
        background-image: 
            radial-gradient(white, rgba(255,255,255,.3) 4px, transparent 6px),
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px);
        background-size: 800px 800px, 450px 450px;
        background-position: 0 0, 80px 100px;
        animation: meteor-flow-large 12s linear infinite;
        opacity: 0.4; /* Meningkatkan opasitas agar lebih terlihat di HP */
    }

    @keyframes meteor-flow-large {
        from { background-position: 0 0, 80px 100px; }
        to { background-position: 800px 1600px, 530px 1700px; }
    }

    /* FIX: MENGEMBALIKAN JUDUL & ROKET V1 YANG LEBIH BAGUS */
    .hero-title {
        font-size: 3rem !important; /* Ukuran besar seperti V1 */
        font-weight: 800 !important;
        color: #38bdf8 !important;
        text-align: center;
        margin-top: 10px;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.5); /* Efek glow V2 tapi teks V1 */
    }
    
    .rocket-main {
        font-size: 80px;
        filter: drop-shadow(0 0 15px #38bdf8);
        text-align: center;
    }

    /* FIX: MEMASTIKAN TEKS INPUT DAN PLACEHOLDER TERLIHAT JELAS */
    input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important; /* Paksa di iPhone/iOS */
    }
    
    ::placeholder {
        color: #94a3b8 !important; /* Abu-abu terang agar terbaca di background gelap */
        opacity: 1 !important;
    }
    
    /* Warna tulisan label (di atas kotak) */
    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
    }

    /* Kotak Input & Dropdown */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
    }

    /* Tombol Utama Mewah */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px !important;
        width: 100% !important;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM LOGIN ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state.pwd_input == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password Salah!")

# --- HALAMAN LOGIN (KOTAK DIISI, LOGO V1, METEOR GEDE) ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div style="text-align: center; margin-top: 30px;">
            <div class="rocket-main">🚀</div>
            <h1 class="hero-title">HookCraft AI</h1>
        </div>
        
        <div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 20px; padding: 30px; margin: 30px 0;">
            <p style='color: #38bdf8; font-weight: bold; font-size: 1.2rem; text-align: center; margin-bottom: 20px;'>CORE SYSTEM ACTIVE</p>
            <div style='color: white; font-size: 1rem; margin-bottom: 12px;'>🔥 <b>Neural Hook Engine</b> - Creating attention-grabbing openers.</div>
            <div style='color: white; font-size: 1rem; margin-bottom: 12px;'>🧠 <b>Psychology Hooks</b> - Formulated based on viral patterns.</div>
            <div style='color: white; font-size: 1rem; margin-bottom: 12px;'>📊 <b>Deep Analysis</b> - Optimized for 2026 Viral Algorithms.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="pwd_input", on_change=check_password)
    st.markdown("<p style='text-align:center; font-size:0.8rem; color:#475569; margin-top:20px;'>AUTHENTICATING SECURE CONNECTION...</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SETELAH LOGIN) ---
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🚀 Control Center</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#94a3b8;'>Berhasil login! Mulai viral hari ini.</p>", unsafe_allow_html=True)
st.markdown("---")

# Area Kerja Aplikasi
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Tips hemat anak kos")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password", placeholder="sk-xxxx...")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Silakan masukkan API Key OpenAI Anda dulu!")
    elif not topik:
        st.warning("Silakan tulis topik videonya ya.")
    else:
        with st.spinner("Meracik ide..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional social media marketing master."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.info("🔥 Ini racikan hook viral untukmu:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
