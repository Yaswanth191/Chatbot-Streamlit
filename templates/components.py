import streamlit as st

def render_chat_header():
    st.markdown('<h2 class="chat-header">Chat with Yash AI 🤖</h2>', unsafe_allow_html=True)

def render_response_box(response_text):
    st.markdown(f'<div class="response-box">{response_text}</div>', unsafe_allow_html=True)

def render_history_box(chat_history):
    st.markdown('<div class="history-box">', unsafe_allow_html=True)
    if chat_history:
        for role, text, time in chat_history:
            st.markdown(f'<div class="history-item"><b>{role} ({time}):</b> {text}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="history-item">No history yet. Start chatting!</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)