#!/bin/bash
# Quick deployment script for Render

echo "🚀 Preparing Chatbot for Render Deployment"
echo "=========================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - Ready for Render deployment"
    echo "✅ Git repository initialized"
else
    echo "📦 Updating Git repository..."
    git add .
    git commit -m "Update for Render deployment"
    echo "✅ Git repository updated"
fi

echo ""
echo "📋 Next Steps:"
echo "1. Create a GitHub repository"
echo "2. Push your code:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git push -u origin main"
echo ""
echo "3. Go to https://render.com"
echo "4. Create two services:"
echo "   - Web Service (Backend): Use Backend/ folder"
echo "   - Static Site (Frontend): Use frontend/ folder"
echo ""
echo "5. Set environment variables:"
echo "   - OPENROUTER_API_KEY: Your API key"
echo "   - REACT_APP_API_URL: Your backend URL"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
echo ""
echo "🎉 Your chatbot is ready for deployment!"

