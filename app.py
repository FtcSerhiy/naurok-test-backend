import hug
import download
import key

# @hug.cli()
@hug.get('/')
# @hug.local()
def index(name: hug.types.text, amount: hug.types.number, subject: hug.types.text, klass: hug.types.number):
    page = download.find(str(name), int(amount), str(subject), int(klass))
    urls = download.get_urls(page)
    return key.parse(urls[0])

# if __name__ == '__main__':
    # index.interface.cli()
