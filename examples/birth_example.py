import RandomUsers as ru

username = ru.Username()
birth = ru.Birth(date_format="%Y-%m-%d")
user_model = ru.User(username=username, birth=birth)
user = user_model.generate()
print(f"Birthday: {user['birthday']}")
print(f"Age: {user['age']}")
