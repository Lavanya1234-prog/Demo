import streamlit as st

st.header("This is my first streamlit App :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")