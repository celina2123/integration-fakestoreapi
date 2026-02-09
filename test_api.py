import requests

def test_get_products_returns_200():
    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200
