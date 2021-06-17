import random
import csv
import RandomUsers as ru


class StudentID(ru.Field):
    def __init__(self, id_range: range = range(1000, 10000)) -> None:
        self.value = None
        self.id_range = id_range

    def generate(self):
        self.value = random.choice(self.id_range)
        return self.value


class Grade(ru.Field):
    def __init__(self, grade_range: range = range(1, 10)) -> None:
        self.value = None
        self.grade_range = grade_range

    def generate(self):
        self.value = random.choice(self.grade_range)
        return self.value


class StudentModel(ru.Person):
    def __init__(
        self, name=None, student_id=None, grade=None, phone_number=None
    ) -> None:
        self.info = dict()
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.phone_number = phone_number

    def get_available(self):
        return ["name", "student_id", "grade", "phone_number"]

    def generate(self):
        self.info = dict()
        surname, forename = self.name.generate()
        self.info["name"] = " ".join([surname, forename])
        self.info["student_id"] = self.student_id.generate()
        self.info["grade"] = self.grade.generate()
        self.info["phone_number"] = self.phone_number.generate()
        return self.info

    def bulk_generate(self, n=100, csv_file=False):
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


name = ru.Name()
student_id = StudentID()
grade = Grade()
phone_number = ru.PhoneNumber()

student_model = StudentModel(name, student_id, grade, phone_number)
student = student_model.generate()
print(student)
students = student_model.bulk_generate(csv_file="students.csv")
