import abc
import random
from string import ascii_letters, digits
from typing import Callable
from . import data


class Field(abc.ABC):
    @abc.abstractmethod
    def generate(self, *args):
        return NotImplementedError


class Name(Field):
    def __init__(
        self, surname_list: list = data.surname, forename_list: list = data.forename
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
        allow: str = ascii_letters + digits,
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
        domain_list: list = data.email_domain,
    ) -> None:
        self.value = None
        self.length_range = length_range  # does not include the length of prefix
        self.prefix = prefix
        self.allow = allow
        self.domain_list = domain_list

    def generate(self) -> str:
        length = random.choice(self.length_range)
        username = self.prefix + "".join(random.choices(self.allow, k=length))
        self.value = username + "@" + random.choice(self.domain_list)
        return self.value
