# Use a modern Python image with pip included
FROM python:3.11-slim

# Set working directory
WORKDIR /usr/src/app

# Copy requirements first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY templates/ templates/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
