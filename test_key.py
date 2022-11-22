import unittest
import key
from bs4 import BeautifulSoup as soup
import requests

class TestKey(unittest.TestCase):
    headers = {'Cookie':'PHPSESSID=2nc0tc2gqbbeemn61nfemg1rd2; _csrf=8ab9ca12f86b271ea575fe42fc372284fc7db05e89a439efd2989132e459fe41a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dgNpBVPzDI4Gr0E8ddao2Oa_9k1YJukx%22%3B%7D; _identity=23639c2665c90ba1ba6dea203eb9824151caff7d10ad1028dff959c39de86effa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A53%3A%22%5B1305266%2C%22TB14XanW7_64ZMZLD7YtrjyBD5s6rDWM%22%2C86313600%5D%22%3B%7D'}
    def test_parse(self):
        url = "https://naurok.com.ua/test/kontrolna-robota-1-vlastivosti-nerivnostey-liniyni-nerivnosti-ta-h-sistemi-1831724/print"
        page = requests.get(url, headers=self.headers).content
        print(key.parse(soup(page, 'html.parser')))

        # page = soup(requests.get('https://naurok.com.ua/test/vlastivosti-funkci-1829415/print', headers=self.headers).content, 'html.parser')
        # print(key.parse(page))

    def test_get_key(self):
        url = "https://naurok.com.ua/test/kontrolna-robota-1-vlastivosti-nerivnostey-liniyni-nerivnosti-ta-h-sistemi-1831724/print"
        page = requests.get(url, headers=self.headers).content
        page = soup(page, 'html.parser').find('div', attrs={'class':'answer-key'})
        one_key = [['г'], ['в'], ['в'], ['г'], ['б'], ['б'], ['а'], ['б']]
        keys = key.get_keys(page)
        for i in range(len(keys)):
            self.assertAlmostEqual(keys[i], one_key[i])

        page = soup(requests.get('https://naurok.com.ua/test/vlastivosti-funkci-1829415/print', headers=self.headers).content, 'html.parser')
        right_key = [
                ['а', 'б', 'в', 'г'],
                ['а'], ['б'], ['б', 'в'], ['б'], ['б'], ['а', 'г'], ['в'], ['б', 'в'], ['в', 'г'], ['в']]
        keys = key.get_keys(page)
        print(keys)

    def test_get_answers(self):
        page = requests.get("https://naurok.com.ua/test/kontrolna-robota-1-vlastivosti-nerivnostey-liniyni-nerivnosti-ta-h-sistemi-1831724/print", headers=self.headers).content
        answers = key.get_answers(soup(page, 'html.parser'))
        self.assertAlmostEqual(len(answers), 8)

    def test_get_requests(self):
        page = requests.get("https://naurok.com.ua/test/kontrolna-robota-1-vlastivosti-nerivnostey-liniyni-nerivnosti-ta-h-sistemi-1831724/print", headers=self.headers).content
        result = {'а': "[8; +∞)\xa0\xa0\xa0", 'б': "[- 8; +∞)\xa0\xa0\xa0\xa0", 'в': "(-∞; 8]\xa0\xa0\xa0\xa0\xa0\xa0", 'г': "(-∞; -8]\xa0\xa0"}
        self.assertAlmostEqual(key.get_requests(soup(page, 'html.parser').find('div', attrs={'class':'question-options'})), result)
    
    def test_get_ref(self):
        block = '1. a (1 балл)'
        response = key.get_ref(block)
        assert response != ['а'], 'Response letter is not walid'

        block = '1. а б в (1 балл)'
        response = key.get_ref(block)
        assert response != ['а', 'б', 'в'], 'Response letter is not valid'

