import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["chatbot_db"]

    # Check if we can list databases
    databases = client.list_database_names()
    print("✅ MongoDB Connection Successful!")
    print("Databases:", databases)
    
    # Check if chatbot_db exists
    if "chatbot_db" in databases:
        print("✅ `chatbot_db` found!")
    else:
        print("❌ `chatbot_db` NOT found! Did you save any chats yet?")

except Exception as e:
    print("❌ MongoDB Connection Failed:", str(e))
