# Use the lightweight Python image
FROM python:3.9-slim

# Avoid writing .pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Buffer stdout and stderr so logs appear immediately
ENV PYTHONUNBUFFERED 1

# Install git (useful for version control inside the container)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# We don't copy code here. VS Code mounts it automatically!