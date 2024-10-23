# serve.py
import os
from waitress import serve
from mysite.wsgi import application

port = int(os.environ.get("PORT", 8000))

serve(application, host='0.0.0.0', port=port)
