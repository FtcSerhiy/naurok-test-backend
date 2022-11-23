from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
import download
import key
import chardet

app = Flask(__name__)
app.config['JSON_ADD_STATUS'] = False

@app.route('/')
def index():
    print(request.args)
    name = request.args.get('name')
    amount = int(request.args.get('amount'))
    subject = request.args.get('subject')
    klass = int(request.args.get('klass'))

    try:
        response = []
        urls = download.get_urls(download.get_urls(download.find(name, amount, subject, klass)))
        for url in urls:
            response.append(key.parse(url))
    except AttributeError as err:
        print(err)
        # return json_response(err=f'internal server error: {err}', status_=500)
    return json_response(value=response, status_=200)

if __name__ == '__main__':
    app.run()
