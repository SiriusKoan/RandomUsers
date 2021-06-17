import RandomUsers as ru

username = ru.Username()
password = ru.Password()

# use built-in user object
user_model = ru.BasicModel(username=username, password=password, instance=ru.Instance)
user = user_model.generate()
print(f"Username: {user.username}")
print(f"Password: {user.password}")
