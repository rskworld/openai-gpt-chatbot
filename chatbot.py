"""
OpenAI GPT Chatbot
Complete chatbot project using OpenAI GPT API for intelligent conversations and text generation.

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026

This chatbot project integrates with OpenAI GPT API to create intelligent conversational interfaces.
Features include message handling, context management, and response generation.
Perfect for building chatbots with advanced language understanding and natural conversation capabilities.
"""

import os
import json
import time
from typing import List, Dict, Optional, Generator, Callable
from openai import OpenAI
from datetime import datetime


class GPTChatbot:
    """
    OpenAI GPT Chatbot Class
    
    Handles conversation management, context handling, and response generation
    using OpenAI's GPT-3 and GPT-4 models.
    
    Author: RSK World (https://rskworld.in)
    Year: 2026
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize the GPT Chatbot
        
        Args:
            api_key: OpenAI API key (if not provided, will use OPENAI_API_KEY env variable)
            model: Model to use (gpt-3.5-turbo, gpt-4, etc.)
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        self.system_prompt = "You are a helpful and friendly AI assistant."
        
        # Advanced features - Author: RSK World (https://rskworld.in) - Year: 2026
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        self.conversation_stats = {
            "total_messages": 0,
            "total_requests": 0,
            "total_cost": 0.0,
            "start_time": datetime.now().isoformat()
        }
        self.max_retries = 3
        self.retry_delay = 1
    
    def set_system_prompt(self, prompt: str):
        """
        Set the system prompt for the chatbot
        
        Args:
            prompt: System prompt to set
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.system_prompt = prompt
    
    def add_message(self, role: str, content: str):
        """
        Add a message to conversation history
        
        Args:
            role: Message role (user, assistant, system)
            content: Message content
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.conversation_history.append({"role": role, "content": content})
    
    def clear_history(self):
        """Clear conversation history"""
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.conversation_history = []
    
    def get_response(self, user_message: str, temperature: float = 0.7, max_tokens: int = 500, 
                     stream: bool = False, functions: Optional[List] = None) -> str:
        """
        Get response from GPT model with advanced features
        
        Args:
            user_message: User's message
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens in response
            stream: Whether to stream the response
            functions: Optional list of function definitions for function calling
            
        Returns:
            Assistant's response
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        # Add user message to history
        self.add_message("user", user_message)
        
        # Prepare messages for API call
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)
        
        # Prepare API parameters
        api_params = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        if functions:
            api_params["functions"] = functions
            api_params["function_call"] = "auto"
        
        # Retry logic with exponential backoff
        # Author: RSK World (https://rskworld.in) - Year: 2026
        for attempt in range(self.max_retries):
            try:
                if stream:
                    return self._get_streaming_response(api_params)
                
                # Call OpenAI API
                response = self.client.chat.completions.create(**api_params)
                
                # Extract assistant response
                assistant_message = response.choices[0].message.content
                
                # Track token usage
                if response.usage:
                    self.token_usage["prompt_tokens"] += response.usage.prompt_tokens
                    self.token_usage["completion_tokens"] += response.usage.completion_tokens
                    self.token_usage["total_tokens"] += response.usage.total_tokens
                
                # Update statistics
                self.conversation_stats["total_requests"] += 1
                self.conversation_stats["total_messages"] += 2  # user + assistant
                
                # Add assistant response to history
                self.add_message("assistant", assistant_message)
                
                return assistant_message
                
            except Exception as e:
                if attempt < self.max_retries - 1:
                    wait_time = self.retry_delay * (2 ** attempt)
                    print(f"Retry attempt {attempt + 1}/{self.max_retries} after {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    error_msg = f"Error getting response after {self.max_retries} attempts: {str(e)}"
                    print(error_msg)
                    return error_msg
    
    def _get_streaming_response(self, api_params: dict) -> str:
        """
        Get streaming response from GPT model
        
        Args:
            api_params: API parameters dictionary
            
        Returns:
            Complete assistant response
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        api_params["stream"] = True
        full_response = ""
        
        stream = self.client.chat.completions.create(**api_params)
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content
                print(content, end='', flush=True)
        
        print()  # New line after streaming
        self.add_message("assistant", full_response)
        return full_response
    
    def get_streaming_response(self, user_message: str, temperature: float = 0.7, 
                               max_tokens: int = 500, callback: Optional[Callable] = None) -> Generator[str, None, None]:
        """
        Get streaming response generator
        
        Args:
            user_message: User's message
            temperature: Sampling temperature
            max_tokens: Maximum tokens
            callback: Optional callback function for each chunk
            
        Yields:
            Response chunks
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.add_message("user", user_message)
        
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)
        
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )
            
            full_response = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    if callback:
                        callback(content)
                    yield content
            
            self.add_message("assistant", full_response)
            self.conversation_stats["total_requests"] += 1
            
        except Exception as e:
            error_msg = f"Error in streaming: {str(e)}"
            if callback:
                callback(error_msg)
            yield error_msg
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """
        Get full conversation history
        
        Returns:
            List of conversation messages
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        return self.conversation_history
    
    def save_conversation(self, filename: str):
        """
        Save conversation to JSON file
        
        Args:
            filename: Output filename
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
    
    def load_conversation(self, filename: str):
        """
        Load conversation from JSON file
        
        Args:
            filename: Input filename
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        with open(filename, 'r', encoding='utf-8') as f:
            self.conversation_history = json.load(f)
    
    def get_token_usage(self) -> Dict:
        """
        Get token usage statistics
        
        Returns:
            Dictionary with token usage stats
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        return self.token_usage.copy()
    
    def get_conversation_stats(self) -> Dict:
        """
        Get conversation statistics
        
        Returns:
            Dictionary with conversation stats
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        stats = self.conversation_stats.copy()
        stats["token_usage"] = self.token_usage.copy()
        stats["current_time"] = datetime.now().isoformat()
        return stats
    
    def reset_stats(self):
        """Reset token usage and conversation statistics"""
        # Author: RSK World (https://rskworld.in) - Year: 2026
        self.token_usage = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
        self.conversation_stats = {
            "total_messages": 0,
            "total_requests": 0,
            "total_cost": 0.0,
            "start_time": datetime.now().isoformat()
        }
    
    def export_conversation_txt(self, filename_or_file):
        """
        Export conversation to plain text file
        
        Args:
            filename_or_file: Output filename (str) or file-like object (BytesIO)
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        if isinstance(filename_or_file, str):
            f = open(filename_or_file, 'w', encoding='utf-8')
            close_file = True
        else:
            # For BytesIO, we need to write as bytes
            content = self._generate_txt_content()
            filename_or_file.write(content.encode('utf-8'))
            return
        
        try:
            f.write(self._generate_txt_content())
        finally:
            if close_file:
                f.close()
    
    def _generate_txt_content(self) -> str:
        """
        Generate text content for export
        
        Returns:
            String content
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        content = "=" * 60 + "\n"
        content += "OpenAI GPT Chatbot Conversation\n"
        content += f"Created by RSK World (https://rskworld.in)\n"
        content += f"Export Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        content += "=" * 60 + "\n\n"
        
        for msg in self.conversation_history:
            role = msg['role'].upper()
            msg_content = msg['content']
            content += f"[{role}]\n{msg_content}\n\n"
        
        content += "\n" + "=" * 60 + "\n"
        content += "Token Usage Statistics\n"
        content += "=" * 60 + "\n"
        content += f"Prompt Tokens: {self.token_usage['prompt_tokens']}\n"
        content += f"Completion Tokens: {self.token_usage['completion_tokens']}\n"
        content += f"Total Tokens: {self.token_usage['total_tokens']}\n"
        
        return content
    
    def search_conversation(self, query: str) -> List[Dict]:
        """
        Search conversation history for messages containing query
        
        Args:
            query: Search query string
            
        Returns:
            List of matching messages
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        query_lower = query.lower()
        results = []
        
        for msg in self.conversation_history:
            if query_lower in msg['content'].lower():
                results.append(msg)
        
        return results
    
    def get_conversation_summary(self) -> str:
        """
        Get a summary of the conversation
        
        Returns:
            Conversation summary string
        """
        # Author: RSK World (https://rskworld.in) - Year: 2026
        user_messages = [msg for msg in self.conversation_history if msg['role'] == 'user']
        assistant_messages = [msg for msg in self.conversation_history if msg['role'] == 'assistant']
        
        summary = f"Conversation Summary:\n"
        summary += f"- Total Messages: {len(self.conversation_history)}\n"
        summary += f"- User Messages: {len(user_messages)}\n"
        summary += f"- Assistant Messages: {len(assistant_messages)}\n"
        summary += f"- Total Tokens Used: {self.token_usage['total_tokens']}\n"
        summary += f"- Total Requests: {self.conversation_stats['total_requests']}\n"
        
        if user_messages:
            summary += f"\nFirst User Message: {user_messages[0]['content'][:100]}...\n"
        
        return summary


