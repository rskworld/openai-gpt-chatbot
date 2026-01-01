# OpenAI GPT Chatbot

Complete chatbot project using OpenAI GPT API for intelligent conversations and text generation.

**Author:** RSK World  
**Website:** https://rskworld.in  
**Email:** help@rskworld.in  
**Phone:** +91 93305 39277  
**Year:** 2026

> 📖 **For complete documentation, see [DOCUMENTATION.md](DOCUMENTATION.md)**

## Description

This chatbot project integrates with OpenAI GPT API to create intelligent conversational interfaces. Features include message handling, context management, and response generation. Perfect for building chatbots with advanced language understanding and natural conversation capabilities.

## Features

### Core Features
- ✅ OpenAI API integration
- ✅ GPT-3 and GPT-4 support
- ✅ Conversation management
- ✅ Context handling
- ✅ Easy to customize

### Advanced Features
- ✅ **Streaming Responses** - Real-time token streaming for faster responses
- ✅ **Token Usage Tracking** - Monitor token consumption and costs
- ✅ **Conversation Statistics** - Track messages, requests, and usage
- ✅ **Export Conversations** - Export as JSON or TXT format
- ✅ **Conversation Search** - Search through conversation history
- ✅ **Markdown Rendering** - Beautiful markdown and code syntax highlighting
- ✅ **Dark Mode** - Toggle between light and dark themes
- ✅ **Custom Personas** - 8 pre-built personas (Coding, Creative, Teacher, etc.)
- ✅ **Advanced Error Handling** - Retry logic with exponential backoff
- ✅ **Web Interface** - Beautiful and modern UI with Flask
- ✅ **Settings Panel** - Configure model, temperature, tokens, and personas

## Technologies

- OpenAI API
- Python
- GPT-3
- GPT-4
- ChatGPT
- Flask (for web interface)
- HTML/CSS/JavaScript

## Difficulty Level

**Beginner** - Perfect for developers new to AI chatbots and OpenAI API integration.

## Installation

### Prerequisites

- Python 3.7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup Steps

1. **Clone or download this project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   
   **Option 1: Using .env file (Recommended)**
   
   Copy the example file:
   ```bash
   # Windows
   copy env_example.txt .env
   
   # Linux/Mac
   cp env_example.txt .env
   ```
   
   Then edit `.env` and replace `your_openai_api_key_here` with your actual API key.
   
   **Option 2: Environment variable**
   ```bash
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="your_openai_api_key_here"
   
   # Linux/Mac
   export OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Get your API key from: https://platform.openai.com/api-keys

4. **Run the chatbot:**

   **Command Line Interface:**
   ```bash
   python chatbot.py
   ```
   
   **Web Interface:**
   ```bash
   python app.py
   ```
   Then open your browser and navigate to `http://localhost:5000`

## Usage

### Command Line Interface

Run `python chatbot.py` and start chatting! Commands:
- Type your message and press Enter
- Type `quit` or `exit` to end the conversation
- Type `clear` to clear conversation history
- Type `history` to view conversation history

### Web Interface

1. Start the Flask server: `python app.py`
2. Open `http://localhost:5000` in your browser
3. Start chatting with the AI assistant
4. Use the Settings button to configure:
   - Model selection (GPT-3.5 Turbo, GPT-4, etc.)
   - Temperature (controls randomness)
   - Max tokens (response length)

## Project Structure

```
openai-gpt-chatbot/
├── chatbot.py          # Main chatbot class and CLI
├── app.py              # Flask web application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables example
├── README.md           # This file
├── templates/
│   └── index.html      # Web interface HTML
└── static/
    ├── style.css       # Stylesheet
    └── script.js       # Frontend JavaScript
```

## Code Examples

### Basic Usage

```python
from chatbot import GPTChatbot

# Initialize chatbot
chatbot = GPTChatbot(model="gpt-3.5-turbo")

# Set custom system prompt
chatbot.set_system_prompt("You are a helpful assistant.")

# Get response
response = chatbot.get_response("Hello, how are you?")
print(response)

# Save conversation
chatbot.save_conversation("conversation.json")
```

### Using GPT-4

