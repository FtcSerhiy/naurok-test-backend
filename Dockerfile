FROM python:alpine

COPY . .
WORKDIR .

RUN pip install poetry && poetry install

CMD ["uwsgi --http 0.0.0.0:8080 --wsgi-file server/app.py --callable __hug_wsgi__"]
