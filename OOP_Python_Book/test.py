class Student:
    def __init__(self, name):
        self._name = name
        self._grade = None

    @property
    def grade(self):
        return self._grade
    
    def change_grade(self, grade):
        self.grade = grade

priya = Student('Priya')
priya.change_grade('A')
print(priya.grade)            # A