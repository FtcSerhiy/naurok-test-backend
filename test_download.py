import unittest
import download
from bs4 import BeautifulSoup as soup
import requests

class TestDownload(unittest.TestCase):
    # headers = {'Cookie': 'PHPSESSID=2nc0tc2gqbbeemn61nfemg1rd2; _csrf=8ab9ca12f86b271ea575fe42fc372284fc7db05e89a439efd2989132e459fe41a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dgNpBVPzDI4Gr0E8ddao2Oa_9k1YJukx%22%3B%7D; _identity=23639c2665c90ba1ba6dea203eb9824151caff7d10ad1028dff959c39de86effa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A53%3A%22%5B1305266%2C%22TB14XanW7_64ZMZLD7YtrjyBD5s6rDWM%22%2C86313600%5D%22%3B%7D'}
    def test_find(self):
        pass

    def test_filter_blocks(self):
        pass

    def test_filter_urls(self):
        url = 'https://naurok.com.ua/test/vektori-1423805.html'
        page = requests.get(url).content
        response = download.filter_urls(soup(page, 'html.parser'))
        f = open('data.html', 'w')
        f.write(str(response))

        f.close()

    def test_get_urls(self):
        pass

