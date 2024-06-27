# CRUD

1. Clone the repository:
```bash
git clone https://github.com/aguiarpaulo/crud.git

cd crud
```
2. Configure the correct Python version with pyenv:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Install project dependencies:
```bash
poetry init
poetry install
```
4. Activate the virtual environment:
```bash
poetry shell
```
5. Run tests to ensure everything is working as expected:
```bash
poetry run pytest -v
```
6. Run the command to view project documentation:
```bash
mkdocs serve
```
7. Run the pipeline run command to perform ETL:
```bash
frontend -> streamlit run frontend/app.py
backend -> python3 app/main

or 

docker compose up

> to rebuild
docker build -t name_of_your_image:tag .
```
8. Check in the data/output folder if the file was generated correctly.
```
Contact:
Paulo Aguiar - aguiarlapaulo@gmail.com