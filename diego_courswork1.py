import os

inventory = {}
product_ids = set()
categories = ["Electronics", "Home", "Office"]

current_id = 100 


class Product:
    def __init__(self, name, price, quantity, brand, category, product_id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
        self.category = category
        self.product_id = product_id

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def display(self):
        print(f"ID: {self.product_id} | Name: {self.name} | Brand: {self.brand[0]} | Category: {self.category}")
        print(f"Price: ${self.price:.2f} | Quantity: {self.quantity}")


class PerishableProduct(Product):
    def __init__(self, name, price, quantity, brand, category, product_id, expiration_date):
        super().__init__(name, price, quantity, brand, category, product_id)
        self.expiration_date = expiration_date

    def display(self):
        super().display()
        print(f"Expiration Date: {self.expiration_date}")


FILE_NAME = "inventory.txt"