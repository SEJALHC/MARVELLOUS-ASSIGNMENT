class BookStore:
    noofbooks=0

    def __init__(self,name,author):
        self.name=name
        self.author=author
        BookStore.noofbooks+=1

    def display(self):
        print(f"{self.name} by {self.author}.no of books:{BookStore.noofbooks}")



obj1=BookStore("linux sytm","robert love")
obj1.display()
obj2=BookStore("c programming","dennis ritchie")
obj2.display()