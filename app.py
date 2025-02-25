from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Streamlit Page Config
st.set_page_config(page_title="Chat with Yash AI 🤖", layout="wide")

# Create Columns (Chat Input | Chat History)
col1, col2 = st.columns([2, 1])  # Left side (Chat) is wider than Right side (History)

with col1:
    st.header("Chat with Yash AI 🤖")

    # Multi-line text input (3 lines visible)
    user_input = st.text_area("Ask me anything:", height=100, key="input")  
    submit = st.button("ASK YASH AI")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if submit and user_input:
        response = get_gemini_response(user_input)
        st.session_state['chat_history'].append(("You", user_input))
        
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Yash AI 🤖", chunk.text))

with col2:
    st.subheader("Chat History📜")
    for role, text in st.session_state['chat_history']:
        st.write(f"**{role}:** {text}")


