import unittest
import hashlib
import datetime
from string import ascii_letters, digits
import random
import RandomUsers as ru


class ModelField(ru.Field):
    def generate(self):
        return random.randint(1, 10000)


class FieldTestModel(unittest.TestCase):
    def setUp(self) -> None:
        self.field = ModelField()
        self.type = int

    def test_output_type(self):
        self.assertEqual(type(self.field.generate()), self.type)

    def test_random(self):
        # Basically, it will not be the same.
        value1 = self.field.generate()
        value2 = self.field.generate()
        self.assertNotEqual(value1, value2)


class NameFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Name()
        self.type = tuple


class UsernameFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Username()
        self.type = str

    def test_length_range(self):
        username = self.field.generate()
        self.assertIn(len(username), self.field.length_range)

    def test_allow(self):
        username = self.field.generate()
        self.assertNotIn("$", username)


class PasswordFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Password(allow=ascii_letters + digits, must="%")
        self.hash_field = ru.Password(
            allow=ascii_letters + digits, must="%", hash=self.hash_function
        )
        self.type = str

    @staticmethod
    def hash_function(s):
        return hashlib.sha256(s.encode("utf-8")).hexdigest()

    def test_length_range(self):
        password = self.field.generate()
        self.assertIn(len(password), self.field.length_range)

    def test_allow(self):
        password = self.field.generate()
        self.assertNotIn("$", password)

    def test_must(self):
        password = self.field.generate()
        self.assertIn("%", password)

    def test_hash(self):
        password = self.hash_field.generate()
        self.assertEqual(len(password), 64)


class EmailFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Email()
        self.type = str

    def test_length_range(self):
        email = self.field.generate()
        email = email.split("@")[0]
        email = email.lstrip(self.field.prefix)
        self.assertIn(len(email), self.field.length_range)

    def test_prefix(self):
        email = self.field.generate()
        self.assertTrue(email.startswith(self.field.prefix))

    def test_allow(self):
        email = self.field.generate()
        self.assertNotIn("$", email)


class BirthInfoFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.BirthInfo()
        self.type = tuple

    def test_birth_year_range(self):
        birthday = self.field.generate()[0]
        year = datetime.datetime.strptime(birthday, self.field.date_format).year
        self.assertIn(year, self.field.birth_year_range)


class GenderFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Gender()
        self.type = str

    def test_random(self):
        # it is very likely that the two values are the same.
        pass


class PhoneNumberFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.PhoneNumber()
        self.type = str

    def test_format(self):
        phone_number = self.field.generate()
        self.assertTrue(
            phone_number.startswith("".join(self.field.format).replace("i", ""))
        )

    def test_allow(self):
        phone_number = self.field.generate()
        self.assertNotIn("$", phone_number)


class LocationFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Location()
        self.type = str


class TimezoneFieldTest(FieldTestModel):
    def setUp(self) -> None:
        self.field = ru.Timezone()
        self.type = str
