# Deploy Chatbot to Render

## Prerequisites
1. GitHub account
2. Render account (free at https://render.com)
3. Your OpenRouter API key

## Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

## Step 2: Deploy Backend to Render
1. Go to https://render.com and sign in
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the backend service:
   - **Name**: `chatbot-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r Backend/requirements.txt`
   - **Start Command**: `cd Backend && uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - `OPENROUTER_API_KEY`: Your OpenRouter API key
5. Click "Create Web Service"

## Step 3: Deploy Frontend to Render
1. In Render dashboard, click "New +" → "Static Site"
2. Connect the same GitHub repository
3. Configure the frontend service:
   - **Name**: `chatbot-frontend`
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`
   - **Environment Variables**:
     - `REACT_APP_API_URL`: `https://chatbot-backend.onrender.com` (update with your actual backend URL)
4. Click "Create Static Site"

## Step 4: Update CORS Settings
After deployment, update the CORS origins in `Backend/app.py`:
```python
allow_origins=[
    "http://localhost:3000", 
    "http://127.0.0.1:3000",
    "https://YOUR_FRONTEND_URL.onrender.com",  # Replace with your actual frontend URL
    "https://*.onrender.com"
],
```

## Step 5: Test Your Deployment
1. Visit your frontend URL
2. Test the chatbot functionality
3. Check backend logs in Render dashboard if there are issues

## Environment Variables Needed
- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `REACT_APP_API_URL`: Your backend URL (set automatically)

## Troubleshooting
- Check Render logs for deployment issues
- Ensure all environment variables are set
- Verify CORS settings match your frontend URL
- Check that the API key is valid and has sufficient credits

## Cost
- Backend: Free tier available (with some limitations)
- Frontend: Free tier available
- OpenRouter: Pay per use (very affordable)

