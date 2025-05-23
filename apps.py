import streamlit as st
from wish import wish_internship

st.title("Internship Wish Generator")

user_name = st.text_input("Enter your name:")
if user_name:
    wish = wish_internship(user_name)
    st.write(wish)
