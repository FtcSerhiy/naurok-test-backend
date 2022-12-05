import time
from rich.console import Console
from core import download, key
from rich.table import Table
import rich
import sys

def main():
    console = Console()

    test_name = sys.argv[1]
    subject = sys.argv[2]
    klas = 9
    amount = int(sys.argv[3])
    
    with console.status('[bold green]get keys', spinner='point'):
        pages = download.find(test_name, amount, subject, klas)
        url = download.get_urls(pages)[0]

        obj = key.parse(url)
        table = Table(title='[bold green]Responses')
        table.add_column('Names', style="cyan")
        table.add_column('Responses', style='green')

        for name in list(obj.keys()):
            table.add_row(name, str(obj[name]))

        console.print(table)
