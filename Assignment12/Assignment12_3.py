class Arithmetic():
    def __init__(self):
        self.value1=0
        self.value2=0
      

    def Accept(self):
        self.value1=int(input("enter value1:"))
        self.value2=int(input("enter value2:"))
       

    def Add(self):
         return self.value1+self.value2

    def sub(self):
        return self.value1-self.value2


    def mult(self):
        return self.value1*self.value2
    
    def div(self):
        if self.value2 !=0:
            return self.value1/self.value2
        else:
            print("division not possible")
    
a1=Arithmetic()
a1.Accept()
print("addition is :",a1.Add())
print("subtracton is :",a1.sub())
print("multiplication is :",a1.mult())
print("divisio  is :",a1.div())