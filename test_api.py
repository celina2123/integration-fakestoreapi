import requests

def test_get_products_returns_200():
    url = "https://fakestoreapi.com/products"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
