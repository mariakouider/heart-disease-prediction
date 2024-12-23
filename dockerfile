# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Google Cloud Run
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
