import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
from pathlib import Path
# from IPython.display import Markdown
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.header("This is my first streamlit App LETS ENJOY :blue[cool] :sunglasses:")

import streamlit as st

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

def main():

    # Sidebar for use case selection
    use_case = st.sidebar.selectbox("Select Use Case", ["Text Conversation"]
                                                        
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

if __name__ == "__main__":
    main()


