FROM python:alpine

COPY . app/
WORKDIR /app

RUN pip install poetry && poetry install --without dev && apk add gunicorn

# CMD ["uwsgi --http 0.0.0.0:8080 --wsgi-file server/app.py --callable __hug_wsgi__"]
