class Classroom:
    def __init__(self, name):
        self.name = name
        self.student = []
        self.subject = []

    def add_student(self, student):
        roll_no = f"{self.name}-{len(self.student)+1}"
        student.id = roll_no
        self.student.append(student)

    def add_subject(self, subject):
        self.subject.append(subject)

    def take_semester_final_exm(self):
        for subject in self.subject:
            subject.exm(self.student)
        for student in self.student:
            student.final_grade()
