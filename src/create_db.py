import json
from faker import Faker

fake = Faker()

def generate_fake_data(num_users=10, num_posts=100, num_comments=500, num_albums=100, num_photos=500, num_todos=200):
    data = {
        "users": [],
        "posts": [],
        "comments": [],
        "albums": [],
        "photos": [],
        "todos": []
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

    for i in range(1, num_albums + 1):
        album = {
            "id": i,
            "userId": fake.random_element(elements=data["users"])["id"],
            "title": fake.sentence(nb_words=3)
        }
        data["albums"].append(album)

    for i in range(1, num_photos + 1):
        photo = {
            "id": i,
            "albumId": fake.random_element(elements=data["albums"])["id"],
            "title": fake.sentence(nb_words=3),
            "url": fake.image_url(),
            "thumbnailUrl": fake.image_url()
        }
        data["photos"].append(photo)

    for i in range(1, num_todos + 1):
        todo = {
            "id": i,
            "userId": fake.random_element(elements=data["users"])["id"],
            "title": fake.sentence(nb_words=3),
            "completed": fake.boolean()
        }
        data["todos"].append(todo)

    return data

if __name__ == "__main__":
    fake_data = generate_fake_data()
    with open('db.json', 'w') as f:
        json.dump(fake_data, f, indent=4)
