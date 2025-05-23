# app.py
import streamlit as st

st.title("Simple Streamlit App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! 👋")
else:
    st.write("Please enter your name above ☝️")
st.write("This is a simple Streamlit app that greets the user by name.")
st.write("You can run this app using the command: `streamlit run app.py`")