import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('SERVER_ENV') == 'Main':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.product')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')

application = get_wsgi_application()
