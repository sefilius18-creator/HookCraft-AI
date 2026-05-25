import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(page_title="HookCraft AI", page_icon="🚀", layout="centered")

# --- CSS SEDERHANA & STABIL ---
st.markdown("""
    <style>
    /* Background Dasar */
    .stApp { background-color: #0b0f1a !important; }
    
    /* Judul Utama */
    .hero-wrapper {
        display: flex; flex-direction: column; align-items: center;
        margin-top: 20px; color: white;
    }
    .main-title { font-size: 3.5rem; font-weight: 800; margin: 0; }
    .sub-title { font-size: 3rem; font-weight: 800; margin-top: -10px; }
    
    /* Box Fitur */
    .feature-box {
        background: rgba(255,255,255,0.05); border: 1px solid #38bdf8;
        border-radius: 15px; padding: 20px; margin: 20px 0; color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIC ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login_action():
    if st.session_state.pwd == "Sefilius18":
        st.session_state["authenticated"] = True
    else:
        st.error("Password Salah!")

# --- TAMPILAN ---
if not st.session_state["authenticated"]:
    st.markdown("""
        <div class="hero-wrapper">
            <div style="font-size: 60px;">🚀 HookCraft</div>
            <div class="sub-title">AI</div>
        </div>
        <div class="feature-box">
            <p style='color:#38bdf8; font-weight:bold; text-align:center;'>CORE SYSTEM ACTIVE</p>
            <p>🔹 Neural Hook Engine</p>
            <p>🔹 Deep Analysis</p>
            <p>🔹 Psychology Hooks</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.text_input("PASSWORD:", type="password", key="pwd")
    st.button("MASUK", on_click=login_action)
    st.stop()

st.success("Akses Diterima.")
