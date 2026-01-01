/*
OpenAI GPT Chatbot - JavaScript
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
Year: 2026
*/

// Author: RSK World (https://rskworld.in) - Year: 2026
// Configuration
let currentModel = 'gpt-3.5-turbo';
let temperature = 0.7;
let maxTokens = 500;
let useStreaming = true;
let isDarkMode = localStorage.getItem('darkMode') === 'true';
let currentPersona = 'default';

// DOM Elements
// Author: RSK World (https://rskworld.in) - Year: 2026
const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const chatMessages = document.getElementById('chatMessages');
const clearBtn = document.getElementById('clearBtn');
const settingsBtn = document.getElementById('settingsBtn');
const settingsModal = document.getElementById('settingsModal');
const closeSettings = document.getElementById('closeSettings');
const saveSettings = document.getElementById('saveSettings');
const modelSelect = document.getElementById('modelSelect');
const temperatureSlider = document.getElementById('temperatureSlider');
const temperatureValue = document.getElementById('temperatureValue');
const maxTokensInput = document.getElementById('maxTokensInput');
const currentModelSpan = document.getElementById('currentModel');
const typingIndicator = document.getElementById('typingIndicator');
const streamToggle = document.getElementById('streamToggle');
const themeToggle = document.getElementById('themeToggle');
const statsBtn = document.getElementById('statsBtn');
const exportBtn = document.getElementById('exportBtn');
const searchBtn = document.getElementById('searchBtn');
const statsModal = document.getElementById('statsModal');
const exportModal = document.getElementById('exportModal');
const searchModal = document.getElementById('searchModal');
const personaSelect = document.getElementById('personaSelect');

// Initialize
// Author: RSK World (https://rskworld.in) - Year: 2026
document.addEventListener('DOMContentLoaded', function() {
    setupEventListeners();
    loadSettings();
    autoResizeTextarea();
    initializeTheme();
    configureMarked();
});

// Setup Event Listeners
// Author: RSK World (https://rskworld.in) - Year: 2026
function setupEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    messageInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    clearBtn.addEventListener('click', clearChat);
    settingsBtn.addEventListener('click', openSettings);
    closeSettings.addEventListener('click', closeSettingsModal);
    saveSettings.addEventListener('click', saveSettingsHandler);
    
    temperatureSlider.addEventListener('input', function() {
        temperatureValue.textContent = this.value;
    });
    
    // Advanced features - Author: RSK World (https://rskworld.in) - Year: 2026
    statsBtn.addEventListener('click', openStats);
    exportBtn.addEventListener('click', openExport);
    searchBtn.addEventListener('click', openSearch);
    themeToggle.addEventListener('click', toggleTheme);
    streamToggle.addEventListener('change', function() {
        useStreaming = this.checked;
    });
    
    // Modal close handlers
    document.getElementById('closeStats').addEventListener('click', closeStatsModal);
    document.getElementById('closeStatsBtn').addEventListener('click', closeStatsModal);
    document.getElementById('closeExport').addEventListener('click', closeExportModal);
    document.getElementById('closeExportBtn').addEventListener('click', closeExportModal);
    document.getElementById('closeSearch').addEventListener('click', closeSearchModal);
    document.getElementById('closeSearchBtn').addEventListener('click', closeSearchModal);
    document.getElementById('exportJSON').addEventListener('click', exportAsJSON);
    document.getElementById('exportTXT').addEventListener('click', exportAsTXT);
    document.getElementById('performSearch').addEventListener('click', performSearch);
    document.getElementById('resetStats').addEventListener('click', resetStats);
    
    // Close modal when clicking outside
    window.addEventListener('click', function(e) {
        if (e.target === settingsModal) closeSettingsModal();
        if (e.target === statsModal) closeStatsModal();
        if (e.target === exportModal) closeExportModal();
        if (e.target === searchModal) closeSearchModal();
    });
    
    // Search on Enter key
    document.getElementById('searchInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// Auto-resize textarea
// Author: RSK World (https://rskworld.in) - Year: 2026
function autoResizeTextarea() {
    messageInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 120) + 'px';
    });
}

