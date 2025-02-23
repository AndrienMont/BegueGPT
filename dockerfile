# Use Python 3.11 as base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy and install backend dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files, including frontend.html
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Command to run FastAPI backend
CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]
