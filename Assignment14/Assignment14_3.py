class Book:
    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

b = Book()
b.set_price(500)
print("Price of Book:", b.get_price())
