#!/usr/bin/env python
"""
Local testing script for Railway deployment
This script runs the Django app with waitress server locally
"""
import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# Set environment variables for local testing
os.environ.setdefault('PORT', '8000')
os.environ.setdefault('SECRET_KEY', 'test-secret-key-for-local-development')
os.environ.setdefault('DEBUG', 'True')
os.environ.setdefault('DATABASE_URL', 'sqlite:///db.sqlite3')
os.environ.setdefault('ALLOWED_HOSTS', 'localhost,127.0.0.1')

if __name__ == '__main__':
    from waitress import serve
    from Maor_proj.mysite.wsgi import application
    
    port = int(os.environ.get('PORT', 8000))
    print(f"🚀 Starting Django app on http://localhost:{port}")
    print("📋 Environment variables:")
    print(f"   PORT: {os.environ.get('PORT')}")
    print(f"   DEBUG: {os.environ.get('DEBUG')}")
    print(f"   DATABASE_URL: {os.environ.get('DATABASE_URL')}")
    print("🔧 This simulates Railway's deployment environment")
    print("⏹️  Press Ctrl+C to stop")
    
    serve(application, host='0.0.0.0', port=port)
