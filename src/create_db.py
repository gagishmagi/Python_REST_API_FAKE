import json
from faker import Faker

fake = Faker()

def generate_fake_data(num_users=10, num_posts=100, num_comments=500):
    data = {
        "users": [],
        "posts": [],
        "comments": []
    }

    for i in range(1, num_users + 1):
        user = {
            "id": i,
            "name": fake.name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "address": {
                "street": fake.street_address(),
                "suite": fake.secondary_address(),
                "city": fake.city(),
                "zipcode": fake.zipcode(),
                "geo": {
                    "lat": float(fake.latitude()),
                    "lng": float(fake.longitude())
                }
            },
            "phone": fake.phone_number(),
            "website": fake.domain_name(),
            "company": {
                "name": fake.company(),
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        }
        data["users"].append(user)

    for i in range(1, num_posts + 1):
        post = {
            "id": i,
            "userId": fake.random_element(elements=data["users"])["id"],
            "title": fake.sentence(nb_words=6),
            "body": fake.paragraph(nb_sentences=3)
        }
        data["posts"].append(post)

    for i in range(1, num_comments + 1):
        comment = {
            "id": i,
            "postId": fake.random_element(elements=data["posts"])["id"],
            "name": fake.name(),
            "email": fake.email(),
            "body": fake.paragraph(nb_sentences=2)
        }
        data["comments"].append(comment)

    return data

if __name__ == "__main__":
    fake_data = generate_fake_data()
    with open('db.json', 'w') as f:
        json.dump(fake_data, f, indent=4)
