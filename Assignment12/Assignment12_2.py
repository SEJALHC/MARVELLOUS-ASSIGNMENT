class Circle:
    PI=3.14

    def __init__(self):
        self.radius=0.0
        self.circumference=0.0
        self.area=0.0

    def accept(self):
        self.radius=float(input("Radius:"))

    def CalculateA(self):

        self.area=Circle.PI*self.radius*self.radius
    
    def calculateC(self):
        self.circumference=2*self.radius*Circle.PI

    def display(self):
        print(f"Radius is : {self.radius}")
        print(f"area is : {self.area}")
        print(f"circumference is: {self.circumference}")

c1=Circle()
c1.accept()
c1.CalculateA()
c1.calculateC()
c1.display()

