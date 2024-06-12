# Dockerfile-frontend

# Image base
FROM python:3.9

# Define the directory in the container
WORKDIR /app

# Copy the files and its dependencies and install
COPY pyproject.toml /app/pyproject.toml
RUN poetry add --no-cache-dir --upgrade -r /app/pyproject.toml

# Copy the other files
COPY . /app

# Execute the aplication
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]