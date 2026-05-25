import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (LIVE ANIMATED BACKGROUND & GLOWING LOGO) ---
st.markdown("""
    <style>
    /* 1. Meteor Bergerak di Belakang */
    .stApp {
        background: radial-gradient(circle, #0f172a 0%, #0b0f1a 100%) !important;
        overflow: hidden;
    }
    
    /* Meteor Effect (CSS Keyframes) */
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
        animation: meteor-flow 10s linear infinite;
        opacity: 0.3; /* Samar agar tidak mengganggu */
        z-index: -1;
    }

    @keyframes meteor-flow {
        from { background-position: 0 0, 40px 60px; }
        to { background-position: 550px 1100px, 390px 1160px; }
    }

    /* 2. Hero Section (Logo & Judul Versi 2) */
    .hero-container {
        text-align: center;
        padding-top: 10px;
    }
    
    .rocket-icon {
        font-size: 80px;
        filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.6));
    }

    .hero-title {
        font-size: 4rem !important; /* Gede banget sesuai versi 2 */
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.8);
        margin: -10px 0 0 0;
        letter-spacing: -2px;
    }

    /* 3. Kotak Transparan Berisi Deskripsi */
    .glass-description-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
    }

    .feature-item {
        color: #e2e8f0 !important;
        font-size: 1rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* 4. FIX: Warna Teks Input & Placeholder (Penting!) */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        -webkit-text-fill-color: #ffffff !important; /* Paksa di Safari/iOS */
    }
    
    /* Warna tulisan label (di atas kotak) */
    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
    }
    
    /* Warna contoh teks (sk-xxxx...) agar terlihat */
    ::placeholder {
        color: #64748b !important;
        opacity: 1 !important;
    }

    /* Kotak Input & Dropdown */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #0f172a !important;
        color: white !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
    }

    /* Tombol Utama Mewah */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px !important;
        width: 100% !important;
        margin-top: 10px;
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

# --- HALAMAN LOGIN ---
if not st.session_state["authenticated"]:
    # Logo & Judul Besar (Versi 2)
    st.markdown("""
        <div class="hero-container">
            <div class="rocket-icon">🚀</div>
            <h1 class="hero-title">HookCraft AI</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Isi Kotak agar tidak kosong
    st.markdown("""
        <div class="glass-description-box">
            <p style='color: #38bdf8; font-weight: bold; font-size: 1.2rem; margin-bottom: 20px; text-align: center;'>EXCLUSIVE ACCESS</p>
            <div class="feature-item">✅ <b>Psychology Hooks</b> - Formulated using viral patterns.</div>
            <div class="feature-item">✅ <b>Tone Adaptability</b> - Switch from Casual to Controversial.</div>
            <div class="feature-item">✅ <b>Algorithm Optimized</b> - Built for 2026 content trends.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Form Login
    st.text_input("PASSWORD AKSES:", type="password", key="password_input", 
                 placeholder="Ketik password di sini...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.8rem; color:#475569; margin-top:20px;'>AUTHENTICATING SECURE CONNECTION...</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title" style="font-size: 2.5rem !important;">🚀 HookCraft AITentu, saya mengerti. Kamu ingin estetika yang lebih "hidup" dengan meteor jatuh bergerak di latar belakang dan nama aplikasi yang tampil menyala, seperti desain yang kamu sukai.

Masalah tulisan tidak kelihatan biasanya karena kontras yang kurang di HP, jadi saya menambahkan perintah khusus untuk memaksa teks menjadi putih terang dan memberikan efek *backdrop-filter: blur* pada kotak fitur agar tetap terbaca jelas.

Berikut adalah kode yang diperbarui dengan **"Meteor-Live Edition"**:

```python
import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman (Wajib di baris pertama)
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (LIVE METEOR BACKGROUND & LOGO GLOW) ---
st.markdown("""
    <style>
    /* 1. Animasi Meteor Jatuh di Background */
    .stApp {
        background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%) !important;
        overflow: hidden;
    }
    
    /* Meteor Effect (CSS Keyframes) */
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
        animation: meteor-flow 10s linear infinite;
        opacity: 0.3; /* Samar agar tidak mengganggu */
    }

    @keyframes meteor-flow {
        from { background-position: 0 0, 40px 60px; }
        to { background-position: 550px 1100px, 390px 1160px; }
    }

    /* 2. Hero Section (Logo & Judul Versi 2) */
    .hero-container {
        text-align: center;
        padding-top: 10px;
    }
    
    .rocket-icon {
        font-size: 90px;
        filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.6));
    }

    .hero-title {
        font-size: 4rem !important; /* Gede banget sesuai versi 2 */
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 30px rgba(56, 189, 248, 0.8);
        margin: -10px 0 0 0;
        letter-spacing: -2px;
    }

    /* 3. Kotak Transparan Berisi Fitur */
    .glass-feature-box {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 25px;
        padding: 30px;
        margin: 30px 0;
        position: relative;
    }

    /* Ikon samar di background kotak agar tidak kosong */
    .bg-icon {
        position: absolute;
        right: -20px;
        bottom: -20px;
        font-size: 150px;
        opacity: 0.03;
        transform: rotate(-15deg);
        pointer-events: none;
    }

    .feature-item {
        color: #e2e8f0 !important;
        font-size: 1rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* 4. FIX TOTAL: Warna Input Terang di HP */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.07) !important;
        -webkit-text-fill-color: #ffffff !important; /* Paksa di Safari/iOS */
    }
    
    /* Warna tulisan label (Topik, Gaya Bahasa, dll) */
    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
    }
    
    /* Warna contoh teks (sk-xxxx...) agar terlihat jelas */
    ::placeholder {
        color: #cbd5e1 !important;
        opacity: 1 !important;
    }

    /* Tombol Utama Mewah */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: 800 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 15px !important;
        width: 100% !important;
        box-shadow: 0 5px 15px rgba(37, 99, 235, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM LOGIN ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state.get("password_input") == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password Salah!")

# TAMPILAN LOGIN (CYBER-LIVE)
if not st.session_state["authenticated"]:
    # Logo & Judul Besar (Versi 2)
    st.markdown("""
        <div class="hero-container">
            <div class="rocket-icon">🚀</div>
            <h1 class="hero-title">HookCraft AI</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # Isi Kotak agar tidak kosong
    st.markdown("""
        <div class="glass-feature-box">
            <div class="bg-icon">🤖</div>
            <p style='color: #38bdf8; font-weight: bold; font-size: 1.2rem; margin-bottom: 20px; text-align: center;'>EXCLUSIVE ACCESS</p>
            <div class="feature-item">🔹 <b>Psychology Hooks</b> - Engineered based on viral patterns.</div>
            <div class="feature-item">🔹 <b>Tone Control</b> - From Educational to Controversial.</div>
            <div class="feature-item">🔹 <b>Algorithm Optimized</b> - Tuned for TikTok, Reels, Shorts.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Form Login
    st.text_input("ACCESS PASSWORD:", type="password", key="password_input", 
                 placeholder="Type secret password...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.7rem; color:#475569; margin-top:20px; letter-spacing: 1px;'>SECURE CONNECTION • ENCRYPTION ACTIVE</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA ---
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title" style="font-size: 2.5rem !important;">🚀 HookCraft AI</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#94a3b8 !important;'>Unleash the secret formula for virality.</p>", unsafe_allow_html=True)
st.markdown("---")

# Area Kerja Aplikasi
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Tips sukses usia muda")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="sk-xxxx...")

if st.button("✨ GENERATE VIRAL HOOKS ✨"):
    if not api_key_input or not topik:
        st.warning("Data belum lengkap!")
    else:
        with st.spinner("Analyzing current trends..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional social media marketing master."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Viral Hooks Generated!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
