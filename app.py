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

st.page_link(
    "pages/1_Hook_Generator.py",
    label="🎯 Hook Generator"
)

st.page_link(
    "pages/2_Script_Generator.py",
    label="📝 Script Generator"
)

st.page_link(
    "pages/3_Caption_Generator.py",
    label="📱 Caption Generator"
)

st.page_link(
    "pages/4_History.py",
    label="📚 History"
)
