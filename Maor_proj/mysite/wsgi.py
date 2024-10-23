"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Maor_proj.mysite.settings')

application = get_wsgi_application()
#application = WhiteNoise(application, root='/path/to/staticfiles')
application = WhiteNoise(application, root=os.path.join(settings.BASE_DIR, 'staticfiles'))
