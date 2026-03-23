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

def main():
    load_inventory()

    while True:
        print("Welcome to the Inventory Management System!")
        print("===========================================")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Remove Item")
        print("5. Exit")

        choice = input("Select an option: > ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            save_inventory()
            print("Exiting system. \nGoodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()