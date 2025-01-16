import streamlit as st
import numpy as np
import time
import streamlit as st

st.header("This is my first streamlit App LETS ENJOY :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


def text_conversation():
    st.header("Text Conversation")
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )
    
    user_input = st.text_input("Enter your message:")
    if st.button("Send"):
        response = chat.send_message(user_input)
        st.write("Model:", response.text)




