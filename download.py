from bs4 import BeautifulSoup as soup
import requests

headers = {'Cookie': 'PHPSESSID=2nc0tc2gqbbeemn61nfemg1rd2; _csrf=8ab9ca12f86b271ea575fe42fc372284fc7db05e89a439efd2989132e459fe41a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dgNpBVPzDI4Gr0E8ddao2Oa_9k1YJukx%22%3B%7D; _identity=23639c2665c90ba1ba6dea203eb9824151caff7d10ad1028dff959c39de86effa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A53%3A%22%5B1305266%2C%22TB14XanW7_64ZMZLD7YtrjyBD5s6rDWM%22%2C86313600%5D%22%3B%7D'}

def find(test_name: str, amount: int, subject: str, klass: int) -> list:
    code = requests.get(
        f'http://naurok.com.ua/test/{subject}/klas-{klass}?q={test_name}').content
    page = soup(code, 'html.parser')
    blocks = page.find_all(
        'div', attrs={'class': 'file-item test-item'})
    result = []
    for block in blocks:
        page = filter_blocks(block, amount, test_name)
        if page is not None:
            result.append(page)
    if result is not None:
        return result
    raise NameError

def filter_blocks(block: soup, amount: int, name: str) -> soup:
    link = block.find('div', attrs={'class': 'headline'}).a
    block_amount = block.find('div', attrs={
            'class': 'testCounter'}).text
    if int(block_amount) == amount and link.text == name:
        page = requests.get(f"http://naurok.com.ua{link['href']}", headers=headers).content
        return soup(page, 'html.parser')


def filter_urls(page: soup) -> soup:
    for block in page.find_all('a', attrs={'class': 'test-action-button'}):
        if block.span.text == 'Роздрукувати':
            url = f"https://naurok.com.ua{block['href']}"
            page = requests.get(url, headers=headers).content
            return soup(page, 'html.parser')


def get_urls(pages: list) -> list:
    url = [filter_urls(page) for page in pages]
    return url

if __name__ == '__main__':
    import key
    name = input('Write test name: ')
    amount = int(input('Write amount questions: '))
    klass = int(input('Write your klass: '))
    subject = input('Wrute this subject: ')

    urls = get_urls(find(name, amount, subject, klass))
    print(key.parse(urls[0]))
