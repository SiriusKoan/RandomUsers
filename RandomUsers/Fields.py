import abc
import random
import datetime
from string import ascii_letters, digits, punctuation
from typing import Callable
from . import data


class Field(abc.ABC):
    """
    Basic field, and it can be used for adding another field.
    """

    @abc.abstractmethod
    def generate(self):
        return NotImplementedError


class Name(Field):
    def __init__(
        self,
        surname_list: list[str] = data.surname,
        forename_list: list[str] = data.forename,
    ) -> None:
        """
        :param surname_list: list of surnames
        :param forename_list: list of forenames
        """
        self.surname = None
        self.forename = None
        self.surname_list = surname_list
        self.forename_list = forename_list

    def generate(self) -> tuple[str, str]:
        """
        Generate random names from specific or default list.

        :return: <tuple[str, str]>. The first string is surname and the second string is forename.
        """
        self.surname = random.choice(self.surname_list)
        self.forename = random.choice(self.forename_list)
        return (self.surname, self.forename)


class Username(Field):
    def __init__(
        self, length_range: range = range(5, 15), allow: str = ascii_letters + digits
    ) -> None:
        """
        :param length_range: the range of the username's length. Notice the last number will not in the range
        :param allow: allowed characters
        """
        self.value = None
        self.length_range = length_range
        self.allow = allow

    def generate(self) -> str:
        """
        Generate random username.

        :return: <str>
        """
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
        """
        :param length_range: the range of the password's length. Notice the last number will not in the range
        :param allow: allowed characters
        :param must: the characters must in the password
        :param hash: a hash function, or use None to generate unhashed password
        """
        self.value = None
        self.length_range = length_range
        self.allow = allow
        self.must = must
        self.hash = hash

    def generate(self) -> str:
        """
        Generate random password.

        :return: <str>
        """
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
        """
        :param length_range: the range of the email's length, but does not include the length of prefix. Notice the last number will not in the range
        :param prefix: the prefix of every email
        :param allow: allowed characters
        :param domain_list: the domain name list
        """
        self.value = None
        self.length_range = length_range
        self.prefix = prefix
        self.allow = allow
        self.domain_list = domain_list

    def generate(self) -> str:
        """
        Generate email address.

        :return: <str>
        """
        length = random.choice(self.length_range)
        username = self.prefix + "".join(random.choices(self.allow, k=length))
        self.value = "@".join([username, random.choice(self.domain_list)])
        return self.value


class Birthday(Field):
    def __init__(
        self, birth_year_range: range = range(1920, 2001), date_format: str = "%Y/%m/%d"
    ) -> None:
        """
        :param birth_year_range: the range of birth year. Notice the last number will not in the range
        :param date_format: the date format for output birthday.
                            It should be recognizable for python time module to parse it.
                            If the date format is not recognizable, the module will raise a ValueError.
        """
        self.birthday = None
        self.birth_year_range = birth_year_range
        self.date_format = date_format

    def generate(self) -> tuple[str, int]:
        """
        Generate random birthday within the given range.

        :return <str>
        """
        start = datetime.date(self.birth_year_range[0], 1, 1)
        end = datetime.date(self.birth_year_range[-1], 12, 31)
        date = start + (end - start) * random.random()
        self.birthday = date.strftime(self.date_format)
        return self.birthday


class Age(Field):
    def __init__(self, birthday: str = None, date_format: str = "%Y/%m/%d") -> None:
        """
        :param birthday: birthday in specific format
        :param date_format: the date format for output birthday.
                            It should be recognizable for python time module to parse it.
                            If the date format is not recognizable, the module will raise a ValueError.
        """
        self.value = None
        self.date_format = date_format
        if birthday:
            self.birthday = datetime.datetime.strptime(birthday, self.date_format)
            self.birthday = self.birthday.date()
        else:
            start = datetime.date(1920, 1, 1)
            end = datetime.date(2001, 12, 31)
            self.birthday = start + (end - start) * random.random()

    def generate(self):
        """
        Generate age from given birthday or random date if the birthday value is not specified.

        :return value: <int>
        """
        timedelta = datetime.date.today() - self.birthday
        self.value = int(timedelta.days / 365.2425)
        return self.value


class Gender(Field):
    def __init__(self, gender_list: list[str] = data.gender) -> None:
        """
        :param gender_list: the gender list
        """
        self.value = None
        self.gender_list = gender_list

    def generate(self) -> str:
        """
        Choose a gender in given gender list.

        :return value: <str>
        """
        self.value = random.choice(self.gender_list)
        return self.value


class PhoneNumber(Field):
    def __init__(self, format: str = "+886 9iiiiiiii", allow: str = digits) -> None:
        """
        :param format: the format of phone number. You should use "i" for random part, and numbers for static part.
        :param allow: allowed characters
        """
        self.value = None
        self.format = list(format)
        self.allow = allow

    def generate(self) -> str:
        """
        Generate random phone number.

        :return: <str>
        """
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
        """
        :param location_list: location list
        """
        self.value = None
        self.location_list = location_list
        self.timezone_range = timezone_range

    def generate(self) -> tuple[str, str]:
        """
        Generate random location.

        :return: <str>
        """
        self.value = random.choice(self.location_list)
        return self.value


class Timezone(Field):
    def __init__(self, timezone_range: range = range(-24, 25)) -> None:
        """
        :param timezone_range: the range of timezone
        """
        self.value = None
        self.timezone_range = timezone_range

    def generate(self):
        """
        Generate random timezone.

        :return: <str>
        """
        self.value = "%+d" % (random.choice(self.timezone_range))
        return self.value
