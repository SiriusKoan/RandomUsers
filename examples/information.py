import RandomUsers as ru

username = ru.Username()
password = ru.Password()
email = ru.Email()

# normal user
user_model = ru.BasicModel(username=username, password=password, email=email)
user = user_model.generate()
print(user)
# admin
admin_model = ru.BasicModel(
    username=username, password=password, email=email, information={"is_admin": True}
)
admin = admin_model.generate()
print(admin)
