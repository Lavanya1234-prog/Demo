import streamlit as st
import numpy as np
import time
import streamlit as st

st.header("This is my first streamlit App LETS ENJOY :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))


with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")
