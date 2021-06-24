from string import ascii_letters, digits
import RandomUsers as ru

username = ru.Username()
password = ru.Password(allow=ascii_letters + digits)

user_model = ru.BasicModel(username=username, password=password)
users = user_model.ordered_generate(ordered_fields={"username": "num_"}, csv_file="test.csv")
