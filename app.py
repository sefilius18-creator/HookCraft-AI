import streamlit as st

st.set_page_config(
    page_title="HookCraft AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 HookCraft AI")

st.markdown("""
### AI Content Creation Toolkit

Buat Hook, Script, dan Caption viral
menggunakan Gemini AI.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Hook Generator",
        "Ready"
    )

with col2:
    st.metric(
        "Script Generator",
        "Ready"
    )

with col3:
    st.metric(
        "Caption Generator",
        "Ready"
    )

st.info(
    "Pilih menu di sidebar untuk mulai menggunakan tools."
)
