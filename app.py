import streamlit as st
from pathlib import  Path

st.set_page_config(
    page_title="student task dashboard",
    layout="wide"
)
html_file = Path("index.html").read_text(encoding="utf-8")

st.components.v1.html(html_file,height=900,scrolling=True)