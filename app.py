import streamlit as st
from openai import OpenAI

# 1. Pengaturan Halaman
st.set_page_config(page_title="HookCraft AI - Viral Hook Generator", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (VERSI FIX JUDUL BESAR & MEWAH) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
    }
    
    /* JUDUL UTAMA - Bikin Gede & Glowing */
    h1 {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        color: #00d2ff !important;
        text-align: center !important;
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
        text-shadow: 0 0 20px rgba(0, 210, 255, 0.3);
    }
    
    /* SUBJUDUL */
    .subtitle {
        color: #94a3b8 !important;
        text-align: center !important;
        font-size: 1.2rem !important;
        margin-bottom: 30px !important;
    }
    
    /* Label Input (Tulisan di atas kotak) */
    label p {
        color: #38bdf8 !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
    
    /* Input Box */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #334155 !important;
        border-radius: 12px !important;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #00d2ff !important;
    }
    
    /* Tombol Utama */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 12px !important;
        margin-top: 20px !important;
        width: 100% !important;
        box-shadow: 0 10px 20px rgba(0, 210, 255, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM KEAMANAN ---
PASSWORD_RAHASIA = "Sefilius18"
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password salah!")

if not st.session_state["authenticated"]:
    st.markdown("<h1>🔒 HookCraft AI</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Akses Terbatas untuk Member Eksklusif</p>", unsafe_allow_html=True)
    st.text_input("Masukkan Password Akses:", type="password", key="password_input", on_change=check_password)
    st.stop() 

# --- HALAMAN UTAMA ---
st.markdown("<h1>🚀 HookCraft AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Bikin 3 Detik Pertama Videomu Viral!</p>", unsafe_allow_html=True)
st.markdown("---")

topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Cara cuan dari HP")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif", "Misterius (Kepo)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Mau berapa pilihan hook?", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password", placeholder="sk-xxxx...")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Masukkan API Key Anda dulu!")
    elif not topik:
        st.warning("Isi dulu topik videonya.")
    else:
        with st.spinner("Meracik ide viral..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter viral. Berikan hook pendek dan tajam dalam Bahasa Indonesia."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Hasil Racikan HookCraft AI:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")
