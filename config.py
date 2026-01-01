"""
Configuration file for OpenAI GPT Chatbot

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
"""

import os
from dotenv import load_dotenv

# Author: RSK World (https://rskworld.in) - Year: 2026
# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class for OpenAI GPT Chatbot
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    
    # OpenAI API Configuration
    # Author: RSK World (https://rskworld.in) - Year: 2026
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    
    # Model Configuration
    # Author: RSK World (https://rskworld.in) - Year: 2026
    DEFAULT_MODEL = "gpt-3.5-turbo"  # Options: gpt-3.5-turbo, gpt-4, gpt-4-turbo-preview
    GPT4_MODEL = "gpt-4"
    GPT3_MODEL = "gpt-3.5-turbo"
    
    # Response Configuration
    # Author: RSK World (https://rskworld.in) - Year: 2026
    DEFAULT_TEMPERATURE = 0.7  # Controls randomness (0.0 to 2.0)
    DEFAULT_MAX_TOKENS = 500   # Maximum tokens in response
    MAX_TOKENS_LIMIT = 4096  # Maximum tokens for most models
    
    # System Prompt
    # Author: RSK World (https://rskworld.in) - Year: 2026
    DEFAULT_SYSTEM_PROMPT = "You are a helpful and friendly AI assistant created by RSK World (https://rskworld.in)."
    
    # Conversation Settings
    # Author: RSK World (https://rskworld.in) - Year: 2026
    MAX_CONVERSATION_HISTORY = 50  # Maximum messages to keep in history
    SAVE_CONVERSATIONS = True  # Whether to save conversations
    CONVERSATION_DIR = "conversations"  # Directory to save conversations
    
    # Application Settings
    # Author: RSK World (https://rskworld.in) - Year: 2026
    APP_NAME = "OpenAI GPT Chatbot"
    APP_VERSION = "1.0.0"
    APP_AUTHOR = "RSK World"
    APP_WEBSITE = "https://rskworld.in"
    APP_EMAIL = "help@rskworld.in"
    APP_PHONE = "+91 93305 39277"
    APP_YEAR = "2026"
    
    @classmethod
    def validate(cls) -> bool:
        """
        Validate configuration
        
        Returns:
            True if configuration is valid, False otherwise
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        if not cls.OPENAI_API_KEY:
            return False
        return True
    
    @classmethod
    def get_info(cls) -> dict:
        """
        Get application information
        
        Returns:
            Dictionary with application information
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        return {
            "name": cls.APP_NAME,
            "version": cls.APP_VERSION,
            "author": cls.APP_AUTHOR,
            "website": cls.APP_WEBSITE,
            "email": cls.APP_EMAIL,
            "phone": cls.APP_PHONE,
            "year": cls.APP_YEAR
        }

