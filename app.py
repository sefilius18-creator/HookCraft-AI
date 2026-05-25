import streamlit as st
from openai import OpenAI

# 1. Pengaturan Halaman
st.set_page_config(page_title="HookCraft AI - Viral Hook Generator", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (Perbaikan Warna Tulisan agar Terang) ---
st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
    }
    
    /* Paksa semua tulisan label (Topik, Gaya Bahasa, dll) jadi Putih */
    label, .stMarkdown, p, span {
        color: white !important;
        font-weight: 500;
    }
    
    /* Perbaiki tampilan input box agar tulisan di dalamnya jelas */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        color: white !important;
        border: 1px solid #38bdf8 !important;
    }
    
    /* Tombol Utama Glowing */
    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #818cf8) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100% !important;
        margin-top: 10px;
    }
    
    /* Kotak Hasil */
    .result-box {
        background-color: #334155;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #38bdf8;
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
        st.error("❌ Password salah!")

if not st.session_state["authenticated"]:
    st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🔒 HookCraft AI</h1>", unsafe_allow_html=True)
    st.text_input("Masukkan Password Akses:", type="password", key="password_input", on_change=check_password)
    st.stop() 

# --- HALAMAN UTAMA APLIKASI ---
st.markdown("<h1 style='text-align: center; color: #38bdf8;'>🚀 HookCraft AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Bikin 3 Detik Pertama Videomu Viral!</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Pengguna (Dibuat vertikal agar lebih rapi di HP)
topik = st.text_input("💡 Apa topik atau tema videomu?", placeholder="Contoh: Tips hemat anak kos")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif", "Misterius", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Mau berapa pilihan hook?", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Masukkan API Key dulu!")
    elif not topik:
        st.warning("Topik tidak boleh kosong!")
    else:
        with st.spinner("Sedang meracik ide viral..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter TikTok viral. Buat hook yang sangat menarik dalam Bahasa Indonesia."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.success("🔥 Hook Viral Berhasil Dibuat:")
                st.write(response.choices[0].message.content)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
