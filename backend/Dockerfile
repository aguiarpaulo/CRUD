# Dockerfile-backend

# Image base
FROM python:3.11

# Define the directory in the container
WORKDIR /app

# Copy the files and its dependenciesans install
RUN pip install poetry
COPY pyproject.toml /app/pyproject.toml
#RUN poetry add /app/pyproject.toml
# Instale as dependências listadas no pyproject.toml
RUN poetry install --no-root --no-interaction --no-ansi

# Install Streamlit
RUN pip install streamlit

# Install Uvicorn
RUN poetry add uvicorn

# Copy the other files
COPY . /app

# CExecute the aplication
CMD ["poetry", "run","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]