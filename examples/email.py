from string import ascii_letters
import RandomUsers as ru

username = ru.Username(allow=ascii_letters)
password = ru.Password(length_range=range(13,25))
# Create email object with specific prefix and domain name
email = ru.Email(length_range=range(10,11), prefix="myapp_", domain_list=["test.com"])

user_model = ru.User(username=username, password=password, email=email)
user = user_model.generate()
print(user.email)
