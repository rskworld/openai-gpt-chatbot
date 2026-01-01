"""
Example Usage of OpenAI GPT Chatbot

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026

This file demonstrates various ways to use the OpenAI GPT Chatbot.
"""

from chatbot import GPTChatbot
from config import Config
import os

# Author: RSK World (https://rskworld.in) - Year: 2026
def example_basic_usage():
    """
    Basic usage example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)
    
    # Initialize chatbot
    # Author: RSK World (https://rskworld.in) - Year: 2026
    chatbot = GPTChatbot(model=Config.GPT3_MODEL)
    
    # Simple conversation
    response = chatbot.get_response("Hello! What can you do?")
    print(f"Assistant: {response}\n")


def example_gpt4_usage():
    """
    GPT-4 usage example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 2: Using GPT-4")
    print("=" * 60)
    
    # Initialize with GPT-4
    # Author: RSK World (https://rskworld.in) - Year: 2026
    chatbot = GPTChatbot(model=Config.GPT4_MODEL)
    chatbot.set_system_prompt("You are an expert Python programmer.")
    
    response = chatbot.get_response(
        "Explain list comprehensions in Python",
        temperature=0.7,
        max_tokens=300
    )
    print(f"Assistant: {response}\n")


def example_conversation_context():
    """
    Conversation with context example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 3: Conversation with Context")
    print("=" * 60)
    
    # Author: RSK World (https://rskworld.in) - Year: 2026
    chatbot = GPTChatbot(model=Config.DEFAULT_MODEL)
    
    # Multi-turn conversation
    messages = [
        "My name is John and I love programming.",
        "What programming languages do you recommend?",
        "Can you give me a simple example in Python?"
    ]
    
    for msg in messages:
        print(f"You: {msg}")
        response = chatbot.get_response(msg)
        print(f"Assistant: {response}\n")
    
    # View conversation history
    print("Conversation History:")
    for msg in chatbot.get_conversation_history():
        print(f"  {msg['role']}: {msg['content'][:50]}...")


def example_custom_system_prompt():
    """
    Custom system prompt example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 4: Custom System Prompt")
    print("=" * 60)
    
    # Author: RSK World (https://rskworld.in) - Year: 2026
    chatbot = GPTChatbot(model=Config.DEFAULT_MODEL)
    chatbot.set_system_prompt(
        "You are a helpful coding assistant created by RSK World. "
        "Always provide clear, concise answers with code examples when relevant."
    )
    
    response = chatbot.get_response("How do I create a Python function?")
    print(f"Assistant: {response}\n")


def example_save_load_conversation():
    """
    Save and load conversation example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 5: Save and Load Conversation")
    print("=" * 60)
    
    # Author: RSK World (https://rskworld.in) - Year: 2026
    chatbot = GPTChatbot(model=Config.DEFAULT_MODEL)
    
    # Have a conversation
    chatbot.get_response("Hello!")
    chatbot.get_response("Tell me a fun fact about Python.")
    
    # Save conversation
    filename = "example_conversation.json"
    chatbot.save_conversation(filename)
    print(f"Conversation saved to {filename}")
    
    # Create new chatbot and load conversation
    new_chatbot = GPTChatbot(model=Config.DEFAULT_MODEL)
    new_chatbot.load_conversation(filename)
    
    print(f"Loaded conversation with {len(new_chatbot.get_conversation_history())} messages")
    
    # Continue conversation
    response = new_chatbot.get_response("Tell me another fact!")
    print(f"Assistant: {response}\n")


def example_different_temperatures():
    """
    Different temperature settings example
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("Example 6: Different Temperature Settings")
    print("=" * 60)
    
    # Author: RSK World (https://rskworld.in) - Year: 2026
    question = "Write a short creative story about AI."
    
    temperatures = [0.3, 0.7, 1.2]
    
    for temp in temperatures:
        chatbot = GPTChatbot(model=Config.DEFAULT_MODEL)
        chatbot.clear_history()
        
        response = chatbot.get_response(question, temperature=temp, max_tokens=200)
        print(f"\nTemperature {temp}:")
        print(f"{response[:150]}...\n")


def main():
    """
    Main function to run examples
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("\n" + "=" * 60)
    print("OpenAI GPT Chatbot - Usage Examples")
    print("Created by RSK World (https://rskworld.in)")
    print("Year: 2026")
    print("=" * 60 + "\n")
    
    # Check if API key is set
    # Author: RSK World (https://rskworld.in) - Year: 2026
    if not Config.validate():
        print("Error: OPENAI_API_KEY not set!")
        print("Please set your API key in .env file or as environment variable.")
        print("For more information, visit: https://rskworld.in")
        return
    
    try:
        # Run examples
        # Author: RSK World (https://rskworld.in) - Year: 2026
        example_basic_usage()
        example_gpt4_usage()
        example_conversation_context()
        example_custom_system_prompt()
        example_save_load_conversation()
        example_different_temperatures()
        
        print("\n" + "=" * 60)
        print("All examples completed!")
        print("Visit https://rskworld.in for more projects.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        print("For support, contact: help@rskworld.in")


if __name__ == "__main__":
    main()

