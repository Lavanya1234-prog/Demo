import streamlit as st

st.header("This is my first streamlit App LETS ENJOY :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")



st.header("Settings")
st.write(f"You are logged in as {st.session_state.role}.")

st.header("Admin 1")
st.write(f"You are logged in as {st.session_state.role}.")

st.header("Admin 2")
st.write(f"You are logged in as {st.session_state.role}.")
