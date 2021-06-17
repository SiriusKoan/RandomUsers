from string import ascii_letters, digits
import RandomUsers as ru

username = ru.Username()
password = ru.Password(allow=ascii_letters + digits)

user_model = ru.UserModel(username=username, password=password)
users = user_model.bulk_generate(n=100, csv_file="test.csv")
