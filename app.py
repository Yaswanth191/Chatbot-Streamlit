import streamlit as st
import re
import uuid  # Generates a unique user ID for each user session
from chatbot import configure_genai, get_gemini_response
from datetime import datetime
from templates.components import render_chat_header, render_response_box, render_history_box
import mongodb  # Using MongoDB instead of SQLite
from config import check_env_vars

# Ensure all required environment variables are set
check_env_vars()

# Initialize chat model
chat = configure_genai()

# Streamlit Page Config
st.set_page_config(page_title="Chat with Yash AI 🤖", layout="wide")

# Load and inject CSS
with open("static/styles.css", "r") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Load and inject JavaScript
js_code = """
<script src="static/script.js"></script>
"""
st.components.v1.html(js_code, height=0)

# Generate a unique session-based user ID
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())  # Unique user session ID

user_id = st.session_state["user_id"]

# Create Columns
col1, col2 = st.columns([2, 1])

with col1:
    render_chat_header()
    
    with st.form(key="chat_form"):
        user_input = st.text_area("Ask me anything:", height=100, key="input")
        submit = st.form_submit_button("ASK YASH AI")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if submit and user_input:
        with st.spinner("Yash AI is thinking..."):
            response = get_gemini_response(chat, user_input)
            full_response = response if isinstance(response, str) else "".join(
                chunk.text if hasattr(chunk, "text") else chunk for chunk in response
            )

        # Check if user is providing their name
        if "my name is" in user_input.lower():
            match = re.search(r"my name is (.+)", user_input, re.IGNORECASE)
            if match:
                user_name = match.group(1).strip()
                mongodb.save_user_name(user_id, user_name)  # Save name with user ID
                full_response = f"Nice to meet you, {user_name}!"
            else:
                full_response = "Could you repeat your name again?"

        # Check if user is asking their name
        elif "what is my name" in user_input.lower():
            stored_name = mongodb.fetch_last_user_name(user_id)  # Fetch name using user ID
            if stored_name:
                full_response = f"Your name is {stored_name}!"
            else:
                full_response = "I don't remember your name yet. Please tell me!"

        # Save chat to MongoDB
        mongodb.save_chat(user_input, full_response)

        # Update chat history in session
        st.session_state['chat_history'].append(("You", user_input, datetime.now().strftime("%H:%M:%S")))
        st.subheader("Response:")
        render_response_box(full_response)
        st.session_state['chat_history'].append(("Yash AI 🤖", full_response, datetime.now().strftime("%H:%M:%S")))
    else:
        st.write("Debug: No submission yet or input is empty.")

with col2:
    if 'history_visible' not in st.session_state:
        st.session_state['history_visible'] = True

    button_label = "Hide History 📜" if st.session_state['history_visible'] else "Show History 📜"
    if st.button(button_label, key="toggle_history"):
        st.session_state['history_visible'] = not st.session_state['history_visible']

    if st.session_state['history_visible']:
        render_history_box(st.session_state['chat_history'])
