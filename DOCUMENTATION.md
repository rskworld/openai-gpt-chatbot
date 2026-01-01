# OpenAI GPT Chatbot - Complete Documentation

**Author:** RSK World  
**Website:** https://rskworld.in  
**Email:** help@rskworld.in  
**Phone:** +91 93305 39277  
**Year:** 2026

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Quick Start Guide](#quick-start-guide)
3. [Installation](#installation)
4. [Features](#features)
5. [Usage](#usage)
6. [Advanced Features](#advanced-features)
7. [API Endpoints](#api-endpoints)
8. [Configuration](#configuration)
9. [Code Examples](#code-examples)
10. [Project Structure](#project-structure)
11. [Troubleshooting](#troubleshooting)
12. [Errors Fixed](#errors-fixed)
13. [Support](#support)

---

## Project Overview

Complete chatbot project using OpenAI GPT API for intelligent conversations and text generation. This project integrates with OpenAI GPT API to create intelligent conversational interfaces with features including message handling, context management, and response generation.

### Project Details

- **Title:** OpenAI GPT Chatbot
- **Category:** OpenAI Integration
- **Difficulty:** Beginner
- **Technologies:** OpenAI API, Python, GPT-3, GPT-4, ChatGPT, Flask

### Description

This chatbot project integrates with OpenAI GPT API to create intelligent conversational interfaces. Features include message handling, context management, and response generation. Perfect for building chatbots with advanced language understanding and natural conversation capabilities.

---

## Quick Start Guide

### 5-Minute Setup

#### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 2: Set Up API Key

Create a `.env` file in the project root:

**On Windows:**
```bash
copy env_example.txt .env
```

**On Linux/Mac:**
```bash
cp env_example.txt .env
```

Then edit `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

> **Note:** The `.env` file is already in `.gitignore` to keep your API key secure. Never commit your `.env` file to version control!

#### Step 3: Run the Chatbot

**Option A: Command Line Interface**
```bash
python chatbot.py
```

**Option B: Web Interface**
```bash
python app.py
```
Then open http://localhost:5000 in your browser

### That's It!

You're ready to chat with GPT! 🚀

---

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
   
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

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

---

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

---

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
   - Persona selection

---

## Advanced Features

### 1. Streaming Responses
**Real-time token streaming for faster perceived response times**

- Enable/disable streaming via toggle in the UI
- Server-Sent Events (SSE) implementation
- Real-time display of tokens as they're generated
- Better user experience with immediate feedback

**Usage:**
- Toggle "Stream Response" checkbox in the chat interface
- Or use `get_streaming_response()` method in code

### 2. Token Usage Tracking
**Monitor API usage and costs**

- Track prompt tokens, completion tokens, and total tokens
- Real-time statistics display
- Session-based tracking
- Export statistics with conversations

**Access:**
- Click "Stats" button in header
- View in Statistics modal
- Included in exported conversations

### 3. Conversation Statistics
**Comprehensive analytics**

- Total messages count
- Total API requests
- Token usage breakdown
- Session duration
- Reset functionality

### 4. Export Functionality
**Export conversations in multiple formats**

**Formats:**
- **JSON** - Full conversation with metadata and statistics
- **TXT** - Plain text format with conversation and stats

**Features:**
- One-click export
- Includes conversation history
- Includes token usage statistics
- Timestamped filenames

### 5. Conversation Search
**Search through conversation history**

- Full-text search across all messages
- Case-insensitive matching
- Results with context
- Highlight matching content

**Usage:**
- Click "Search" button
- Enter search query
- View matching messages

### 6. Markdown Rendering
**Beautiful markdown and code display**

- Full markdown support
- Code syntax highlighting
- Multiple language support
- Proper formatting for:
  - Headers
  - Lists
  - Code blocks
  - Blockquotes
  - Links

**Libraries:**
- Marked.js for markdown parsing
- Highlight.js for syntax highlighting

### 7. Dark Mode
**Theme switching for better user experience**

- Toggle between light and dark themes
- Persistent theme preference (localStorage)
- Smooth transitions
- Optimized color schemes for both themes

**Usage:**
- Click moon/sun icon in header
- Theme preference saved automatically

### 8. Custom Personas
**Pre-built conversation styles**

**Available Personas:**
1. **Default Assistant** - General-purpose helper
2. **Coding Assistant** - Programming expert
3. **Creative Writer** - Creative writing specialist
4. **Educational Tutor** - Teaching assistant
5. **Business Advisor** - Professional consultant
6. **Friendly Chat** - Casual conversation
7. **Technical Expert** - Deep technical analysis
8. **Translation Assistant** - Multilingual support

**Usage:**
- Select persona in Settings
- Automatically updates system prompt
- Persists across sessions

### 9. Advanced Error Handling
**Robust error management**

- Automatic retry with exponential backoff
- Configurable retry attempts (default: 3)
- Graceful error messages
- User-friendly error display

**Features:**
- Network error handling
- API rate limit handling
- Timeout management
- Detailed error logging

### 10. Conversation Summary
**Quick overview of conversations**

- Message count breakdown
- Token usage summary
- First message preview
- Quick statistics

**Access:**
- API endpoint: `/api/summary`
- Programmatic access via `get_conversation_summary()`

---

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

---

## Configuration

Edit `config.py` to customize:
- Default model
- Temperature settings
- Max tokens
- System prompts
- Conversation settings

### Model Settings
- GPT-3.5 Turbo (default)
- GPT-4
- GPT-4 Turbo
- Easy model switching

### Response Parameters
- Temperature control (0.0 - 2.0)
- Max tokens configuration
- Streaming toggle
- Custom system prompts

### Personalization
- Persona selection
- Custom prompts
- Theme preferences
- Settings persistence

---

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

### Streaming Response

```python
for chunk in chatbot.get_streaming_response("Hello"):
    print(chunk, end='', flush=True)
```

### Get Statistics

```python
stats = chatbot.get_conversation_stats()
print(f"Total tokens: {stats['token_usage']['total_tokens']}")
print(f"Total requests: {stats['total_requests']}")
```

### Search Conversation

```python
results = chatbot.search_conversation("python")
for msg in results:
    print(f"{msg['role']}: {msg['content']}")
```

### Export Conversation

```python
# Export as JSON
chatbot.save_conversation("chat.json")

# Export as TXT
chatbot.export_conversation_txt("chat.txt")
```

### Use Persona

```python
from personas import get_persona

persona = get_persona("coding")
chatbot.set_system_prompt(persona['system_prompt'])
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

---

## Project Structure

```
openai-gpt-chatbot/
├── chatbot.py              # Main chatbot class and CLI interface
├── app.py                  # Flask web application
├── config.py               # Configuration settings
├── personas.py              # Personas and templates
├── example_usage.py         # Usage examples
├── setup.py                 # Package setup script
├── requirements.txt         # Python dependencies
├── env_example.txt          # Environment variables example
├── DOCUMENTATION.md         # This file (complete documentation)
├── LICENSE                  # MIT License
├── .gitignore              # Git ignore file
├── templates/
│   └── index.html          # Web interface HTML
└── static/
    ├── style.css           # Stylesheet
    └── script.js           # Frontend JavaScript
```

### Files Created

#### Core Files
1. **chatbot.py** - Main chatbot class with OpenAI API integration
2. **app.py** - Flask web application for web interface
3. **config.py** - Configuration and settings management
4. **example_usage.py** - Comprehensive usage examples
5. **personas.py** - Persona definitions and templates

#### Documentation
6. **DOCUMENTATION.md** - Complete documentation (this file)
7. **LICENSE** - MIT License

#### Configuration
8. **requirements.txt** - Python dependencies
9. **setup.py** - Package setup script
10. **env_example.txt** - Environment variables template
11. **.gitignore** - Git ignore rules

#### Web Interface
12. **templates/index.html** - Main web interface
13. **static/style.css** - Stylesheet
14. **static/script.js** - Frontend JavaScript

---

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

### Common Issues

1. **Module not found errors:** Run `pip install -r requirements.txt`
2. **API key errors:** Check your `.env` file or environment variables
3. **Port already in use:** Change the port in `app.py` or stop the existing process
4. **Streaming not working:** Check browser console for errors, ensure SSE is supported

---

## Errors Fixed

All files and folders have been checked and verified. The following issues were identified and fixed:

### 1. Export Function Fix
**File:** `app.py`
- **Issue:** The export_txt function was trying to use BytesIO incorrectly
- **Fix:** Changed to use `_generate_txt_content()` method directly and write to BytesIO
- **Status:** ✅ Fixed

### 2. Unused Import Removal
**File:** `chatbot.py`
- **Issue:** Unused `StringIO` import in export function
- **Fix:** Removed unused import
- **Status:** ✅ Fixed

### 3. Markdown Library Safety Checks
**File:** `static/script.js`
- **Issue:** Potential errors if marked.js library fails to load
- **Fix:** Added `typeof marked !== 'undefined'` checks before using marked.parse()
- **Status:** ✅ Fixed

### 4. Highlight.js Error Handling
**File:** `static/script.js`
- **Issue:** Potential errors with highlight.js API
- **Fix:** Added try-catch blocks and fallback methods (highlightElement and highlightBlock)
- **Status:** ✅ Fixed

### Code Verification

#### Python Files
✅ `chatbot.py` - No syntax errors, all imports correct
✅ `app.py` - No syntax errors, all imports correct
✅ `config.py` - No syntax errors, all imports correct
✅ `personas.py` - No syntax errors, all imports correct
✅ `example_usage.py` - No syntax errors, all imports correct

#### JavaScript Files
✅ `static/script.js` - All DOM elements verified, error handling added
✅ All getElementById calls match HTML elements

#### HTML Files
✅ `templates/index.html` - All required IDs present, structure correct

#### CSS Files
✅ `static/style.css` - All styles defined, dark mode working

### Status: ✅ ALL CLEAR

The project is ready for use. All errors have been fixed and the code is verified.

---

## UI/UX Enhancements

### Modern Interface
- Clean, modern design
- Responsive layout
- Smooth animations
- Intuitive navigation

### Responsive Design
- Mobile-friendly
- Tablet optimized
- Desktop enhanced
- Adaptive layouts

### Accessibility
- Keyboard navigation
- Screen reader friendly
- High contrast modes
- Clear visual hierarchy

---

## Technical Features

### Performance
- Efficient token streaming
- Optimized API calls
- Caching where appropriate
- Minimal overhead

### Security
- Session-based isolation
- Secure API key handling
- Input validation
- XSS protection

### Scalability
- Session management
- Stateless API design
- Efficient memory usage
- Concurrent request handling

---

## Testing Recommendations

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set API Key:**
   - Create `.env` file with `OPENAI_API_KEY=your_key`

3. **Run Application:**
   ```bash
   python app.py
   ```

4. **Test Features:**
   - Send messages
   - Toggle streaming
   - Test dark mode
   - Export conversations
   - Search conversations
   - View statistics
   - Change personas

---

## Author Information

All files include author information in comments:
- **Author:** RSK World
- **Website:** https://rskworld.in
- **Email:** help@rskworld.in
- **Phone:** +91 93305 39277
- **Year:** 2026

---

## Support

For support, questions, or more projects:
- **Website:** https://rskworld.in
- **Email:** help@rskworld.in
- **Phone:** +91 93305 39277

---

## License

This project is provided as-is for educational and development purposes.

MIT License - See LICENSE file for details.

---

## Credits

**Created by RSK World**  
Visit [https://rskworld.in](https://rskworld.in) for more free programming resources and source code.

---

© 2026 RSK World | All Rights Reserved

