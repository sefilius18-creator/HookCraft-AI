import streamlit as st

st.set_page_config(
    page_title="HookCraft AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 HookCraft AI")

st.markdown("""
## Selamat Datang

Generate Hook, Script dan Caption Viral
menggunakan Gemini AI.
""")

if st.button("🎯 Hook Generator"):
    st.switch_page("pages/1_Hook_Generator.py")

if st.button("📝 Script Generator"):
    st.switch_page("pages/2_Script_Generator.py")

if st.button("📱 Caption Generator"):
    st.switch_page("pages/3_Caption_Generator.py")

if st.button("📚 History"):
    st.switch_page("pages/4_History.py")
