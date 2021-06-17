from string import ascii_letters, digits
import hashlib
import RandomUsers as ru


def sha(s):
    f = hashlib.sha256(s.encode("utf-8"))
    return f.hexdigest()


username = ru.Username()
password = ru.Password(allow=ascii_letters + digits, must="$", hash=sha)
user_model = ru.UserModel(username=username, password=password)
user = user_model.generate()
print(user)
