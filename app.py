import streamlit as st
from openai import OpenAI

# 1. Pengaturan Halaman
st.set_page_config(page_title="HookCraft AI - Viral Hook Generator", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (Versi Sempurna) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
    }
    
    /* Warna Label & Teks */
    label, .stMarkdown, p, span {
        color: white !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Input Box & Placeholder */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b !important;
        color: white !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 10px !important;
    }
    
    /* Bikin tulisan contoh (placeholder) jadi abu-abu terang agar terbaca */
    input::placeholder {
        color: #94a3b8 !important;
        opacity: 1;
    }
    
    /* Tombol Utama Mewah */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 18px !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 10px !important;
        box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3) !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 210, 255, 0.5) !important;
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
    st.markdown("<h1 style='text-align: center; color: #00d2ff;'>🔒 HookCraft AI</h1>", unsafe_allow_html=True)
    st.text_input("Masukkan Password Akses:", type="password", key="password_input", on_change=check_password)
    st.stop() 

# --- HALAMAN UTAMA ---
st.markdown("<h1 style='text-align: center; color: #00d2ff;'>🚀 HookCraft AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Mulai viral hari ini dengan racikan hook AI terbaik.</p>", unsafe_allow_html=True)
st.markdown("---")

topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Cara cuan dari HP")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif", "Misterius (Kepo)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Mau berapa pilihan hook?", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password", placeholder="sk-xxxx...")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Silakan masukkan API Key Anda dulu!")
    elif not topik:
        st.warning("Isi dulu topik videonya ya.")
    else:
        with st.spinner("Meracik ide..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter viral. Berikan hook pendek dan tajam."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.info("🔥 Ini dia racikan hook untukmu:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Sepertinya ada masalah: {e}")
