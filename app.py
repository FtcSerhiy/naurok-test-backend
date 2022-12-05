import hug
from hug.middleware import CORSMiddleware
from core import download, key

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.post('/')
def index(response, body):
    name = body.get('name')
    amount = body.get('amount')
    subject = body.get('subject')
    klass = body.get('klass')

    page = download.find(str(name), int(amount), str(subject), int(klass))
    urls = download.get_urls(page)

    return {'value': key.parse(urls[0])}


@hug.get('/')
def testsss():
    return 'ok'
