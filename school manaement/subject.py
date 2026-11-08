from preson import Teacher
from school import School


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_mark = 100
        self.pass_marks = 33

    def exm(self, student):
        for student in student:
            mark = self.teacher.evaluate_exm()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)
