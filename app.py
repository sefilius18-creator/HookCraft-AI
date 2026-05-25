import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman (Wajib di baris pertama)
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (OPTIMASI LAYAR HP & FIX TEKS) ---
st.markdown("""
    <style>
    /* Dasar Background */
    .stApp {
        background-color: #0f172a !important;
    }

    /* Judul Utama yang Tetap Gede & Nyala */
    .hero-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-align: center;
        margin-top: 20px;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
        line-height: 1;
    }

    /* Subtitle */
    .hero-sub {
        color: #94a3b8 !important;
        text-align: center;
        font-size: 1rem !important;
        margin-bottom: 30px;
    }

    /* FIX TOTAL UNTUK INPUT: Putih Terang, Tidak Boleh Transparan */
    input {
        color: #ffffff !important;
        background-color: #1e293b !important;
        -webkit-text-fill-color: #ffffff !important; /* Paksa untuk iPhone/Safari */
    }

    /* Warna Tulisan Label (Di atas kotak input) */
    label p {
        color: #38bdf8 !important;
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }

    /* Placeholder (Teks samar contoh) agar terlihat jelas */
    ::placeholder {
        color: #64748b !important;
        opacity: 1 !important;
    }

    /* Kotak Input & Dropdown */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
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
        margin-top: 10px;
    }
    
    /* Login Area */
    .login-box {
        padding: 30px;
        border-radius: 20px;
        background-color: #1e293b;
        border: 1px solid #38bdf8;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA LOGIN ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state.get("password_input") == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password Salah!")

# --- HALAMAN LOGIN (VERSI SOLID - ANTI POLOS) ---
if not st.session_state["authenticated"]:
    st.markdown('<p class="hero-title">🚀<br>HookCraft AI</p>', unsafe_allow_html=True)
    
    # Gunakan kontainer solid agar pasti terlihat di HP
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:white;'>Exclusive Access</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#94a3b8;'>Unlock the secret to viral content.</p>", unsafe_allow_html=True)
    
    st.text_input("PASSWORD AKSES:", type="password", key="password_input", 
                 placeholder="Ketik password di sini...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.7rem; color:#475569; margin-top:15px;'>Protected by HookCraft System</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SETELAH LOGIN) ---
st.markdown('<p class="hero-title">🚀<br>HookCraft AI</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">The Master Key to Content Virality.</p>', unsafe_allow_html=True)

# Input Section
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Cara diet tanpa lapar")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="Tempel sk-xxxx di sini")

if st.button("✨ GENERATE VIRAL HOOKS ✨"):
    if not api_key_input:
        st.error("Isi API Key dulu!")
    elif not topik:
        st.warning("Topik jangan kosong!")
    else:
        with st.spinner("Meracik ide..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah ahli viral marketing. Berikan hook yang sangat memicu rasa ingin tahu."},
                        {"role": "user", "content": f"Buat {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Hasil Untukmu:")
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #38bdf8; color: white;">
                {response.choices[0].message.content.replace('', '')}
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Masalah: {e}")