// Send Message with Streaming Support
// Author: RSK World (https://rskworld.in) - Year: 2026
async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message) {
        return;
    }
    
    // Remove welcome message if present
    const welcomeMsg = chatMessages.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.remove();
    }
    
    // Add user message to chat
    addMessage('user', message);
    messageInput.value = '';
    messageInput.style.height = 'auto';
    
    // Show typing indicator
    typingIndicator.style.display = 'block';
    sendBtn.disabled = true;
    
    try {
        if (useStreaming && streamToggle.checked) {
            // Use streaming
            await sendStreamingMessage(message);
        } else {
            // Use regular API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    model: currentModel,
                    temperature: temperature,
                    max_tokens: maxTokens
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                addMessage('assistant', data.response, true);
            } else {
                addMessage('assistant', 'Error: ' + (data.error || 'Failed to get response'));
            }
        }
    } catch (error) {
        addMessage('assistant', 'Error: ' + error.message);
    } finally {
        typingIndicator.style.display = 'none';
        sendBtn.disabled = false;
        messageInput.focus();
    }
}

// Send Streaming Message
// Author: RSK World (https://rskworld.in) - Year: 2026
async function sendStreamingMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant';
    
    const icon = document.createElement('div');
    icon.className = 'message-icon';
    icon.innerHTML = '<i class="fas fa-robot"></i>';
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content markdown-content';
    
    messageDiv.appendChild(icon);
    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);
    
    try {
        const response = await fetch('/api/chat/stream', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                model: currentModel,
                temperature: temperature,
                max_tokens: maxTokens
            })
        });
        
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let fullResponse = '';
        
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            
            const chunk = decoder.decode(value);
            const lines = chunk.split('\n');
            
            for (const line of lines) {
                if (line.startsWith('data: ')) {
                    const data = line.slice(6);
                    if (data === '[DONE]') continue;
                    
                    try {
                        const json = JSON.parse(data);
                        if (json.chunk) {
                            fullResponse += json.chunk;
                            if (typeof marked !== 'undefined') {
                                messageContent.innerHTML = marked.parse(fullResponse);
                            } else {
                                messageContent.textContent = fullResponse;
                            }
                            highlightCode(messageContent);
                            chatMessages.scrollTop = chatMessages.scrollHeight;
                        }
                    } catch (e) {
                        // Ignore parse errors
                    }
                }
            }
        }
    } catch (error) {
        messageContent.textContent = 'Error: ' + error.message;
    }
}

