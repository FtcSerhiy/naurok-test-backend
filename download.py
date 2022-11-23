from bs4 import BeautifulSoup as soup
import requests


class Find:
    def __init__(self, test_name: str, amount: int, subject: str, klass: int):
        self.name = test_name
        self.amount = amount
        code = requests.get(
            f'http://naurok.com.ua/test/{subject}/klas-{klass}?q={test_name}').content
        page = soup(code, 'html.parser')
        self.blocks = page.find_all(
            'div', attrs={'class': 'file-item test-item'})

    def find(self) -> list:
        result = []
        for block in self.blocks:
            page = self.filter_blocks(block)
            if page is not None:
                result.append(page)
        return result

    def filter_blocks(self, block: soup) -> soup:
        link = block.find('div', attrs={'class': 'headline'}).a
        if int(block.find('div', attrs={
               'class': 'testCounter'}).text) == self.amount and link.text == self.name:
            page = requests.get(f"http://naurok.com.ua{link['href']}").content
            return soup(page, 'html.parser')
        return None


def filter_urls(page: soup) -> soup:
    for block in page.find_all('a', attrs={'class': 'test-action-button'}):
        if block.span.text == 'Роздрукувати':
            page = requests.get(f"http://naurok.com.ua{block['href']}", headers={
                                'Cookie': 'PHPSESSID=2nc0tc2gqbbeemn61nfemg1rd2; _csrf=8ab9ca12f86b271ea575fe42fc372284fc7db05e89a439efd2989132e459fe41a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dgNpBVPzDI4Gr0E8ddao2Oa_9k1YJukx%22%3B%7D; _identity=23639c2665c90ba1ba6dea203eb9824151caff7d10ad1028dff959c39de86effa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A53%3A%22%5B1305266%2C%22TB14XanW7_64ZMZLD7YtrjyBD5s6rDWM%22%2C86313600%5D%22%3B%7D'}).content
            with open('data.html', 'wb') as f:
                f.write(page)
            return soup(page, 'html.parser')


def get_urls(pages: list) -> list:
    url = [filter_urls(page) for page in pages]
    return url


if __name__ == '__main__':
    import key
    name = input('Write test name: ')
    amount = int(input('Write amount questions: '))
    klass = int(input('Write your klass: '))
    subject = input('Write this subject: ')

    urls = get_urls(Find(name, amount, subject, klass).find())
    for url in urls:
        print(key.parse(url))
