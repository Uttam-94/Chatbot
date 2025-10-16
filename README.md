# AI Chatbot with Modern UI

A beautiful, user-friendly chatbot application built with FastAPI backend and React frontend, powered by DeepSeek API for natural conversation.

## Features

- 🤖 **AI-Powered Conversations**: Uses DeepSeek API for fast, accurate, and intelligent responses
- 🎨 **Modern UI**: Beautiful, responsive design with Tailwind CSS
- 💬 **Real-time Chat**: Smooth messaging experience with typing indicators
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- 🔄 **Auto-scroll**: Messages automatically scroll to show latest content
- ⚡ **Fast Performance**: Optimized for speed and smooth interactions

## Project Structure

```
ChatBot/
├── Backend/
│   ├── app.py              # FastAPI backend server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js         # Main React component
│   │   ├── index.css      # Global styles with Tailwind
│   │   └── components/
│   │       └── ChatWindow.js # Chat interface component
│   ├── package.json       # Node.js dependencies
│   ├── tailwind.config.js # Tailwind configuration
│   └── postcss.config.js  # PostCSS configuration
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- DeepSeek API key (free at https://platform.deepseek.com/)

## Installation & Setup

### 1. Backend Setup

Navigate to the Backend directory and set up the Python environment:

```bash
cd Backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure DeepSeek API

**Option A: Using the setup script (Recommended)**
```bash
# From the project root directory
python setup_deepseek.py
```

**Option B: Manual setup**
1. Get your API key from https://platform.deepseek.com/
2. Create a `.env` file in the project root:
   ```
   DEEPSEEK_API_KEY=your-api-key-here
   ```
3. Or set environment variable:
   ```bash
   export DEEPSEEK_API_KEY="your-api-key-here"
   ```

### 3. Frontend Setup

Navigate to the frontend directory and install dependencies:

```bash
cd frontend

# Install dependencies
npm install
```

## Running the Application

### 1. Start the Backend Server

```bash
cd Backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at `http://localhost:8000`

### 2. Start the Frontend Development Server

In a new terminal:

```bash
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

1. Open your browser and go to `http://localhost:3000`
2. Start chatting with the AI assistant
3. The chatbot will respond using the DialoGPT model
4. Enjoy natural conversations with your AI assistant!

## API Endpoints

- `GET /` - Health check endpoint
- `POST /chat` - Send a message to the chatbot
  - Request body: `{"message": "Your message here"}`
  - Response: `{"response": "AI response here"}`

## Features in Detail

### Modern UI Components
- **Gradient backgrounds** for visual appeal
- **Animated message bubbles** with smooth transitions
- **Typing indicators** to show when the AI is responding
- **Avatar icons** for both user and AI
- **Responsive design** that adapts to different screen sizes

### Enhanced User Experience
- **Auto-scroll** to latest messages
- **Loading states** with animated dots
- **Error handling** with user-friendly messages
- **Keyboard shortcuts** (Enter to send, Shift+Enter for new line)
- **Disabled states** to prevent spam during loading

### Technical Improvements
- **CORS enabled** for cross-origin requests
- **Proper error handling** in both frontend and backend
- **Optimized API responses** with consistent structure
- **Modern React hooks** for state management
- **Tailwind CSS** for consistent, maintainable styling

## Troubleshooting

### Backend Issues
- Make sure Python dependencies are installed: `pip install -r requirements.txt`
- Check that the server is running on port 8000
- Verify the DialoGPT model is downloading correctly (first run may take time)

### Frontend Issues
- Ensure Node.js dependencies are installed: `npm install`
- Check that the development server is running on port 3000
- Verify Tailwind CSS is properly configured

### Connection Issues
- Make sure both servers are running simultaneously
- Check that CORS is properly configured in the backend
- Verify the API URL in the frontend matches the backend port

## Customization

### Styling
- Modify `frontend/src/index.css` for global styles
- Update `frontend/tailwind.config.js` for theme customization
- Edit component styles directly in the JSX files

### AI Model
- Change the model in `Backend/app.py` by updating the model name
- Adjust generation parameters (temperature, top_k, top_p) for different response styles

### Features
- Add new API endpoints in `Backend/app.py`
- Create new React components in `frontend/src/components/`
- Extend the chat functionality with additional features

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this chatbot!

---

**Happy Chatting! 🤖💬**
