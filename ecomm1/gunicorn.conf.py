from django.conf import settings

# ...

# Add the static file serving rule
def on_starting(server):
    server.log.info("Starting Gunicorn.")
    server.log.info(f"Serving static files from {settings.STATIC_ROOT}")

# ...

# Gunicorn configuration
bind = "0.0.0.0:8000"
workers = 4
accesslog = "/home/ubuntu/access.log"
errorlog = "/home/ubuntu/error.log"
timeout = 120
on_starting = on_starting
