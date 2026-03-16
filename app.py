import streamlit as st

st.set_page_config(page_title="Minimal App", page_icon="✨", layout="centered")

st.title("Minimal Streamlit App")
st.write("Your Dockerized Streamlit app is running.")

name = st.text_input("What's your name?")

if name:
    st.success(f"Hello, {name}!")