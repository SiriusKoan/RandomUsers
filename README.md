# RandomUsers
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/RandomUsers.svg)](https://pypi.python.org/pypi/RandomUsers)
[![PyPi Package Version](https://img.shields.io/pypi/v/RandomUsers.svg)](https://pypi.python.org/pypi/RandomUsers)  
A simple tool helps you generate fake users.
## Installation
```shell
$ pip install RandomUsers
```
## Examples
### Basic
```python
import RandomUsers as ru
# Create username object
username = ru.Username()
# Create password object
password = ru.Password()
# Create email object
email = ru.Email()
# Create user model object
user_model = ru.User(username=username, password=password, email=email)
user = user_model.generate()
print(user)
```
### With more fields
```python
import RandomUsers as ru
name = ru.Name()
username = ru.Username()
# "@", "#" and "$" must be in the password
password = ru.Password(length_range=range(20,25), must="@#$")
birth = ru.Birth(birth_year_range=range(2000, 2011))
user_model = ru.User(name=name, username=username, password=password, birth=birth)
user = user_model.generate()
print(user)
```
