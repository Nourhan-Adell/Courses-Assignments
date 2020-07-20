class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("We are out of stuck")
        else:
            print("We don't have this product")

    def print_purchases(self):
        for item in self.purchases:
            print(item)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key + ':' + str(value))
        print()


customer = Customer("Nourhan", "Nourhan@hmail.com")
# print(customer.name)
# print(customer.email)
# print()

apple_watch = Product("Apple_watch", 299)
# print(apple_watch.name)
# print(apple_watch.price)
# print()

mac = Product("Mac", 1999)
# print(mac.name)
# print(mac.price)
# print()

inventory = Inventory()
inventory.add_product("Apple_watch", 100)
inventory.add_product("Mac", 489)

inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)
inventory.print_inventory()
customer.print_purchases()
