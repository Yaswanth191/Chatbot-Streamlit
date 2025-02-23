from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize chat session in session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = genai.GenerativeModel("gemini-pro").start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    chat = st.session_state.chat_session  # Retrieve chat session
    response = chat.send_message(question, stream=True)  # Send message with history
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Get user input
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    response = get_gemini_response(input_text)

    # Display response and update chat history
    st.subheader("The Response is")
    full_response = ""
    for chunk in response:
        st.write(chunk.text)
        full_response += chunk.text

    # Store user input and AI response in session history
    st.session_state.chat_session.history.append({"role": "user", "parts": [input_text]})  
    st.session_state.chat_session.history.append({"role": "model", "parts": [full_response]})  

# Display full chat history
st.subheader("The Chat History is")
for message in st.session_state.chat_session.history:
    role = "You" if message["role"] == "user" else "Bot"
    st.write(f"{role}: {message['parts'][0]}")  