// Add Message to Chat with Markdown Support
// Author: RSK World (https://rskworld.in) - Year: 2026
function addMessage(role, content, renderMarkdown = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;
    
    const icon = document.createElement('div');
    icon.className = 'message-icon';
    icon.innerHTML = role === 'user' 
        ? '<i class="fas fa-user"></i>' 
        : '<i class="fas fa-robot"></i>';
    
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    
    if (renderMarkdown && role === 'assistant') {
        messageContent.classList.add('markdown-content');
        if (typeof marked !== 'undefined') {
            messageContent.innerHTML = marked.parse(content);
        } else {
            messageContent.textContent = content;
        }
        highlightCode(messageContent);
    } else {
        messageContent.textContent = content;
    }
    
    messageDiv.appendChild(icon);
    messageDiv.appendChild(messageContent);
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Clear Chat
// Author: RSK World (https://rskworld.in) - Year: 2026
async function clearChat() {
    if (!confirm('Are you sure you want to clear the conversation?')) {
        return;
    }
    
    try {
        const response = await fetch('/api/clear', {
            method: 'POST'
        });
        
        if (response.ok) {
            chatMessages.innerHTML = `
                <div class="welcome-message">
                    <i class="fas fa-robot"></i>
                    <h2>Welcome to OpenAI GPT Chatbot</h2>
                    <p>Start a conversation by typing a message below.</p>
                    <p class="info">Created by <a href="https://rskworld.in" target="_blank">RSK World</a> | Year: 2026</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error clearing chat:', error);
    }
}

// Open Settings Modal
// Author: RSK World (https://rskworld.in) - Year: 2026
function openSettings() {
    modelSelect.value = currentModel;
    temperatureSlider.value = temperature;
    temperatureValue.textContent = temperature;
    maxTokensInput.value = maxTokens;
    personaSelect.value = currentPersona;
    settingsModal.style.display = 'block';
}

// Close Settings Modal
// Author: RSK World (https://rskworld.in) - Year: 2026
function closeSettingsModal() {
    settingsModal.style.display = 'none';
}

// Save Settings
// Author: RSK World (https://rskworld.in) - Year: 2026
async function saveSettingsHandler() {
    currentModel = modelSelect.value;
    temperature = parseFloat(temperatureSlider.value);
    maxTokens = parseInt(maxTokensInput.value);
    const newPersona = personaSelect.value;
    
    currentModelSpan.textContent = currentModel;
    
    // Set persona if changed
    if (newPersona !== currentPersona) {
        try {
            const response = await fetch(`/api/personas/${newPersona}`, {
                method: 'POST'
            });
            const data = await response.json();
            if (response.ok) {
                currentPersona = newPersona;
                alert(`Persona changed to: ${data.persona.name}`);
            }
        } catch (error) {
            console.error('Error setting persona:', error);
        }
    }
    
    // Save to localStorage
    localStorage.setItem('chatbot_model', currentModel);
    localStorage.setItem('chatbot_temperature', temperature);
    localStorage.setItem('chatbot_max_tokens', maxTokens);
    localStorage.setItem('chatbot_persona', currentPersona);
    
    closeSettingsModal();
}

// Load Settings
// Author: RSK World (https://rskworld.in) - Year: 2026
async function loadSettings() {
    const savedModel = localStorage.getItem('chatbot_model');
    const savedTemperature = localStorage.getItem('chatbot_temperature');
    const savedMaxTokens = localStorage.getItem('chatbot_max_tokens');
    const savedPersona = localStorage.getItem('chatbot_persona');
    
    if (savedModel) currentModel = savedModel;
    if (savedTemperature) temperature = parseFloat(savedTemperature);
    if (savedMaxTokens) maxTokens = parseInt(savedMaxTokens);
    if (savedPersona) currentPersona = savedPersona;
    
    currentModelSpan.textContent = currentModel;
    
    // Set persona on load
    if (savedPersona) {
        try {
            await fetch(`/api/personas/${savedPersona}`, { method: 'POST' });
        } catch (error) {
            console.error('Error loading persona:', error);
        }
    }
}

// Configure Marked for Markdown Rendering
// Author: RSK World (https://rskworld.in) - Year: 2026
function configureMarked() {
    if (typeof marked !== 'undefined') {
        marked.setOptions({
            breaks: true,
            gfm: true,
            highlight: function(code, lang) {
                if (lang && typeof hljs !== 'undefined') {
                    try {
                        return hljs.highlight(code, { language: lang }).value;
                    } catch (e) {
                        return hljs.highlightAuto(code).value;
                    }
                }
                return code;
            }
        });
    }
}

// Highlight Code Blocks
// Author: RSK World (https://rskworld.in) - Year: 2026
function highlightCode(element) {
    if (typeof hljs !== 'undefined') {
        element.querySelectorAll('pre code').forEach((block) => {
            try {
                hljs.highlightElement(block);
            } catch (e) {
                // Fallback if highlightElement doesn't work
                try {
                    hljs.highlightBlock(block);
                } catch (e2) {
                    // Ignore if highlighting fails
                }
            }
        });
    }
}

// Theme Management
// Author: RSK World (https://rskworld.in) - Year: 2026
function initializeTheme() {
    if (isDarkMode) {
        document.body.classList.add('dark-mode');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }
}

function toggleTheme() {
    isDarkMode = !isDarkMode;
    document.body.classList.toggle('dark-mode', isDarkMode);
    localStorage.setItem('darkMode', isDarkMode);
    themeToggle.innerHTML = isDarkMode 
        ? '<i class="fas fa-sun"></i>' 
        : '<i class="fas fa-moon"></i>';
}

// Statistics Functions
// Author: RSK World (https://rskworld.in) - Year: 2026
async function openStats() {
    statsModal.style.display = 'block';
    await loadStats();
}

function closeStatsModal() {
    statsModal.style.display = 'none';
}

async function loadStats() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();
        
        const statsContent = document.getElementById('statsContent');
        statsContent.innerHTML = `
            <div class="stats-grid">
                <div class="stat-item">
                    <h3>${data.total_messages || 0}</h3>
                    <p>Total Messages</p>
                </div>
                <div class="stat-item">
                    <h3>${data.total_requests || 0}</h3>
                    <p>Total Requests</p>
                </div>
                <div class="stat-item">
                    <h3>${data.token_usage?.total_tokens || 0}</h3>
                    <p>Total Tokens</p>
                </div>
                <div class="stat-item">
                    <h3>${data.token_usage?.prompt_tokens || 0}</h3>
                    <p>Prompt Tokens</p>
                </div>
                <div class="stat-item">
                    <h3>${data.token_usage?.completion_tokens || 0}</h3>
                    <p>Completion Tokens</p>
                </div>
            </div>
            <div class="stats-details">
                <p><strong>Session Start:</strong> ${new Date(data.start_time).toLocaleString()}</p>
            </div>
        `;
    } catch (error) {
        document.getElementById('statsContent').innerHTML = 
            '<p>Error loading statistics: ' + error.message + '</p>';
    }
}

async function resetStats() {
    if (!confirm('Are you sure you want to reset statistics?')) return;
    
    try {
        await fetch('/api/reset-stats', { method: 'POST' });
        await loadStats();
    } catch (error) {
        alert('Error resetting stats: ' + error.message);
    }
}

// Export Functions
// Author: RSK World (https://rskworld.in) - Year: 2026
function openExport() {
    exportModal.style.display = 'block';
}

function closeExportModal() {
    exportModal.style.display = 'none';
}

function exportAsJSON() {
    window.location.href = '/api/export/json';
    closeExportModal();
}

function exportAsTXT() {
    window.location.href = '/api/export/txt';
    closeExportModal();
}

// Search Functions
// Author: RSK World (https://rskworld.in) - Year: 2026
function openSearch() {
    searchModal.style.display = 'block';
    document.getElementById('searchInput').focus();
}

function closeSearchModal() {
    searchModal.style.display = 'none';
    document.getElementById('searchResults').innerHTML = '';
}

async function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    if (!query) {
        alert('Please enter a search query');
        return;
    }
    
    const resultsDiv = document.getElementById('searchResults');
    resultsDiv.innerHTML = '<p>Searching...</p>';
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });
        
        const data = await response.json();
        
        if (data.results && data.results.length > 0) {
            let html = `<h3>Found ${data.count} result(s):</h3>`;
            data.results.forEach((msg, index) => {
                html += `
                    <div class="search-result-item">
                        <strong>${msg.role.toUpperCase()}:</strong>
                        <p>${msg.content.substring(0, 200)}${msg.content.length > 200 ? '...' : ''}</p>
                    </div>
                `;
            });
            resultsDiv.innerHTML = html;
        } else {
            resultsDiv.innerHTML = '<p>No results found.</p>';
        }
    } catch (error) {
        resultsDiv.innerHTML = '<p>Error searching: ' + error.message + '</p>';
    }
}

