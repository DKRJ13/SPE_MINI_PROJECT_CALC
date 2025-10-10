# FROM python:3.11-slim
# WORKDIR /app
# # ENV PYTHONUNBUFFERED=1
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# COPY src/ ./src/
# COPY README.md ./
# ENTRYPOINT ["python", "-m", "src.main"]

# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and other files
COPY src/ ./src/
COPY README.md ./

# Ensure Python output is not buffered (useful for logs)
ENV PYTHONUNBUFFERED=1

# Default command to run your app
ENTRYPOINT ["python", "-u", "-m", "src.main"]
