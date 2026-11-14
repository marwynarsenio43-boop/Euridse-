from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Para ti, Euridse ❤️", page_icon="❤️", layout="centered")

st.markdown(
    """
    <style>
      header, footer, #MainMenu, [data-testid="stToolbar"], [data-testid="stDecoration"] {display:none !important;}
      .stApp {background:#12080d;}
      .block-container {padding:0 !important; max-width:100% !important;}
      iframe {height:100vh !important; border:0; display:block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "page.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
