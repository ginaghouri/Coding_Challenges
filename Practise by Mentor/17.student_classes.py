student1 = [12345, 'Tom', 10, 'A', 'A', 'A']


student1 = {
    'id': 12345,
    'name': 'Tom',
    'age': 10
}

student2 = {
    'id': 12346,
    'name': 'Dan',
    'age': 9
}

students = [student1, student2]

grades = {
    12345: { 'eng': 'A', 'math': 'A', 'comps': 'A' },
    12346: { 'eng': 'B', 'math': 'A+', 'comps': 'A+' }
}

class Student:
    def __init__(self, student_id, name, age, pronoun):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.pronoun = pronoun
    
    def showInformation(self):
        print(f"The student ID is {self.student_id} and the student name is {self.name}. {self.pronoun} is {self.age} years old.")
        
s1 = Student(1, "Tom", 20, 'He')
s2 = Student(2, "Jack", 21, 'He')
s3 = Student(3, "Rob", 22, 'He')
s4 = Student(4, "Kristine", 19, 'She')

students = [s1, s2, s3, s4]

for student in students:
    student.showInformation()
