FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# upgrade pip and certificates
# RUN apt-get update && apt-get install -y ca-certificates
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change to app directory where main.py is located
WORKDIR /app/app

# Expose port
EXPOSE 8001

# Run the application using direct file path format
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"] 