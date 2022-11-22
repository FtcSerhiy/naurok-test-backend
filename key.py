from bs4 import BeautifulSoup as soup
import download


def parse(page: soup) -> dict:
    result = {}

    keys = get_keys(page.find('div', attrs={'class': 'answer-key'}))
    answers = get_answers(page)
    requests = [
        get_requests(block) for block in page.find_all(
            'div', attrs={
                'class': 'question-options'})]

    for i in range(len(keys)):
        response = [requests[i][e] for e in keys[i]]
        result.update({answers[i]: response})

    return result

# get answers to test


def get_keys(block: soup):
    keys = [get_ref(e.text) for e in block.find_all('div')]
    return [i for i in keys if i is not None]


def get_ref(block: str) -> list:
    try:
        one = block.split('.')[1]
        two = one.split('(')[0]
        return two.replace(" ", '').split()
    except IndexError as err:
        print(err)


# get all answers from test
def get_answers(page: soup) -> list:
    return [e.find('div', attrs={'class': 'col-md-11 no-padding'}).p.text for e in page.find_all(
        'div', attrs={'class': 'entry-item question-view-item'})]

# get all requests (use for loop)


def get_requests(block: soup) -> dict:
    result = {}
    for e in block.find_all('div', attrs={'class': 'text-only-option'}):
        letter = e.find('div', attrs={'class': 'option-letter'}).text[:-1]
        result.update(
            {letter: e.find('div', attrs={'class': 'option-text'}).p.text})
    return result
