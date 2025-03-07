# Yash AI Chatbot - README
## Project Overview
Yash AI is an AI-powered chatbot built with Google Gemini API and Streamlit, designed for real-time
conversational interactions. It features chat history management, streaming responses, and a clean,
interactive UI.
## Features
- Conversational AI: Powered by Google Gemini (gemini-pro).
- Interactive UI: Built using Streamlit for ease of use.
- Session-Based Chat History: Maintains context within a session.
- Streaming Responses: Ensures smooth, real-time chatbot interactions.
- Secure API Key Handling: Uses a .env file for API security.
## Installation & Setup
1. Clone the Repository:
```
git clone <repository_url>
cd AI_CHATBOT
```
2. Install Dependencies:
```
pip install -r requirements.txt
```
3. Set Up Environment Variables:
Create a .env file and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```
4. Run the Chatbot:
```
streamlit run app.py
```
## How It Works
1. User Input: The chatbot takes user queries via the Streamlit UI.
2. Processing with Gemini API: Sends the input to gemini-pro and retrieves a response.
3. Streaming Responses: Ensures dynamic, real-time responses.
4. Chat History Management: Uses st.session_state to track conversations within a session.
5. Displaying Messages: Shows user and AI messages in a structured chat format.
## File Structure
AI_CHATBOT/
- app.py : Main chatbot logic with Gemini API integration
- chat.py : Chatbot processing logic (if modularized)
- qachat.py : Optional Q&A-specific logic
- vision.py : Optional module for image-based queries
- requirements.txt: Dependencies
- .env : Stores API keys securely
- .gitignore : Ignores sensitive files
- LICENSE : License details
## Future Enhancements
- Persistent Memory: Store chat history in a database (SQLite, Firebase, Redis).
- Knowledge Base (RAG): Enhance chatbot accuracy using FAISS/Pinecone.
- Multimodal Support: Extend chatbot to handle images via Gemini Vision models.
- Cloud Deployment: Deploy on AWS, GCP, or Render using Docker for scalability.
- Fine-Tuning: Experiment with domain-specific datasets for better performance.
## License
This project is licensed under the MIT License.
---
Want to enhance Yash AI? Let's collaborate!# Chatbot-Streamlit
