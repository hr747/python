<<<<<<< HEAD
class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, student):
        self.student_list.append(student)


class student:
    def __init__(self, name, roll, deperment):
        self.name = name
        self.roll = roll
        self.deperment = deperment
        self.is_enroll = True
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enroll:
            print(f'student is already  enroll ')
        else:
            self.is_enroll = True
            print(f'student enroll successfull')

    def drop_student(self):
        if not self.is_enroll:
            print(f'student not found')
        else:
            self.is_enroll = False
            print(f'student drop successfull')

    def view_student_info(self):
        print(f'Name : {self.name}')
        print(f'Roll : {self.roll}')
        print(f'Deperment : {self.deperment}')
        print(f'Enroll : {self.is_enroll}')


s1 = student("Riad", 101, "CSE")

s2 = student("Raha", 102, "EEE")

s3 = student("Mahi", 103, "BBA")

s4 = student("Romon", 104, "CSE")

s5 = student("Soron", 105, "BBA")
while 0<1:

    print("\n1. View All Students")

    print("\n2. Enroll student")

    print("\n3. Drop student")

    print("\n4. Exit")

    choice = input()
    if choice == '1':
        for student in StudentDatabase.student_list:
            student.view_student_info()
    elif choice == '2':
        sid = input(f'input roll')
        found = False
        for s in StudentDatabase.student_list:
            if str(s.roll) == sid:
                s.enroll_student()
                found = True

                break
        if not found:
                        name = input('Enter name: ')
                        roll = int(sid)
                        department = input('Enter department: ')
        
                        student(name, roll, department)
                        print('Student added successfully!')   

    elif choice == '3':
        sid = input(f'input roll')
        found = False

        for student in StudentDatabase.student_list:
            if str(student.roll) == sid:
                student.drop_student()

                found = True

                break

        if not found:
            print("Invalid Student ID!")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
=======
class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, student):
        self.student_list.append(student)


class student:
    def __init__(self, name, roll, deperment):
        self.name = name
        self.roll = roll
        self.deperment = deperment
        self.is_enroll = True
        StudentDatabase.add_student(self)

    def enroll_student(self):
        if self.is_enroll:
            print(f'student is already  enroll ')
        else:
            self.is_enroll = True
            print(f'student enroll successfull')

    def drop_student(self):
        if not self.is_enroll:
            print(f'student not found')
        else:
            self.is_enroll = False
            print(f'student drop successfull')

    def view_student_info(self):
        print(f'Name : {self.name}')
        print(f'Roll : {self.roll}')
        print(f'Deperment : {self.deperment}')
        print(f'Enroll : {self.is_enroll}')


s1 = student("Riad", 101, "CSE")

s2 = student("Raha", 102, "EEE")

s3 = student("Mahi", 103, "BBA")

s4 = student("Romon", 104, "CSE")

s5 = student("Soron", 105, "BBA")
while 0<1:

    print("\n1. View All Students")

    print("\n2. Enroll student")

    print("\n3. Drop student")

    print("\n4. Exit")

    choice = input()
    if choice == '1':
        for student in StudentDatabase.student_list:
            student.view_student_info()
    elif choice == '2':
        sid = input(f'input roll')
        found = False
        for s in StudentDatabase.student_list:
            if str(s.roll) == sid:
                s.enroll_student()
                found = True

                break
        if not found:
                        name = input('Enter name: ')
                        roll = int(sid)
                        department = input('Enter department: ')
        
                        student(name, roll, department)
                        print('Student added successfully!')   

    elif choice == '3':
        sid = input(f'input roll')
        found = False

        for student in StudentDatabase.student_list:
            if str(student.roll) == sid:
                student.drop_student()

                found = True

                break

        if not found:
            print("Invalid Student ID!")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
>>>>>>> 358d5db7b7990c492baf93d7105f46166eab48fd
