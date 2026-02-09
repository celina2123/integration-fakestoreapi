import requests

def test_get_products_returns_200():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get("https://fakestoreapi.com/products", headers=headers)
    assert response.status_code == 200
