from dotenv import load_dotenv, find_dotenv
import os

# Load .env file if it exists
if find_dotenv():
    load_dotenv()
else:
    print("⚠️ Warning: No .env file found. Make sure your API key is set.")

REQUIRED_ENV_VARS = ["GOOGLE_API_KEY", "MONGO_URI"]

def check_env_vars():
    """Ensures all required environment variables are set."""
    missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"⚠️ Missing environment variables: {', '.join(missing_vars)}. Please set them in your .env file.")

def get_api_key():
    """
    Retrieves the Google API key from environment variables.
    
    Returns:
        The API key as a string.
    
    Raises:
        ValueError: If the API key is not found in environment variables.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("⚠️ GOOGLE_API_KEY not found in environment variables. Please set it in a .env file.")
    return api_key
