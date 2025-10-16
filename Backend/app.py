from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os


app = FastAPI()

# Serve React build as static files
app.mount("/", StaticFiles(directory="build", html=True), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:3000",
        "https://chatbot-frontend.onrender.com",  # Update with your actual frontend URL
        "https://*.onrender.com"  # Allow all Render subdomains
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Chatbot API running!"}


# OpenRouter API Configuration
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
# You'll need to get your API key from https://openrouter.ai/
# Never hardcode API keys; read from environment on Render or locally
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# Chat history for context
chat_history = []

# Request structure
class UserInput(BaseModel):
    message: str

def call_openrouter_api(user_message):
    """Call OpenRouter API to get AI response"""
    global chat_history
    
    # Add user message to history
    chat_history.append({"role": "user", "content": user_message})
    
    # Prepare messages for API (keep last 10 messages for context)
    messages = [
        {
            "role": "system", 
            "content": "You are a helpful, friendly, and knowledgeable AI assistant. You provide accurate, helpful, and engaging responses. You can help with questions, have conversations, tell jokes, and assist with various topics. Always be polite and try to be helpful."
        }
    ] + chat_history[-10:]  # Keep last 10 messages for context
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",  # Optional: identifies your app
        "X-Title": "AI Chatbot"  # Optional: identifies your app
    }
    
    data = {
        "model": "deepseek/deepseek-chat",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 500,
        "stream": False
    }
    
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        # Check for API errors in response
        if "error" in result:
            error_msg = result["error"].get("message", "Unknown API error")
            if "invalid" in error_msg.lower() or "authentication" in error_msg.lower():
                return "🔑 API key authentication failed. Please check your OpenRouter API key. You can get a new key from https://openrouter.ai/"
            return f"API Error: {error_msg}"
        
        ai_response = result["choices"][0]["message"]["content"]
        
        # Add AI response to history
        chat_history.append({"role": "assistant", "content": ai_response})
        
        return ai_response
        
    except requests.exceptions.RequestException as e:
        print(f"OpenRouter API error: {e}")
        if "401" in str(e) or "authentication" in str(e).lower():
            return "🔑 API key authentication failed. Please check your OpenRouter API key. You can get a new key from https://openrouter.ai/"
        return "I'm sorry, I'm having trouble connecting to the AI service right now. Please try again later."
    except KeyError as e:
        print(f"Unexpected API response format: {e}")
        return "I received an unexpected response from the AI service. Please try again."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "I encountered an unexpected error. Please try again."

@app.post("/chat")
async def chat(user: UserInput):
    global chat_history
    user_input = user.message.strip()

    # Handle weather requests with fallback
    if "weather" in user_input.lower():
        weather_response = get_weather_data()
        return {"response": weather_response}
    
    # Check if API key is configured
    if not OPENROUTER_API_KEY:
        return {
            "response": "🔧 OpenRouter API is not configured yet. Please add your API key to use the advanced AI features. For now, here are some basic responses:\n\n• Weather info: I can help with weather information\n• General chat: I'm a basic chatbot\n\nTo get your OpenRouter API key, visit: https://openrouter.ai/"
        }
    
    # Call OpenRouter API for better responses
    ai_response = call_openrouter_api(user_input)
    return {"response": ai_response}

def get_weather_data():
    try:
        # Example API call with better error handling
        url = "https://api.weatherapi.com/v1/current.json?key=demo&q=Delhi"
        res = requests.get(url, timeout=5)
        data = res.json()
        
        if 'location' in data and 'current' in data:
            return f"The current temperature in {data['location']['name']} is {data['current']['temp_c']}°C"
        else:
            return "I can help with weather information, but the weather service is currently unavailable. Please try asking about something else!"
    except Exception as e:
        return "I can help with weather information, but the weather service is currently unavailable. Please try asking about something else!"

