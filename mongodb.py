import os
import time
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["chatbot_db"]
chat_collection = db["chat_history"]
user_collection = db["users"]

def save_chat(user_message, bot_response):
    """ Save chat history to MongoDB """
    chat_data = {"user_message": user_message, "bot_response": bot_response}
    chat_collection.insert_one(chat_data)

def fetch_chat_history(limit=10):
    """ Retrieve chat history from MongoDB """
    chats = chat_collection.find().sort("_id", -1).limit(limit)
    return list(chats)

def save_user_name(user_id, user_name):
    """ Save user name with a unique user ID """
    user_collection.update_one(
        {"user_id": user_id},  # Match the user_id
        {"$set": {"user_name": user_name, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}},
        upsert=True  # Insert if not exists, update if exists
    )

def fetch_last_user_name(user_id):
    """ Retrieve last stored user name for a specific user """
    user = user_collection.find_one({"user_id": user_id})
    return user["user_name"] if user else None
