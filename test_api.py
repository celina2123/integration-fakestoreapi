import requests

def test_get_products_returns_200():
    r = requests.get("https://fakestoreapi.com/products", timeout=20)
    assert r.status_code == 200 
