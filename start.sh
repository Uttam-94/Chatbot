#!/bin/bash

echo "🚀 Starting AI Chatbot Application..."
echo "=================================="

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16+ first."
    exit 1
fi

echo "✅ Prerequisites check passed!"

# Backend setup
echo ""
echo "🔧 Setting up backend..."
cd Backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating Python virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📥 Installing Python dependencies..."
pip install -r requirements.txt

# Start backend server in background
echo "🔌 Starting backend server on http://localhost:8000..."
uvicorn app:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Frontend setup
echo ""
echo "🔧 Setting up frontend..."
cd ../frontend

# Install npm dependencies
echo "📥 Installing Node.js dependencies..."
npm install

# Start frontend server
echo "🎨 Starting frontend server on http://localhost:3000..."
echo ""
echo "🌟 Application is starting up!"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Start frontend server
npm start

# This will run until npm start is terminated

