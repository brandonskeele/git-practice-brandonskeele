class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


    def discount_price(self, percentage):
        return self.price - (self.price * (percentage / 100))
    

    def change_price(self, new_price):
        self.price = new_price


toy = Product(12345, "Teddy Bear", 4)
print(toy.id)
print(toy.name)
print(toy.price)

print(toy.discount_price(20))
toy.change_price(10.2)
print(toy.price)