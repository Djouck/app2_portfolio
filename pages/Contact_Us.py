import streamlit as st

st.header("Contact Me")

with st.form(key="my_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        print(button)
        print("I was pressed!")