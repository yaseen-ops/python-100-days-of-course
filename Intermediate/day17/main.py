class User:
    def __init__(self, userid, username):
        self.id = userid
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("101", "Sachin")
user_2 = User("102", "Dhoni")

user_1.follow(user_2)
print(user_1.id)
print(f"user1 followers {user_1.followers}")
print(f"user1 following {user_1.following}")
print(f"user2 followers {user_2.followers}")
print(f"user2 followers {user_2.following}")