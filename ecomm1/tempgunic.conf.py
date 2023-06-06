import os
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomm1.settings')

# Configure Django settings
settings.configure(ROOT_URLCONF = 'ecomm1.urls')

# Add the static file serving rule
def on_starting(server):
    server.log.info("Starting Gunicorn.")
    server.log.info(f"Serving static files from {settings.STATIC_ROOT}")

# Rest of the Gunicorn configuration...

#env = 'DJANGO_SETTINGS_MODULE=ecomm1.settings'
