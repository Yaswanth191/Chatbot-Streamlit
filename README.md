# 🚀 AI Chatbot - Streamlit & MongoDB

## 📌 Project Overview
This is an AI-powered **chatbot application** built using **Python, Streamlit, and MongoDB**, with **Google Gemini API** for intelligent responses. The chatbot provides a real-time conversational experience and is deployed on **AWS EC2 with Docker**.

🔗 **Live Demo**: [https://3.83.87.37:8501/](https://3.83.87.37:8501/)

## 📂 Project Structure
```
AI_Chatbot/
│── static/                   # Static files (CSS, JS)
│── templates/                # UI Components for Streamlit
│── config/                   # Configuration settings
│── core/                     # Main chatbot logic
│── database/                 # MongoDB & SQLite integration
│── tests/                    # Unit tests
│── scripts/                  # Utility scripts
│── deployment/               # Docker & AWS setup
│── docs/                     # Documentation files
│── app.py                    # Streamlit application
│── requirements.txt          # Dependencies
│── Dockerfile                # Containerization setup
│── .gitignore                # Ignore unnecessary files
```

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Yaswanth191/Chatbot-Streamlit.git
cd Chatbot-Streamlit
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**
```sh
streamlit run app.py
```
👉 The chatbot will be available at `http://localhost:8501/`

## 📦 Deployment on AWS EC2 with Docker
### **1️⃣ Build and Run Docker Container**
```sh
docker build -t ai-chatbot .
docker run -d -p 8501:8501 ai-chatbot
```
### **2️⃣ Access the Chatbot**
Go to: **http://your-ec2-ip:8501/**

## 🔍 Features
✔️ **Conversational AI** using Google Gemini API  
✔️ **Interactive Streamlit UI**  
✔️ **MongoDB Integration** for chat history  
✔️ **Show/Hide Chat History Feature**  
✔️ **Deployed on AWS EC2 with Docker**  

## 📝 License
This project is licensed under the **MIT License**.

## 
**Yaswanth Panchakarla**  
📧 yaswanthpanchakarla1@gmail.com  
🔗 GitHub: [Chatbot-Streamlit](https://github.com/Yaswanth191/Chatbot-Streamlit)

🚀 **Contributions are welcome!** Feel free to fork, create issues, and submit PRs.

