FROM docker.io/frederikp/python-poetry-alpine

COPY . .
WORKDIR .

RUN poetry -V && poetry install

CMD ["poetry", "run", "gunicorn", "server.app:app"]
