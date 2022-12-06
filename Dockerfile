FROM python:alpine

COPY . app/
WORKDIR /app

RUN pip install poetry && poetry install --without dev

CMD ["poetry", "run", "gunicorn", "server.app:app"]
