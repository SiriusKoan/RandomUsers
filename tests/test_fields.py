import unittest
import RandomUsers as ru


class NameFieldTest(unittest.TestCase):
    def setUp(self) -> None:
        self.field = ru.Name()

    def test_output_type(self):
        name = self.field.generate()
        self.assertEqual(type(name), tuple)
        self.assertEqual(type(name[0]), str)
        self.assertEqual(type(name[1]), str)

    def test_random(self):
        # Basically, it will not be the same.
        name1 = self.field.generate()
        name2 = self.field.generate()
        self.assertNotEqual(name1, name2)
