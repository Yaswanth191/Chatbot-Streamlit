import streamlit as st
from chatbot import configure_genai, get_gemini_response
from datetime import datetime
from templates.components import render_chat_header, render_response_box, render_history_box

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
            full_response = "".join(chunk.text for chunk in response) if hasattr(response, "__iter__") else response
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
    button_class = "toggle-button-on" if st.session_state['history_visible'] else "toggle-button-off"
    if st.button(button_label, key="toggle_history"):
        st.session_state['history_visible'] = not st.session_state['history_visible']

    if st.session_state['history_visible']:
        render_history_box(st.session_state['chat_history'])