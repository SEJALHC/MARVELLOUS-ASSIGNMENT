class Student:
    school_name = "Marvellous School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")

s1 = Student("Sejal", 101)
s1.display()

# Changing class variable
Student.school_name = "Updated School"
s1.display()
