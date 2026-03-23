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

def load_inventory():
    global current_id
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) >= 6:
                    pid = int(data[0])
                    name = data[1]
                    brand = (data[2],)
                    category = data[3]
                    price = float(data[4])
                    quantity = int(data[5])

                    product = Product(name, price, quantity, brand, category, pid)
                    inventory[name] = product
                    product_ids.add(pid)
                    current_id = max(current_id, pid)

def save_inventory():
    with open(FILE_NAME, "w") as file:
        for product in inventory.values():
            file.write(f"{product.product_id},{product.name},{product.brand[0]},{product.category},{product.price},{product.quantity}\n")

def add_item():
    global current_id

    name = input("Enter product name: > ").strip()

    print(f"Enter category (Electronics, Home, Office):", end="")
    category = input(" > ").strip()

    if category not in categories:
        print("Invalid category. Defaulting to 'Office'.")
        category = "Office"

    brand_input = input("Enter brand name: > ").strip()
    brand = (brand_input,)  # tuple

    quantity = int(input("Enter quantity: > "))
    price = float(input("Enter price: > "))

    current_id += 1
    product_ids.add(current_id)

    product = Product(name, price, quantity, brand, category, current_id)
    inventory[name] = product

    print("\nItem added successfully!\n")

def view_inventory():
    print("\nCurrent Inventory:")
    print("--------------------")

    if not inventory:
        print("Inventory is empty.")
        return

    for product in inventory.values():
        product.display()
        print()

def update_item():
    name = input("Enter product name to update: > ").strip()

    if name in inventory:
        new_quantity = int(input("Enter new quantity: > "))
        inventory[name].update_quantity(new_quantity)
        print("\nInventory updated successfully!\n")
    else:
        print("Item not found.\n")

def remove_item():
    name = input("Enter product name to remove: > ").strip()

    if name in inventory:
        product_ids.discard(inventory[name].product_id)
        del inventory[name]
        print("\nItem removed successfully!\n")
    else:
        print("Item not found.\n")

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