def main():
    """
    Main function to demonstrate chatbot usage
    
    Author: RSK World (https://rskworld.in) - Year: 2026
    """
    print("=" * 60)
    print("OpenAI GPT Chatbot - RSK World (https://rskworld.in)")
    print("=" * 60)
    print()
    
    # Initialize chatbot
    # Note: Set your OpenAI API key in environment variable OPENAI_API_KEY
    # or create a .env file with OPENAI_API_KEY=your_key_here
    try:
        chatbot = GPTChatbot(model="gpt-3.5-turbo")
        chatbot.set_system_prompt("You are a helpful and friendly AI assistant created by RSK World.")
        
        print("Chatbot initialized! Type 'quit' or 'exit' to end the conversation.")
        print("Type 'clear' to clear conversation history.")
        print("Type 'history' to view conversation history.")
        print("-" * 60)
        print()
        
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nGoodbye! Visit https://rskworld.in for more projects.")
                break
            
            if user_input.lower() == 'clear':
                chatbot.clear_history()
                print("Conversation history cleared.\n")
                continue
            
            if user_input.lower() == 'history':
                history = chatbot.get_conversation_history()
                print("\nConversation History:")
                for msg in history:
                    print(f"{msg['role'].upper()}: {msg['content']}")
                print()
                continue
            
            # Get response from chatbot
            response = chatbot.get_response(user_input)
            print(f"Assistant: {response}\n")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("\nPlease set your OpenAI API key:")
        print("1. Set environment variable: export OPENAI_API_KEY='your-key-here'")
        print("2. Or create a .env file with: OPENAI_API_KEY=your-key-here")
        print("\nFor more information, visit: https://rskworld.in")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("For support, contact: help@rskworld.in")


if __name__ == "__main__":
    main()

