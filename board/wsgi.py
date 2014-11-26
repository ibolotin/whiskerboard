import os

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board.local')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
