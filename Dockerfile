# Use official Python runtime as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application into container (excluding .env from .dockerignore)
COPY . .

# Expose port 8030
EXPOSE 8030

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8030/docs')" || exit 1

# Command to run the application
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8030"]
