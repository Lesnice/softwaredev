class Student:
    
    
    def __init__(self, fullname, student_number, average):
        self.fullname = fullname
        self.student_number = student_number
        self.average = average
    
    def __gt__(self, other):
        return self.average > other.average


student1 = Student(" Peter P", "23243", 88)
student2 = Student(" tony P", "23553", 89)
print(student1 > student2)