import pytest
from app import app

def test():
    with app.test_client() as client:
        response = client.get('/?name=Контрольна робота № 1: "Властивості нерівностей. Лінійні нерівності та їх системи"&amount=8&subject=algebra&klass=9')

        assert response.status_code == 200, f'Status code not correct code: {response.status_code}'
        assert response.get_json()['value'] != ["AttributeError","AttributeError"], f'Return error, {response.get_json()}'
