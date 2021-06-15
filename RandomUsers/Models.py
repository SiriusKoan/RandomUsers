import abc
import csv


class Person(abc.ABC):
    @abc.abstractmethod
    def generate(self, csv):
        return NotImplementedError

    @abc.abstractmethod
    def bulk_generate(self, n, csv):
        return NotImplementedError


class UserInstance:
    def __init__(self) -> None:
        pass


class User(Person):
    def __init__(
        self,
        name=None,
        username=None,
        password=None,
        email=None,
        birth=None,
        gender=None,
        phone_number=None,
        location=None,
        information=None,
        **kwargs,
    ) -> None:
        self.information = information
        self.extra = kwargs
        self.fields = dict()
        if name:
            self.fields["name"] = name
        if username:
            self.fields["username"] = username
        if password:
            self.fields["password"] = password
        if email:
            self.fields["email"] = email
        if birth:
            self.fields["birth"] = birth
        if gender:
            self.fields["gender"] = gender
        if phone_number:
            self.fields["phone_number"] = phone_number
        if location:
            self.fields["location"] = location

    def get_available(self):
        return [key for key in list({self.fields, self.extra}.keys())]

    def generate(self):
        user = UserInstance()
        for key, field in self.fields.items():
            if key == "name":
                user.surname, user.forename = field.generate()
            elif key == "birth":
                user.birthday, user.age = field.generate()
            elif key == "location":
                user.location, user.timezone = field.generate()
            else:
                setattr(user, key, field.generate())
        for key, field in self.extra.items():
            setattr(user, key, field.generate())
        for key, value in self.information.items():
            setattr(user, key, value)
        return user

    def bulk_generate(self, n=100):
        users = []
        for _ in range(n):
            users.append(self.generate())
        return users
