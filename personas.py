"""
Conversation Templates and Custom Personas

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026

Pre-defined conversation templates and personas for the chatbot.
"""

# Author: RSK World (https://rskworld.in) - Year: 2026
PERSONAS = {
    "default": {
        "name": "Default Assistant",
        "system_prompt": "You are a helpful and friendly AI assistant created by RSK World (https://rskworld.in).",
        "description": "A general-purpose helpful assistant"
    },
    "coding": {
        "name": "Coding Assistant",
        "system_prompt": "You are an expert programming assistant created by RSK World. You help with code writing, debugging, and explaining programming concepts. Always provide clear, well-commented code examples.",
        "description": "Specialized in programming and code assistance"
    },
    "creative": {
        "name": "Creative Writer",
        "system_prompt": "You are a creative writing assistant created by RSK World. You help with storytelling, creative writing, poetry, and imaginative content. Be creative and engaging.",
        "description": "Helps with creative writing and storytelling"
    },
    "teacher": {
        "name": "Educational Tutor",
        "system_prompt": "You are a patient and knowledgeable teacher created by RSK World. You explain concepts clearly, provide examples, and adapt to different learning styles. Make learning enjoyable.",
        "description": "Educational and teaching assistant"
    },
    "business": {
        "name": "Business Advisor",
        "system_prompt": "You are a professional business consultant created by RSK World. You provide strategic advice, analyze business problems, and suggest practical solutions. Be professional and data-driven.",
        "description": "Business and professional consulting"
    },
    "friendly": {
        "name": "Friendly Chat",
        "system_prompt": "You are a friendly and conversational AI created by RSK World. You engage in casual conversation, show empathy, and make people feel comfortable. Be warm and approachable.",
        "description": "Casual and friendly conversations"
    },
    "technical": {
        "name": "Technical Expert",
        "system_prompt": "You are a technical expert created by RSK World. You provide detailed technical explanations, troubleshoot problems, and offer in-depth analysis. Be precise and thorough.",
        "description": "Deep technical expertise and analysis"
    },
    "translator": {
        "name": "Translation Assistant",
        "system_prompt": "You are a multilingual translation assistant created by RSK World. You translate text accurately while preserving meaning and context. Support multiple languages.",
        "description": "Translation and multilingual support"
    }
}

# Author: RSK World (https://rskworld.in) - Year: 2026
CONVERSATION_TEMPLATES = {
    "code_review": {
        "name": "Code Review",
        "messages": [
            {
                "role": "user",
                "content": "Please review this code and provide feedback on best practices, potential improvements, and any issues."
            }
        ]
    },
    "explain_concept": {
        "name": "Explain Concept",
        "messages": [
            {
                "role": "user",
                "content": "Can you explain this concept in simple terms with examples?"
            }
        ]
    },
    "brainstorm": {
        "name": "Brainstorming",
        "messages": [
            {
                "role": "user",
                "content": "Let's brainstorm ideas for:"
            }
        ]
    },
    "problem_solving": {
        "name": "Problem Solving",
        "messages": [
            {
                "role": "user",
                "content": "I'm facing this problem. Can you help me analyze it and suggest solutions?"
            }
        ]
    }
}


def get_persona(persona_key: str) -> dict:
    """
    Get persona configuration by key
    
    Args:
        persona_key: Key of the persona
        
    Returns:
        Persona dictionary or default persona
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return PERSONAS.get(persona_key, PERSONAS["default"])


def get_all_personas() -> dict:
    """
    Get all available personas
    
    Returns:
        Dictionary of all personas
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return PERSONAS


def get_template(template_key: str) -> dict:
    """
    Get conversation template by key
    
    Args:
        template_key: Key of the template
        
    Returns:
        Template dictionary or None
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return CONVERSATION_TEMPLATES.get(template_key)


def get_all_templates() -> dict:
    """
    Get all available templates
    
    Returns:
        Dictionary of all templates
    """
    # Author: RSK World (https://rskworld.in) - Year: 2026
    return CONVERSATION_TEMPLATES

