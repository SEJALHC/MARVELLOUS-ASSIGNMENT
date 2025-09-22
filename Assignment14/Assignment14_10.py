class Employee:
    def __init__(self, name, department, salary):
        self.name = name               
        self._department = department 
        self.__salary = salary        

    def display(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

e = Employee("Ravi", "IT", 60000)
e.display()


print("Protected Department:", e._department)

print("Private Salary (via name mangling):", e._Employee__sala__salary)  