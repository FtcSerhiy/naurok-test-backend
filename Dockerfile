FROM python:alpine

COPY . .
WORKDIR .

RUN pip install poetry --upgrade pip && poetry install

CMD ["poetry", "run", "gunicorn", "server.app:app"]
