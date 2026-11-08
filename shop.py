
class Shop:

    def __init__(self):
        self.products = []

    def laptop(self, name, price, brand):
        product = {
            "name": name,
            "price": price,
            "brand": brand
        }
        self.products.append(product)
        print("Laptop added successfully!")

    def phone(self, name, price, brand):
        product = {
            "name": name,
            "price": price,
            "brand": brand
        }
        self.products.append(product)
        print("Phone added successfully!")


shop = Shop()

shop.laptop("Laptop", 50000, "HP")
shop.phone("Phone", 15000, "Samsung")

print(shop.products)