```python
from chatbot import GPTChatbot

# Initialize with GPT-4
chatbot = GPTChatbot(model="gpt-4")

# Get response with custom parameters
response = chatbot.get_response(
    "Explain quantum computing",
    temperature=0.8,
    max_tokens=1000
)
```

## Configuration

Edit `config.py` to customize:
- Default model
- Temperature settings
- Max tokens
- System prompts
- Conversation settings

## API Endpoints (Web Interface)

### Basic Endpoints
- `GET /` - Main chat interface
- `POST /api/chat` - Send message and get response
- `POST /api/chat/stream` - Stream response (Server-Sent Events)
- `POST /api/clear` - Clear conversation history
- `GET /api/history` - Get conversation history
- `GET /api/info` - Get application information

### Advanced Endpoints
- `GET /api/stats` - Get conversation statistics and token usage
- `POST /api/reset-stats` - Reset statistics
- `GET /api/export/json` - Export conversation as JSON
- `GET /api/export/txt` - Export conversation as TXT
- `POST /api/search` - Search conversation history
- `GET /api/summary` - Get conversation summary
- `GET /api/personas` - Get all available personas
- `POST /api/personas/<key>` - Set persona for session
- `GET /api/templates` - Get conversation templates

## Advanced Features

### Streaming Responses

Enable real-time streaming for faster perceived response times:

```python
# In web interface, toggle "Stream Response" checkbox
# Or in code:
for chunk in chatbot.get_streaming_response("Hello", callback=print):
    # Process each chunk
    pass
```

### Token Usage Tracking

Monitor your API usage:

```python
stats = chatbot.get_conversation_stats()
print(f"Total tokens: {stats['token_usage']['total_tokens']}")
print(f"Total requests: {stats['total_requests']}")
```

### Export Conversations

Export your conversations in multiple formats:

```python
# Export as JSON
chatbot.save_conversation("chat.json")

# Export as TXT
chatbot.export_conversation_txt("chat.txt")
```

### Search Conversations

Search through conversation history:

```python
results = chatbot.search_conversation("python")
for msg in results:
    print(f"{msg['role']}: {msg['content']}")
```

### Custom Personas

Use pre-built personas or create your own:

```python
from personas import get_persona

persona = get_persona("coding")
chatbot.set_system_prompt(persona['system_prompt'])
```

Available personas:
- `default` - General assistant
- `coding` - Programming expert
- `creative` - Creative writer
- `teacher` - Educational tutor
- `business` - Business advisor
- `friendly` - Casual chat
- `technical` - Technical expert
- `translator` - Translation assistant

## Customization

### Change System Prompt

```python
chatbot.set_system_prompt("You are a coding assistant specialized in Python.")
```

### Adjust Response Parameters

```python
response = chatbot.get_response(
    user_message,
    temperature=0.9,  # More creative (0.0-2.0)
    max_tokens=1000   # Longer responses
)
```

### Save and Load Conversations

```python
# Save conversation
chatbot.save_conversation("my_chat.json")

# Load conversation
chatbot.load_conversation("my_chat.json")
```

## Troubleshooting

### API Key Issues

- Make sure your `.env` file contains `OPENAI_API_KEY=your_key`
- Or set the environment variable: `export OPENAI_API_KEY=your_key`
- Verify your API key is valid at [OpenAI Platform](https://platform.openai.com)

### Import Errors

- Install all dependencies: `pip install -r requirements.txt`
- Make sure you're using Python 3.7+

### Rate Limits

- OpenAI API has rate limits based on your plan
- If you hit rate limits, wait a moment and try again
- Consider upgrading your OpenAI plan for higher limits

## Support

For support, questions, or more projects:
- **Website:** https://rskworld.in
- **Email:** help@rskworld.in
- **Phone:** +91 93305 39277

## License

This project is provided as-is for educational and development purposes.

## Credits

**Created by RSK World**  
Visit [https://rskworld.in](https://rskworld.in) for more free programming resources and source code.

---

## Documentation

For complete documentation including:
- Quick start guide
- Advanced features
- API reference
- Code examples
- Troubleshooting
- And more...

**See [DOCUMENTATION.md](DOCUMENTATION.md)**

---

© 2026 RSK World | All Rights Reserved

