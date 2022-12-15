import time
from rich.console import Console
from core import download, key
from rich.table import Table
from rich.__main__ import make_test_card
import rich
import sys
from time import sleep
from bs4 import BeautifulSoup as soup

def main():
    console = Console()

    if sys.argv[1] == '--help' or sys.argv[1] == 'h':
        console.print('[bold yellow] How use App?')
        console.print('\n[bold yellow] use cli \'test name\' klas subject amount')

    test_name = sys.argv[1]
    subject = sys.argv[2]
    klas = int(sys.argv[3])
    amount = int(sys.argv[4])
    
    with console.status('[bold green]get keys', spinner='point'):
        pages = download.find(test_name, amount, subject, klas)
        url = download.get_urls(pages[0])
        results = key.parse(url)
        table = Table(title='[bold green]Responses')
        table.add_column('Names', style="cyan")
        table.add_column('Responses', style='green')

        for result in results:
            table.add_row(str(result.name), str(result.response))

    with console.pager(styles=True):
        console.print(table)
