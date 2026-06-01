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

if st.button("🎯 Hook Generator", use_container_width=True):
    st.switch_page("pages/1_🎯_Hook_Generator.py")

if st.button("📝 Script Generator", use_container_width=True):
    st.switch_page("pages/2_📝_Script_Generator.py")

if st.button("📱 Caption Generator", use_container_width=True):
    st.switch_page("pages/3_📱_Caption_Generator.py")

if st.button("📚 History", use_container_width=True):
    st.switch_page("pages/4_📚_History.py")
