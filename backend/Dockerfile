# Dockerfile-backend

# Image base
FROM python:3.9

# Define the directory in the container
WORKDIR /app

# Copy the files and its dependenciesans install
COPY pyproject.toml /app/pyproject.toml
RUN poetry add --no-cache-dir --upgrade -r /app/pyproject.toml

# Copy the other files
COPY . /app

# CExecute the aplication
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]