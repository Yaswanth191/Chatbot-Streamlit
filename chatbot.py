import google.generativeai as genai
from config import get_api_key
import logging

# Set up logging to help debug issues
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def configure_genai():
    """
    Configures the Gemini API with the API key from config and initializes a chat session.
    
    Returns:
        A chat session object for interacting with the Gemini model.
    
    Raises:
        ValueError: If the API key is not found or invalid.
        Exception: For other configuration errors.
    """
    try:
        # Load and configure the API key
        api_key = get_api_key()
        if not api_key:
            logger.error("GOOGLE_API_KEY not found in environment variables.")
            raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")
        
        genai.configure(api_key=api_key)
        logger.info("Gemini API configured successfully.")

        # Initialize the Gemini model (gemini-1.5-pro)
        model = genai.GenerativeModel("gemini-1.5-pro")
        chat = model.start_chat(history=[])
        logger.info("Chat session initialized with gemini-1.5-pro model.")
        
        return chat
    
    except Exception as e:
        logger.error(f"Failed to configure Gemini API: {str(e)}")
        raise

def get_gemini_response(chat, question):
    """
    Sends the user's question to the Gemini model and returns the response.
    
    Args:
        chat: The chat session object from configure_genai().
        question: The user's input string.
    
    Returns:
        An iterable of response chunks (if streaming) or a string (if an error occurs).
    
    Raises:
        Exception: If the API call fails (e.g., network issues, safety filters).
    """
    try:
        logger.info(f"Sending question to Gemini model: {question}")
        response = chat.send_message(question, stream=True)
        logger.info("Response received successfully.")
        return response
    except Exception as e:
        logger.error(f"Error getting response from Gemini model: {str(e)}")
        return f"Error: {str(e)}"