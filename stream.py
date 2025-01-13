import streamlit as st
import numpy as np

st.header("This is my first streamlit App LETS ENJOY :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
