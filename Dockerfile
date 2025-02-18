# Use an official lightweight Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

# Copy the app code
COPY . .

# Expose port 8080 (Vercel uses this for containers)
EXPOSE 8080

# Run the Flask app
CMD ["python", "api/app.py"]