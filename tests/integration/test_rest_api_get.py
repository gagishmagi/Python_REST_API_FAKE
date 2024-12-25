# import requests
import json

BASE_URL = "http://localhost:5000"

def setup_module(module):
    # Create a db.json file with initial data
    db_data = {
        "posts": [
            {"id": 1, "title": "Post 1", "body": "Content of post 1", "userId": 1},
            {"id": 2, "title": "Post 2", "body": "Content of post 2", "userId": 1}
        ],
        "comments": [],
        "albums": [],
        "photos": [],
        "todos": [],
        "users": [{
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@gmail.com"
        }]
    }
    with open("db.json", "w") as db_file:
        json.dump(db_data, db_file)

def teardown_module(module):
    # Remove the db.json file after tests
    import os
    os.remove("db.json")

def test_get_posts(client):
    response = client.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_post_by_id(client):
    post_id = 1
    response = client.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)
    assert int(response.get_json().get('id')) == post_id

def test_get_nonexistent_post(client):
    post_id = 9999
    response = client.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 404

def test_create_post(client):
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = client.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert isinstance(response.get_json(), dict)
    assert response.get_json().get('title') == new_post['title']

def test_update_post(client):
    post_id = 1
    updated_post = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = client.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)
    assert response.get_json().get('title') == updated_post['title']

def test_delete_post(client):
    post_id = 1
    response = client.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

# def test_get_comments(client):
#     response = client.get(f"{BASE_URL}/comments")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)

# def test_get_comment_by_id(client):
#     comment_id = 1
#     response = client.get(f"{BASE_URL}/comments/{comment_id}")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), dict)
#     assert int(response.get_json().get('id')) == comment_id

# def test_get_nonexistent_comment(client):
#     comment_id = 9999
#     response = client.get(f"{BASE_URL}/comments/{comment_id}")
#     assert response.status_code == 404

# def test_get_albums(client):
#     response = client.get(f"{BASE_URL}/albums")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)

# def test_get_album_by_id(client):
#     album_id = 1
#     response = client.get(f"{BASE_URL}/albums/{album_id}")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), dict)
#     assert int(response.json().get('id')) == album_id

# def test_get_nonexistent_album(client):
#     album_id = 9999
#     response = client.get(f"{BASE_URL}/albums/{album_id}")
#     assert response.status_code == 404

# def test_get_photos(client):
#     response = client.get(f"{BASE_URL}/photos")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)

# def test_get_photo_by_id(client):
#     photo_id = 1
#     response = client.get(f"{BASE_URL}/photos/{photo_id}")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), dict)
#     assert int(response.json().get('id')) == photo_id

# def test_get_nonexistent_photo(client):
#     photo_id = 9999
#     response = client.get(f"{BASE_URL}/photos/{photo_id}")
#     assert response.status_code == 404

# def test_get_todos(client):
#     response = client.get(f"{BASE_URL}/todos")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), list)

# def test_get_todo_by_id(client):
#     todo_id = 1
#     response = client.get(f"{BASE_URL}/todos/{todo_id}")
#     assert response.status_code == 200
#     assert isinstance(response.get_json(), dict)
#     assert int(response.get_json().get('id')) == todo_id

# def test_get_nonexistent_todo(client):
#     todo_id = 9999
#     response = client.get(f"{BASE_URL}/todos/{todo_id}")
#     assert response.status_code == 404

def test_get_users(client):
    response = client.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_user_by_id(client):
    user_id = 1
    response = client.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)
    assert int(response.get_json().get('id')) == user_id

def test_get_nonexistent_user(client):
    user_id = 9999
    response = client.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404
