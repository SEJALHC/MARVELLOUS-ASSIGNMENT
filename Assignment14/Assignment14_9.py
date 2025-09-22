class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

p1 = Product("Pen", 10)
p2 = Product("Pencil", 10)

if p1 == p2:
    print("Products have the same price")
else:
    print("Products have different prices")
