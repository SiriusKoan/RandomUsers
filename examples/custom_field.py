import random
import string
import RandomUsers as ru


class Score(ru.Field):
    def __init__(self, score_range: range = range(0, 101)) -> None:
        self.value = None
        self.score_range = score_range

    def generate(self):
        self.value = random.choice(self.score_range)
        return self.value

name = ru.Name()
email = ru.Email(allow=string.digits, domain_list=["coolschool.edu"])
score = Score()
student_model = ru.BasicModel(name=name, email=email, score=score)
student = student_model.generate()
print(student)
