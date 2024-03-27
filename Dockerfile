# Dockerfile
FROM python:3.8-slim

COPY app.py /app.py

# Expose port 80
EXPOSE 80

CMD ["python3", "/app.py"]
