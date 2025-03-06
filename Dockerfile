# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt --timeout=100 --retries=10

# Copy all application files (including static files)
COPY . .

# ✅ Remove unnecessary duplicate static copy
# Expose Streamlit's port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
