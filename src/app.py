from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

def get_db_data():
    db_file_path = "db.json"
    with open(db_file_path) as db:
        return json.load(db)

def save_db_data(db_data):
    db_file_path = "db.json"
    with open(db_file_path, "w") as db:
        json.dump(db_data, db, indent=4)

@app.get('/')
def home_page():
    return "<h1>Welcome Home page</h1>"

@app.get('/<resource>')
def get_all(resource):
    db_data = get_db_data()
    if resource in db_data:
        return jsonify(db_data[resource])
    return {"status": "error", "message": "Resource not found"}, 404

@app.get('/<resource>/<int:id>')
def get_one(resource, id):
    db_data = get_db_data()
    if resource in db_data:
        items = db_data[resource]
        item = next((item for item in items if item["id"] == id), None)
        if item:
            return jsonify(item)
        return {"status": "error", "message": "Item not found"}, 404
    return {"status": "error", "message": "Resource not found"}, 404

@app.post('/<resource>')
def create(resource):
    item = request.get_json()
    if not item:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_data = get_db_data()
    if resource not in db_data:
        db_data[resource] = []

    new_id = max((item["id"] for item in db_data[resource]), default=0) + 1
    item["id"] = new_id
    db_data[resource].append(item)
    save_db_data(db_data)
    return jsonify(item), 201

@app.put('/<resource>/<int:id>')
def update(resource, id):
    updated_item = request.get_json()
    if not updated_item:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_data = get_db_data()
    if resource in db_data:
        items = db_data[resource]
        for item in items:
            if item["id"] == id:
                item.update(updated_item)
                save_db_data(db_data)
                return jsonify(item), 200
        return {"status": "error", "message": "Item not found"}, 404
    return {"status": "error", "message": "Resource not found"}, 404

@app.patch('/<resource>/<int:id>')
def partially_update(resource, id):
    updated_fields = request.get_json()
    if not updated_fields:
        return {"status": "error", "message": "Invalid payload"}, 400

    db_data = get_db_data()
    if resource in db_data:
        items = db_data[resource]
        for item in items:
            if item["id"] == id:
                item.update(updated_fields)
                save_db_data(db_data)
                return jsonify(item), 200
        return {"status": "error", "message": "Item not found"}, 404
    return {"status": "error", "message": "Resource not found"}, 404

@app.delete('/<resource>/<int:id>')
def delete(resource, id):
    db_data = get_db_data()
    if resource in db_data:
        items = db_data[resource]
        db_data[resource] = [item for item in items if item["id"] != id]
        save_db_data(db_data)
        return {"status": "success", "message": "Item deleted"}, 200
    return {"status": "error", "message": "Resource not found"}, 404

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
