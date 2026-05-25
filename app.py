import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (ANIMATED ROBOT & GLOWING LOGO) ---
st.markdown("""
    <style>
    /* 1. Latar Belakang Digital Berdenyut */
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #0b0f1a 100%) !important;
        overflow: hidden;
    }

    /* 2. Robot Bergerak di Belakang */
    .robot-bg {
        position: fixed;
        top: 20%;
        left: 50%;
        transform: translateX(-50%);
        font-size: 250px;
        opacity: 0.1;
        z-index: -1;
        animation: robotMove 8s ease-in-out infinite;
        filter: blur(2px);
    }

    @keyframes robotMove {
        0% { transform: translateX(-50%) translateY(0px) rotate(0deg); }
        33% { transform: translateX(-45%) translateY(-20px) rotate(5deg); }
        66% { transform: translateX(-55%) translateY(10px) rotate(-5deg); }
        100% { transform: translateX(-50%) translateY(0px) rotate(0deg); }
    }

    /* 3. Judul HookCraft AI Besar & Menyala (Versi yang Kamu Suka) */
    .hero-container {
        text-align: center;
        padding: 20px 0;
    }
    
    .rocket-main {
        font-size: 80px;
        filter: drop-shadow(0 0 20px #38bdf8);
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 4rem !important; /* Ukuran besar sesuai gambar kedua */
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 25px rgba(56, 189, 248, 0.9), 0 0 50px rgba(56, 189, 248, 0.4);
        margin: 0;
        line-height: 1;
    }

    /* 4. Kotak Transparan dengan Border Menyala */
    .glass-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(56, 189, 248, 0.3);
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
    }

    /* Teks di dalam kotak agar tetap kontras */
    .feature-item {
        color: #ffffff !important;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 15px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }

    /* Input & Button Styling */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid #38bdf8 !important;
        font-size: 1.1rem !important;
    }

    .stButton>button {
        background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%) !important;
        color: white !important;
        font-weight: bold !important;
        padding: 15px !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4);
        width: 100%;
    }
    </style>
    
    <div class="robot-bg">🤖</div>
    """, unsafe_allow_html=True)

# --- LOGIKA AUTH ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state.get("password_input") == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Akses Ditolak!")

# --- HALAMAN LOGIN ---
if not st.session_state["authenticated"]:
    # Header Utama
    st.markdown("""
        <div class="hero-container">
            <div class="rocket-main">🚀</div>
            <h1 class="hero-title">HookCraft<br>AI</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Isi Kotak Transparan
    st.markdown("""
        <div class="glass-card">
            <p style='color: #38bdf8; font-weight: bold; font-size: 1.3rem; text-align: center; margin-bottom: 20px;'>CORE SYSTEM ACTIVE</p>
            <div class="feature-item">🔥 <b>Viral Hook Generator</b> - Create attention-grabbing openers.</div>
            <div class="feature-item">🧠 <b>Psychology-Based Tone</b> - From Mystery to Controversy.</div>
            <div class="feature-item">📊 <b>Algorithm Optimized</b> - Built for 2026 Social Media.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Form Login
    st.text_input("ENTER ACCESS KEY:", type="password", key="password_input", 
                 placeholder="Type your password...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:0.8rem; margin-top:20px;'>AUTHENTICATING SECURE CONNECTION...</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown("<h1 class='hero-title' style='font-size: 2.5rem !important; text-align:center;'>HookCraft AI</h1>", unsafe_allow_html=True)
st.markdown("---")

# Area Kerja Aplikasi
topik = st.text_input("💡 Apa topik videomu?", placeholder="Misal: Tips sukses usia muda")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="sk-xxxx...")

if st.button("🚀 GENERATE VIRAL HOOKS 🚀"):
    if not api_key_input or not topik:
        st.warning("Mohon isi semua data!")
    else:
        with st.spinner("Processing..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional social media master."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Selesai!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
