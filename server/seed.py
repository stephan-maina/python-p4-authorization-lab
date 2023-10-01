from app import db, User

def seed_database():
    db.create_all()

    # Create a test user with username "Stephorinho $9" and password "password123"
    user1 = User(username="Stephorinho $9")
    user1.set_password("password123")

    # Create another test user with username "Darwin Nunez" and password "secret456"
    user2 = User(username="Darwin Nunez")
    user2.set_password("secret456")

    db.session.add_all([user1, user2])
    db.session.commit()

if __name__ == "__main__":
    seed_database()
