import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (DESAIN LOGIN MEWAH & FIX TEKS TRANSPARAN) ---
st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background: radial-gradient(circle, #1e293b 0%, #0f172a 100%);
    }

    /* Judul Utama */
    .main-title {
        font-size: 3.2rem !important;
        font-weight: 800 !important;
        color: #00d2ff !important;
        text-align: center;
        text-shadow: 0 0 20px rgba(0, 210, 255, 0.4);
        margin-bottom: 0px;
    }

    /* Halaman Login Box */
    .login-container {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    /* Memaksa Label & Teks Putih Terang */
    label p, .stMarkdown p, span, .subtitle {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    /* FIX: Memaksa Teks di dalam Kotak Input & Placeholder Terlihat */
    input {
        color: white !important;
    }
    ::placeholder {
        color: #cbd5e1 !important; /* Abu-abu sangat terang agar terbaca */
        opacity: 1 !important;
    }

    /* Input Box Styling */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #0f172a !important;
        color: white !important;
        border: 2px solid #38bdf8 !important;
        border-radius: 15px !important;
        height: 50px;
    }

    /* Tombol Utama */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5) !important;
        color: white !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        border-radius: 15px !important;
        border: none !important;
        padding: 15px !important;
        width: 100% !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SISTEM LOGIN ---
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password Salah!")

# TAMPILAN LOGIN (DIBUAT LEBIH BERKELAS)
if not st.session_state["authenticated"]:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">🚀 HookCraft AI</h1>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='color: #38bdf8;'>Exclusive Access</h2>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.9rem;'>Please enter your private key to unlock viral growth tools.</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.text_input("PASSWORD AKSES:", type="password", key="password_input", 
                     placeholder="Ketik password di sini...", on_change=check_password)
        
        st.markdown("<br><small style='color: #64748b;'>Protected by HookCraft Encryption</small>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- TAMPILAN APLIKASI (SETELAH LOGIN) ---
st.markdown('<h1 class="main-title">🚀 HookCraft AI</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8 !important;'>Dominate the algorithm, one hook at a time.</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout Input Section
topik = st.text_input("💡 Apa topik videomu?", placeholder="Contoh: Cara diet tanpa lapar")
gaya_bahasa = st.selectbox("🗣️ Pilih Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Pilihan Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 OpenAI API Key:", type="password", placeholder="Tempel API Key sk-xxxx Anda di sini")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("✨ GENERATE VIRAL HOOKS ✨"):
    if not api_key_input:
        st.error("Masukkan API Key OpenAI Anda!")
    elif not topik:
        st.warning("Tuliskan topik videonya dulu!")
    else:
        with st.spinner("Menganalisis pola viral..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Kamu adalah copywriter TikTok viral. Buat hook yang sangat menarik, berani, dan pendek dalam Bahasa Indonesia."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Hook Viral Siap Digunakan:")
                # Kotak hasil dengan background kontras
                st.markdown(f"""
                <div style="background: #1e293b; padding: 20px; border-left: 5px solid #00d2ff; border-radius: 10px;">
                    {response.choices[0].message.content}
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
