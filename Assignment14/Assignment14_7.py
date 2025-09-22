class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}, Salary: {self.salary}")

t = Teacher("Anjali", 30, "Maths", 45000)
t.display()
