"""
Flask Web Application for OpenAI GPT Chatbot

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026

Web interface for the OpenAI GPT Chatbot with conversation management.
"""

from flask import Flask, render_template, request, jsonify, session, Response, send_file
from chatbot import GPTChatbot
from config import Config
from personas import get_all_personas, get_persona, get_all_templates
import os
import uuid
import json as json_lib
from datetime import datetime
from io import BytesIO

# Author: RSK World (https://rskworld.in) - Year: 2026
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "rskworld-2026-secret-key-change-in-production")

# Store chatbot instances per session
# Author: RSK World (https://rskworld.in) - Year: 2026
chatbots = {}


def get_chatbot():
    """
    Get or create chatbot instance for current session
    
    Returns:
        GPTChatbot instance
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    
    session_id = session['session_id']
    
    if session_id not in chatbots:
        chatbots[session_id] = GPTChatbot(
            api_key=Config.OPENAI_API_KEY,
            model=Config.DEFAULT_MODEL
        )
        chatbots[session_id].set_system_prompt(Config.DEFAULT_SYSTEM_PROMPT)
    
    return chatbots[session_id]


@app.route('/')
def index():
    """
    Render main chat interface
    
    Returns:
        Rendered HTML template
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    app_info = Config.get_info()
    return render_template('index.html', app_info=app_info)


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat API requests
    
    Returns:
        JSON response with assistant message
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        model = data.get('model', Config.DEFAULT_MODEL)
        temperature = float(data.get('temperature', Config.DEFAULT_TEMPERATURE))
        max_tokens = int(data.get('max_tokens', Config.DEFAULT_MAX_TOKENS))
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        chatbot = get_chatbot()
        chatbot.model = model
        
        response = chatbot.get_response(
            user_message,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/clear', methods=['POST'])
def clear_history():
    """
    Clear conversation history
    
    Returns:
        JSON response confirming history cleared
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        chatbot.clear_history()
        return jsonify({'message': 'Conversation history cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    """
    Get conversation history
    
    Returns:
        JSON response with conversation history
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        history = chatbot.get_conversation_history()
        return jsonify({'history': history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/info', methods=['GET'])
def get_info():
    """
    Get application information
    
    Returns:
        JSON response with app information
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return jsonify(Config.get_info())


@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    """
    Handle streaming chat API requests
    
    Returns:
        Server-Sent Events stream
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        model = data.get('model', Config.DEFAULT_MODEL)
        temperature = float(data.get('temperature', Config.DEFAULT_TEMPERATURE))
        max_tokens = int(data.get('max_tokens', Config.DEFAULT_MAX_TOKENS))
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        chatbot = get_chatbot()
        chatbot.model = model
        
        def generate():
            try:
                for chunk in chatbot.get_streaming_response(user_message, temperature, max_tokens):
                    yield f"data: {json_lib.dumps({'chunk': chunk})}\n\n"
                yield f"data: {json_lib.dumps({'done': True})}\n\n"
            except Exception as e:
                yield f"data: {json_lib.dumps({'error': str(e)})}\n\n"
        
        return Response(generate(), mimetype='text/event-stream')
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """
    Get conversation statistics and token usage
    
    Returns:
        JSON response with statistics
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        stats = chatbot.get_conversation_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/export/json', methods=['GET'])
def export_json():
    """
    Export conversation as JSON
    
    Returns:
        JSON file download
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        history = chatbot.get_conversation_history()
        stats = chatbot.get_conversation_stats()
        
        export_data = {
            "conversation": history,
            "statistics": stats,
            "export_date": datetime.now().isoformat(),
            "author": "RSK World (https://rskworld.in)"
        }
        
        json_str = json_lib.dumps(export_data, indent=2, ensure_ascii=False)
        filename = f"conversation_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        return Response(
            json_str,
            mimetype='application/json',
            headers={'Content-Disposition': f'attachment; filename={filename}'}
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/export/txt', methods=['GET'])
def export_txt():
    """
    Export conversation as plain text
    
    Returns:
        TXT file download
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        filename = f"conversation_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Generate text content
        content = chatbot._generate_txt_content()
        
        # Create BytesIO with content
        output = BytesIO()
        output.write(content.encode('utf-8'))
        output.seek(0)
        
        return send_file(
            output,
            mimetype='text/plain',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/search', methods=['POST'])
def search_conversation():
    """
    Search conversation history
    
    Returns:
        JSON response with matching messages
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Search query is required'}), 400
        
        chatbot = get_chatbot()
        results = chatbot.search_conversation(query)
        
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/summary', methods=['GET'])
def get_summary():
    """
    Get conversation summary
    
    Returns:
        JSON response with conversation summary
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        summary = chatbot.get_conversation_summary()
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/reset-stats', methods=['POST'])
def reset_stats():
    """
    Reset conversation statistics
    
    Returns:
        JSON response confirming reset
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        chatbot = get_chatbot()
        chatbot.reset_stats()
        return jsonify({'message': 'Statistics reset successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/personas', methods=['GET'])
def get_personas():
    """
    Get all available personas
    
    Returns:
        JSON response with personas
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return jsonify(get_all_personas())


@app.route('/api/personas/<persona_key>', methods=['POST'])
def set_persona(persona_key):
    """
    Set persona for current session
    
    Args:
        persona_key: Key of the persona to set
        
    Returns:
        JSON response confirming persona set
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    try:
        persona = get_persona(persona_key)
        chatbot = get_chatbot()
        chatbot.set_system_prompt(persona['system_prompt'])
        return jsonify({
            'message': f"Persona '{persona['name']}' set successfully",
            'persona': persona
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/templates', methods=['GET'])
def get_templates():
    """
    Get all available conversation templates
    
    Returns:
        JSON response with templates
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return jsonify(get_all_templates())


if __name__ == '__main__':
    # Author: RSK World (https://rskworld.in) - Year: 2026
    if not Config.validate():
        print("Warning: OPENAI_API_KEY not set. Please set it in .env file.")
        print("For more information, visit: https://rskworld.in")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

