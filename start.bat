@echo off
echo 🚀 Starting AI Chatbot Application...
echo ==================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 16+ first.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed!

REM Backend setup
echo.
echo 🔧 Setting up backend...
cd Backend

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating Python virtual environment...
    python -m venv venv
)

REM Activate virtual environment and install requirements
echo 📥 Installing Python dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt

REM Start backend server in background
echo 🔌 Starting backend server on http://localhost:8000...
start /B uvicorn app:app --reload --host 0.0.0.0 --port 8000

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Frontend setup
echo.
echo 🔧 Setting up frontend...
cd ..\frontend

REM Install npm dependencies
echo 📥 Installing Node.js dependencies...
npm install

REM Start frontend server
echo 🎨 Starting frontend server on http://localhost:3000...
echo.
echo 🌟 Application is starting up!
echo    Frontend: http://localhost:3000
echo    Backend API: http://localhost:8000
echo.
echo Press any key to stop both servers
pause >nul

echo 🛑 Shutting down...
taskkill /f /im python.exe >nul 2>&1
