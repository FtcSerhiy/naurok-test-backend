from flask import render_template, Flask, request
from core.data import Key
from core import download, key

app = Flask('naurok test backend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    test_name = str(request.form['test_name'])
    klas = 9
    amount = int(request.form['amount'])
    subject = str(request.form['subject'])

    pages = download.find(test_name, amount, subject, klas)
    try:
        url = download.get_urls(pages)[0]
    except IndexError as err:
        return render_template('result.html', err=err)
    results = key.parse(url)

    return render_template('result.html', responses=results, err=None)


if __name__ == '__main__':
    app.run()

