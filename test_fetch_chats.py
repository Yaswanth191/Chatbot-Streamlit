from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
chat_collection = db["chat_history"]

# Fetch and print the latest 5 chats
print("🔍 Fetching Last 5 Chats:")
for chat in chat_collection.find().sort("_id", -1).limit(5):
    print(f"User: {chat['user_message']} | Bot: {chat['bot_response']}")
