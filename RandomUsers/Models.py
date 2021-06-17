import abc
import csv
from .Exceptions import CsvAndInstanceError


class Person(abc.ABC):
    """
    Basic person class.
    """

    @abc.abstractmethod
    def generate(self, csv):
        return NotImplementedError

    @abc.abstractmethod
    def bulk_generate(self, n, csv):
        return NotImplementedError


class UserInstance:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)


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
        information: dict() = None,
        instance=None,
        **kwargs,
    ) -> None:
        """
        :param name: Name object
        :param username: Username object
        :param password: Password object
        :param email: Email object
        :param birth: Birth object
        :param gender: Gender object
        :param phone_number: PhoneNumber object
        :param location: Location object
        :param information: other user information, such as `{"is_admin": True}`
        :param kwargs: other customized fields
        """
        self.info = dict()
        self.instance = instance
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

    def get_available(self) -> list:
        """
        Return all available fields of the user model.

        :return: <list>
        """
        return [key for key in list({**self.fields, **self.extra}.keys())]

    def generate(self):
        """
        Generate random user object.
        You can access to the user data by using its attributes.
        """
        self.info = dict()
        for key, field in self.fields.items():
            if key == "name":
                self.info["surname"], self.info["forename"] = field.generate()
            elif key == "birth":
                self.info["birthday"], self.info["age"] = field.generate()
            elif key == "location":
                self.info["location"], self.info["timezone"] = field.generate()
            else:
                self.info[key] = field.generate()
        for key, field in self.extra.items():
            self.info[key] = field.generate()
        if self.information:
            for key, value in self.information.items():
                self.info[key] = value
        if self.instance:
            return self.instance(**self.info)
        else:
            return self.info

    def bulk_generate(self, n=100, csv_file=False):
        """
        Generate as many random users as you want.
        """
        if csv_file and self.instance:
            raise CsvAndInstanceError
        users = []
        for _ in range(n):
            users.append(self.generate())
        if csv_file:
            with open(csv_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.get_available())
                for user in users:
                    writer.writerow(list(user.values()))
        return users