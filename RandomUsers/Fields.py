import abc
import random
import datetime
from string import ascii_letters, digits, punctuation
from time import time
from typing import Callable
from . import data


class Field(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        return NotImplementedError


class Name(Field):
    def __init__(
        self,
        surname_list: list[str] = data.surname,
        forename_list: list[str] = data.forename,
    ) -> None:
        self.surname_list = surname_list
        self.forename_list = forename_list

    def generate(self) -> tuple[str, str]:
        self.surname = random.choice(self.surname_list)
        self.forename = random.choice(self.forename_list)
        return (self.surname, self.forename)


class Username(Field):
    def __init__(
        self, length_range: range = range(5, 15), allow: str = ascii_letters + digits
    ) -> None:
        self.value = None
        self.length_range = length_range
        self.allow = allow

    def generate(self) -> str:
        length = random.choice(self.length_range)
        self.value = "".join(random.choices(self.allow, k=length))
        return self.value


class Password(Field):
    def __init__(
        self,
        length_range: range = range(10, 20),
        allow: str = ascii_letters + digits + punctuation,
        must: str = "",
        hash: Callable = None,
    ) -> None:
        self.value = None
        self.length_range = length_range
        self.allow = allow
        self.must = must
        self.hash = hash

    def generate(self) -> str:
        length = max(random.choice(self.length_range), len(self.must))
        length_not_for_must = length - len(self.must)
        self.value = random.choices(self.allow, k=length_not_for_must) + list(self.must)
        random.shuffle(self.value)
        self.value = "".join(self.value)
        if self.hash:
            return self.hash(self.value)
        else:
            return self.value


class Email(Field):
    def __init__(
        self,
        length_range: range = range(5, 15),
        prefix: str = "test_",
        allow: str = ascii_letters + digits,
        domain_list: list[str] = data.email_domain,
    ) -> None:
        self.value = None
        self.length_range = length_range  # does not include the length of prefix
        self.prefix = prefix
        self.allow = allow
        self.domain_list = domain_list

    def generate(self) -> str:
        length = random.choice(self.length_range)
        username = self.prefix + "".join(random.choices(self.allow, k=length))
        self.value = "@".join([username, random.choice(self.domain_list)])
        return self.value


class Birth(Field):
    def __init__(
        self, birth_year_range: range = range(1920, 2001), date_format: str = "%Y/%m/%d"
    ) -> None:
        self.birthday = None
        self.age = None
        self.birth_year_range = birth_year_range
        self.date_format = date_format

    def generate(self) -> tuple[str, int]:
        start = datetime.date(self.birth_year_range[0], 1, 1)
        end = datetime.date(self.birth_year_range[-1], 12, 31)
        date = start + (end - start) * random.random()
        self.birthday = date.strftime(self.date_format)
        timedelta = datetime.date.today() - date
        self.age = int(timedelta.days / 365.2425)
        return (self.birthday, self.age)


class Gender(Field):
    def __init__(self, gender_list: list[str] = data.gender) -> None:
        self.value = None
        self.gender_list = gender_list

    def generate(self) -> str:
        self.value = random.choice(self.gender_list)
        return self.value


class PhoneNumber(Field):
    def __init__(self, format: str = "+886 9iiiiiiii", allow: str = digits) -> None:
        self.value = None
        self.format = list(format)
        self.allow = allow

    def generate(self) -> str:
        self.value = self.format
        for i in range(len(self.value)):
            if self.value[i] == "i":
                self.value[i] = random.choice(self.allow)
        self.value = "".join(self.value)
        return self.value


class Location(Field):
    def __init__(
        self,
        location_list: list[str] = data.location,
        timezone_range: range = range(-24, 25),
    ) -> None:
        self.location = None
        self.timezone = None  # timezone doesn't comply to the location
        self.location_list = location_list
        self.timezone_range = timezone_range

    def generate(self) -> tuple[str, str]:
        self.location = random.choice(self.location_list)
        self.timezone = "%+d" % (random.choice(self.timezone_range))
        return (self.location, self.timezone)
