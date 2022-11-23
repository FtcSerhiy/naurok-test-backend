from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json
import download
import key
import chardet

app = Flask(__name__)
# json = FlaskJSON(app)

app.config['JSON_ADD_STATUS'] = False

@app.route('/', methods = ['POST'])
def index():
    data = request.get_json()
    name = data['name']
    amount = int(data['amount'])
    subject = data['subject']
    klass = int(data['klass'])
    urls = download.get_urls(download.Find(name, amount, subject, klass).find())
    response = []
    print(urls)
    for url in urls:
        response.append(key.parse(url))
    return json_response(value=response)

if __name__ == '__main__':
    app.run()
