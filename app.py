import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman Utama
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (DESAIN LOGIN EXCLUSIVE & UI MODERN) ---
st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }

    /* Styling Judul Besar */
    .main-title {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Container Halaman Login (Glassmorphism) */
    .login-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-top: 50px;
        text-align: center;
    }

    /* Memastikan Semua Label Terbaca (Warna Putih/Biru Terang) */
    label p {
        color: #38bdf8 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }

    /* Warna Teks Putih untuk Semua Markdown */
    .stMarkdown, p, span {
        color: #f8fafc !important;
    }

    /* Input Box */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
    }

    /* Tombol Utama Mewah */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 15px !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(0, 210, 255, 0.2) !important;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 25px rgba(0, 210, 255, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA LOGIN (SISTEM KEAMANAN) ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password salah! Silakan coba lagi.")

# Tampilan Jika Belum Login
if not st.session_state["authenticated"]:
    st.markdown('<h1 class="main-title">🔒 HookCraft AI</h1>', unsafe_allow_html=True)
    
    # Membuat Container Login yang Bagus
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown("### Welcome to the Inner Circle")
        st.markdown("Masukkan password akses Anda untuk mulai membuat konten viral.")
        st.text_input("Access Password:", type="password", key="password_input", on_change=check_password)
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop() 

# --- TAMPILAN HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown('<h1 class="main-title">🚀 HookCraft AI</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem;'>The Master Key to Content Virality.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Section
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Tips diet tanpa olahraga")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="sk-xxxx...")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ GENERATE VIRAL HOOKS ✨"):
    if not api_key_input:
        st.error("Silakan masukkan API Key Anda!")
    elif not topik:
        st.warning("Topik videonya diisi dulu ya.")
    else:
        with st.spinner("Meracik strategi viral..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter viral terbaik. Berikan hook yang sangat tajam dan pendek dalam Bahasa Indonesia."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Hasil Racikan HookCraft AI:")
                st.info(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Terjadi masalah teknis: {e}")
