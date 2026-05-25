import streamlit as st
from openai import OpenAI

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS (PREMIUM TECH LOGIN) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f1a !important;
    }

    /* Judul & Robot Logo */
    .hero-container {
        text-align: center;
        padding-top: 20px;
    }
    
    .robot-logo {
        font-size: 80px;
        filter: drop-shadow(0 0 15px #38bdf8);
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: #38bdf8 !important;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
        margin: 0;
    }

    /* Kotak Transparan Berisi Fitur */
    .feature-box {
        background: rgba(56, 189, 248, 0.03);
        border: 1px solid rgba(56, 189, 248, 0.15);
        border-radius: 20px;
        padding: 25px;
        margin: 25px 0;
        text-align: left;
    }

    .feature-item {
        color: #94a3b8 !important;
        font-size: 0.9rem;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }

    .feature-item i {
        color: #38bdf8;
        margin-right: 10px;
    }

    /* Input & Button Styling */
    input {
        color: #ffffff !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #334155 !important;
    }
    
    label p {
        color: #38bdf8 !important;
        font-weight: bold !important;
        text-align: center;
        width: 100%;
    }

    .stButton>button {
        background: linear-gradient(90deg, #38bdf8, #2563eb) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
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

# --- HALAMAN LOGIN ---
if not st.session_state["authenticated"]:
    # Header dengan Logo Robot
    st.markdown("""
        <div class="hero-container">
            <div class="robot-logo">🤖</div>
            <p class="hero-title">HookCraft AI</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Isi Kotak Transparan agar tidak kosong
    st.markdown("""
        <div class="feature-box">
            <p style='color:white; font-weight:bold; font-size:1.1rem; margin-bottom:15px; text-align:center;'>🚀 AI Content Engine v1.0</p>
            <div class="feature-item">🔹 <b>Viral Hook Generator</b> - Create attention-grabbing openers.</div>
            <div class="feature-item">🔹 <b>Psychology-Based Tone</b> - From Mystery to Controversy.</div>
            <div class="feature-item">🔹 <b>Algorithm Optimized</b> - Built for TikTok, Reels, & Shorts.</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Area Input Password
    st.text_input("ENTER ACCESS KEY:", type="password", key="password_input", 
                 placeholder="Type your password here...", on_change=check_password)
    
    st.markdown("<p style='text-align:center; font-size:0.7rem; color:#475569; margin-top:30px;'>DECRYPTING ACCESS... SYSTEM READY.</p>", unsafe_allow_html=True)
    st.stop()

# --- HALAMAN UTAMA (SESUDAH LOGIN) ---
st.markdown("<div style='text-align:center;'><p class='hero-title'>🚀 HookCraft AI</p></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:#94a3b8 !important;'>Unleash your content's viral potential.</p>", unsafe_allow_html=True)

st.markdown("---")
topik = st.text_input("💡 Apa topik videomu?", placeholder="Misal: Bisnis dari rumah")
gaya_bahasa = st.selectbox("🗣️ Gaya Bahasa:", ["Anak Muda / Kasual", "Kontradiktif (Debat)", "Misterius (Curiosity)", "Edukasi Santai"])
jumlah_hook = st.select_slider("📊 Jumlah Hook:", options=[3, 4, 5, 6, 7], value=5)
api_key_input = st.text_input("🔑 API Key OpenAI:", type="password", placeholder="sk-xxxx...")

if st.button("GENERATE VIRAL HOOKS"):
    if not api_key_input or not topik:
        st.warning("Pastikan API Key dan Topik sudah diisi!")
    else:
        with st.spinner("Processing..."):
            try:
                client = OpenAI(api_key=api_key_input)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional social media copywriter."},
                        {"role": "user", "content": f"Buatkan {jumlah_hook} hook {gaya_bahasa} tentang {topik}."}
                    ]
                )
                st.success("🔥 Selesai!")
                st.markdown(f"""
                <div style="background-color: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #38bdf8; color: white;">
                {response.choices[0].message.content}
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
