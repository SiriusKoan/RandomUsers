import RandomUsers as ru

username = ru.Username()
birthinfo = ru.BirthInfo(date_format="%Y-%m-%d")
user_model = ru.BasicModel(username=username, birthinfo=birthinfo)
user = user_model.generate()
print(f"Birthday: {user['birthinfo'][0]}")
print(f"Age: {user['birthinfo'][1]}")
