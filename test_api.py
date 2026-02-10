import requests

def test_get_products_returns_200():
    r = requests.get("https://fakestoreapi.com/products")
    assert r.status_code == 200
