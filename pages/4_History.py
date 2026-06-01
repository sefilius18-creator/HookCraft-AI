import streamlit as st
import pandas as pd

from database.db import get_history

st.title("📚 History")

data = get_history()

df = pd.DataFrame(
    data,
    columns=[
        "ID",
        "Feature",
        "Prompt",
        "Result"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)
