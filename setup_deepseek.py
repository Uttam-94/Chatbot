#!/usr/bin/env python3
"""
DeepSeek API Setup Script
This script helps you configure your DeepSeek API key for the chatbot.
"""

import os
import sys

def setup_deepseek_api():
    print("🚀 DeepSeek API Setup for Chatbot")
    print("=" * 40)
    print()
    print("To use the DeepSeek API, you need to:")
    print("1. Visit: https://platform.deepseek.com/")
    print("2. Sign up for an account")
    print("3. Get your API key from the dashboard")
    print()
    
    api_key = input("Enter your DeepSeek API key (or press Enter to skip): ").strip()
    
    if not api_key:
        print("\n⚠️  No API key provided. You can:")
        print("   - Run this script again later")
        print("   - Set the DEEPSEEK_API_KEY environment variable")
        print("   - Edit the Backend/app.py file directly")
        return
    
    # Create .env file
    env_content = f"DEEPSEEK_API_KEY={api_key}\n"
    
    try:
        with open(".env", "w") as f:
            f.write(env_content)
        print(f"\n✅ API key saved to .env file")
        print("🔄 Please restart your backend server for changes to take effect")
        
        # Also update the app.py file directly
        try:
            with open("Backend/app.py", "r") as f:
                content = f.read()
            
            updated_content = content.replace(
                'DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "your-deepseek-api-key-here")',
                f'DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "{api_key}")'
            )
            
            with open("Backend/app.py", "w") as f:
                f.write(updated_content)
            
            print("✅ API key also updated in Backend/app.py")
            
        except Exception as e:
            print(f"⚠️  Could not update Backend/app.py: {e}")
            print("   Please manually update the API key in Backend/app.py")
            
    except Exception as e:
        print(f"❌ Error saving API key: {e}")
        return
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Restart your backend server")
    print("2. Start your frontend")
    print("3. Test the chatbot with your DeepSeek API!")

if __name__ == "__main__":
    setup_deepseek_api()
