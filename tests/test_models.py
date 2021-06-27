import unittest
import os
import RandomUsers as ru


class BasicModelTest(unittest.TestCase):
    def setUp(self) -> None:
        self.username = ru.Username()
        self.password = ru.Password()
        self.model = ru.BasicModel(
            username=self.username,
            password=self.password,
            information={"is_admin": True},
        )

    def tearDown(self) -> None:
        try:
            os.remove("test.csv")
        except FileNotFoundError:
            pass

    def test_generate(self):
        self.assertEqual(type(self.model.generate()), dict)

    def test_information(self):
        user = self.model.generate()
        self.assertEqual(user["is_admin"], True)

    def test_instance(self):
        self.model.instance = ru.Instance
        user = self.model.generate()
        # reset
        self.model.instance = None
        self.assertEqual(type(user), ru.Instance)

    def test_get_available(self):
        self.assertEqual(self.model.get_available(), ["username", "password"])

    def test_bulk_generate(self):
        users = self.model.bulk_generate()
        self.assertEqual(len(users), 100)
        self.assertEqual(type(users[0]), dict)

    def test_csv_instance_error(self):
        try:
            self.model.instance = ru.Instance
            users = self.model.bulk_generate(csv_file="test.csv")
        except Exception as e:
            self.assertIsInstance(e, ru.CsvAndInstanceError)
        finally:
            self.model.instance = None

    def test_write_csv(self):
        users = self.model.bulk_generate(csv_file="test.csv")
        self.assertIn("test.csv", os.listdir())

    def test_ordered_generate(self):
        users = self.model.ordered_generate(ordered_fields={"username": "num_"})
        for i in range(1, 101):
            self.assertTrue(users[i - 1]["username"].startswith("num_%d" % i))
