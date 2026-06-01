import streamlit as st

st.set_page_config(
    page_title="HookCraft AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 HookCraft AI")

menu = st.selectbox(
    "Pilih Tool",
    [
        "🎯 Hook Generator",
        "📝 Script Generator",
        "📱 Caption Generator",
        "📚 History"
    ]
)

# HOOK GENERATOR
if menu == "🎯 Hook Generator":

    st.header("🎯 Hook Generator")

    topic = st.text_input(
        "Topik Konten"
    )

    hook_type = st.selectbox(
        "Tipe Hook",
        [
            "FOMO",
            "Curiosity",
            "Storytelling",
            "Problem"
        ]
    )

    if st.button("Generate Hook"):

        st.success(
            f"Topik: {topic}"
        )

        st.write(
            f"Tipe: {hook_type}"
        )

# SCRIPT GENERATOR
elif menu == "📝 Script Generator":

    st.header("📝 Script Generator")

    hook = st.text_area(
        "Masukkan Hook"
    )

    if st.button(
        "Generate Script"
    ):
        st.write(
            "Script akan muncul di sini"
        )

# CAPTION GENERATOR
elif menu == "📱 Caption Generator":

    st.header("📱 Caption Generator")

    topic = st.text_input(
        "Topik Caption"
    )

    if st.button(
        "Generate Caption"
    ):
        st.write(
            "Caption akan muncul di sini"
        )

# HISTORY
elif menu == "📚 History":

    st.header("📚 History")

    st.write(
        "Riwayat akan muncul di sini"
    )
