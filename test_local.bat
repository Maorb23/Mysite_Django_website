@echo off
REM Local testing script for Railway deployment
echo 🚀 Starting local Railway simulation...

REM Set environment variables
set PORT=8000
set SECRET_KEY=test-secret-key-for-local-development
set DEBUG=True
set DATABASE_URL=sqlite:///db.sqlite3
set ALLOWED_HOSTS=localhost,127.0.0.1

REM Activate virtual environment and run Django
call railway_test_env\Scripts\activate.bat
echo ✅ Virtual environment activated

echo 📋 Testing with Django development server (Railway uses gunicorn)
python manage.py runserver 0.0.0.0:8000
