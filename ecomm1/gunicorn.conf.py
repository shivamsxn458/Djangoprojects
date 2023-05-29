import os
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Configure Django settings
settings.configure()

# Add the static file serving rule
def on_starting(server):
    server.log.info("Starting Gunicorn.")
    server.log.info(f"Serving static files from {settings.STATIC_ROOT}")

# Rest of the Gunicorn configuration...

