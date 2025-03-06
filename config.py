from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

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
        raise ValueError("GOOGLE_API_KEY not found in environment variables. Please set it in a .env file.")
    return api_key