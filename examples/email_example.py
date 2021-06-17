import RandomUsers as ru

username = ru.Username()
password = ru.Password()
# Create email object with specific prefix "myapp_" and domain name "test.com"
email = ru.Email(length_range=range(10, 11), prefix="myapp_", domain_list=["test.com"])

user_model = ru.User(username=username, password=password, email=email)
user = user_model.generate()
print(f"Email: {user['email']}")
