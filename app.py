import streamlit as st

st.set_page_config(
    page_title="HookCraft AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 HookCraft AI")

st.markdown("""
### Selamat Datang

Generate Hook, Script dan Caption Viral
menggunakan Gemini AI.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🎯 Hook Generator")

with col2:
    st.info("📝 Script Generator")

with col3:
    st.info("📱 Caption Generator")
