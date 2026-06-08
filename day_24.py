# 1.Build a Student class: name, marks, grade method
class Student:
    def __init__(self,name,marks,grade):
        self.name = name
        self.marks = marks
        self.grade = grade
    def data(self):
        return f"Student_data Name:'{self.name}'|Marks:{self.marks}|Grade:{self.grade}"

    def is_passed(self):
        return self.marks >= 40
    def performance(self):
        if 80 <= self.marks <= 100:
            return "Excellent"
        elif 60 <= self.marks < 80:
            return "Good"
        elif 40 <= self.marks < 60:
            return "Average"
        else:
            return "Fail"
student1 = Student("Biraj",80,10)
print(student1.data())
print(student1.is_passed())
print(student1.performance())


# 2.Store 5 student objects in a list, print the topper 
