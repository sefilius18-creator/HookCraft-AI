import streamlit as st
from openai import OpenAI

# 1. Pengaturan Halaman & Tema
st.set_page_config(page_title="HookCraft AI - Viral Hook Generator", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (Bikin Tampilan Mewah) ---
st.markdown("""
    <style>
    /* Mengubah warna background utama */
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        color: white;
    }
    /* Mengubah tampilan input box */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #334155 !important;
        color: white !important;
        border-radius: 10px !important;
        border: 1px solid #38bdf8 !important;
    }
    /* Tombol Utama yang Glowing */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #818cf8) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        border: none !important;
        padding: 0.5rem 2rem !important;
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4) !important;
        width: 100% !important;
    }
    /* Kotak Hasil AI */
    .result-box {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #38bdf8;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM KEAMANAN (PASSWORD RAHASIA) ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password salah! Silakan cek kembali file PDF dari Lynk.id Anda.")

if not st.session_state["authenticated"]:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🔒 HookCraft AI</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: center;'>Masukkan password akses eksklusif Anda:</p>", unsafe_allow_html=True)
    st.text_input("", type="password", key="password_input", on_change=check_password)
    st.stop() 

# --- HALAMAN UTAMA APLIKASI ---
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🚀 HookCraft AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Bikin 3 Detik Pertama Videomu Viral dalam Sekali Klik!</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout Input
col1, col2 = st.columns(2)
with col1:
    topik = st.text_input("💡 Topik Videomu", placeholder="Misal: Skincare murah")
with col2:
    gaya_bahasa = st.selectbox("🗣️ Gaya Bahasa", ["Anak Muda / Kasual", "Kontradiktif", "Misterius", "Edukasi Santai"])

jumlah_hook = st.select_slider("📊 Jumlah Hook", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Masukkan API Key Anda dulu!")
    elif not topik:
        st.warning("Isi topik videonya dulu!")
    else:
        with st.spinner("Sedang meracik ide viral..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter TikTok viral terbaik."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.success("🔥 Hook Viral Berhasil Dibuat:")
                st.markdown(response.choices[0].message.content)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
