import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Giulia Ruffini")
    content = """
    Hi! I am Giulia! I am a Mathematician and I am a PhD student in Computer Science. My research cover process mining
    topic. And I am learning Python. \n With the Portfolio web app I would like to keep trace of my progress in using 
    Python.\n See you on these screens!
    """
    st.info(content)
