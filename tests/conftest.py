# from flask import current_app as app
import pytest
import sys
import os
import json

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

print(f"sys.path: {sys.path}")

from src.app import app


# from src.create_db import generate_fake_data

# @pytest.fixture(scope='module', autouse=True)
# def setup_db():
#     db_file_path = 'db.json'
#     initial_data = generate_fake_data()

#     with open(db_file_path, 'w') as db:
#         json.dump(initial_data, db, indent=4)
#     yield
#     os.remove(db_file_path)

# @pytest.fixture
# def db_file():
#     db_file_path = os.path.join(
#         os.path.dirname(__file__), '..', 'src', 'db.json')
#     with open(db_file_path, 'r') as db:
#         data = json.load(db)
#     return data


@pytest.fixture
def client():
    with app.app_context(): 
        app.config.update({
            "TESTING": True
        })
        yield app.test_client()

    # with app.app_context():
    #     app.config['TESTING'] = True
    #     with app.test_client() as client:
    #         yield client
