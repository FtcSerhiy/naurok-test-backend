import hug
from hug.middleware import CORSMiddleware
import download
import key

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.post('/')
def index(response, body=None):
    name = body.get('name')
    amount = body.get('amount')
    subject = body.get('subject')
    klass = body.get('klass')

    page = download.find(str(name), int(amount), str(subject), int(klass))
    urls = download.get_urls(page)
    return key.parse(urls[0])

