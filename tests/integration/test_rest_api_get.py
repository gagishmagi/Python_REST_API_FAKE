import requests
import json

BASE_URL = "http://localhost:5000"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    # print(type(response.text))
    # print(json.loads(response.text))
    # print(response.json())
    assert isinstance(response.json(), list)

def test_get_post_by_id():
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert int(response.json().get('id')) == post_id

def test_get_nonexistent_post():
    post_id = 9999
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 404
