from school import School
from preson import Student,Teacher
from subject import Subject
from classroom import Classroom

school =School("ABC","Dhaka")
# adding classroom
eight= Classroom("Eight")
nine=Classroom("NIne")
ten=Classroom("Ten")
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)
# adding clasroom
rahim=Student("Rahim",eight)
fahim=Student("Fahim",nine)
raha=Student("Raha",eight)
korim=Student("korim",ten)
jodu=Student("jodu ",nine)
school.student_admission(rahim)
school.student_admission(fahim)
school.student_admission(raha)
school.student_admission(korim)
school.student_admission(jodu)

#  adding teacher

abul=Teacher("Abul khan")
habul=Teacher("habul")
kabul=Teacher("kabul")

# addin subject
bangla=Subject("bangla",abul)
english=Subject("english",habul)
chemistry=Subject("chemistry",kabul)
biology=Subject("biology",abul)  

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(chemistry)
eight.add_subject(biology)
nine.add_subject(bangla)
nine.add_subject(english)
nine.add_subject(chemistry)
nine.add_subject(biology)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(chemistry)
ten.add_subject(biology)



for classroom in school.classrooms.values():
    classroom.take_semester_final_exm()

print(school)




