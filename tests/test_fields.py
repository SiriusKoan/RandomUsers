import unittest
import hashlib
from string import ascii_letters, digits
import random
import RandomUsers as ru


class ModelField(ru.Field):
    def generate(self):
        return random.randint(1, 100)


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

    def test_output_type(self):
        name = self.field.generate()
        self.assertEqual(type(name), tuple)
        self.assertEqual(type(name[0]), str)
        self.assertEqual(type(name[1]), str)


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
