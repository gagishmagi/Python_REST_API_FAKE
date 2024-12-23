from flask import Flask, Response, jsonify, request
import json
import sys
import os


app = Flask(__name__)


@app.get('/')
def home_page():
    return "<h1>Welcome Home page</h1>"

# @app.route('/posts', methods=["GET"])


@app.get('/posts')
def get_all_posts():
    db_file_path = "db.json"
    with open(db_file_path) as db:
        db_data = json.load(db)
        return jsonify(db_data["posts"])


@app.get('/posts/<id>')
def get_one_post(id):

    db_file_path = "db.json"
    with open(db_file_path) as db:
        db_data = json.load(db)

    def find_by_id(post):
        return post["id"] == int(id)

    try:
        db_data_filtered = list(filter(find_by_id, db_data["posts"]))
        post = db_data_filtered[0]

        return jsonify(post)
    except IndexError:
        return {"status": "error", "message": "Post not found", "status_code": 404}, 404


@app.post('/posts')
def create_single_post():
    post = request.get_json()

    if not post:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_file_path = "db.json"
    with open(db_file_path, "r+") as db:
        db_data = json.load(db)
        new_id = max(post["id"] for post in db_data["posts"]) + 1
        post["id"] = new_id
        db_data["posts"].append(post)
        db.seek(0)
        json.dump(db_data, db, indent=4)
        db.truncate()

    # response = Response(
    #     response=json.dumps({
    #         "id": int(id),
    #         "title": "post 1",
    #         "body": "body of post 1",
    #         "userId": 1
    #     }),
    #     status=200,
    #     mimetype='application/json'
    # )

    return jsonify(post), 201


@app.put('/posts/<id>')
def update_post(id):
    updated_post = request.get_json()

    if not updated_post:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_file_path = "db.json"
    with open(db_file_path, "r+") as db:
        db_data = json.load(db)
        for post in db_data["posts"]:
            if post["id"] == int(id):
                post.update(updated_post)
                db.seek(0)
                json.dump(db_data, db, indent=4)
                db.truncate()
                return jsonify(post), 200

    return {"status": "error", "message": "Post not found"}, 404


@app.patch('/posts/<id>')
def partially_update_post(id):
    updated_fields = request.get_json()

    if not updated_fields:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_file_path = "db.json"
    with open(db_file_path, "r+") as db:
        db_data = json.load(db)
        for post in db_data["posts"]:
            if post["id"] == int(id):
                post.update(updated_fields)
                db.seek(0)
                json.dump(db_data, db, indent=4)
                db.truncate()
                return jsonify(post), 200

    return {"status": "error", "message": "Post not found"}, 404


@app.delete('/posts/<id>')
def delete_post(id):
    db_file_path = "db.json"
    with open(db_file_path, "r+") as db:
        db_data = json.load(db)
        db_data["posts"] = [
            post for post in db_data["posts"] if post["id"] != int(id)]
        db.seek(0)
        json.dump(db_data, db, indent=4)
        db.truncate()

    return {"status": "success", "message": "Post deleted"}, 200


print(f"Running json Server on port { os.getenv('PORT')}")
