# inventory_manager.py

import data

class InventoryManager:
    def add_item(self, item, quantity):
        if item in data.inventory:
            data.inventory[item] += quantity
        else:
            data.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in data.inventory:
            if data.inventory[item] > quantity:
                data.inventory[item] -= quantity
                return f"Removed {quantity} of {item}. Remaining: {data.inventory[item]}"
            elif data.inventory[item] == quantity:
                del data.inventory[item]
                return f"Removed all {quantity} of {item}. Item deleted."
            else:
                return f"Cannot remove {quantity}. Only {data.inventory[item]} in stock."
        return f"{item} not found."

    def view_inventory(self):
        return data.inventory

    def get_stock(self, item):
        return data.inventory.get(item, 0)

# CLI
def main():
    manager = InventoryManager()
    while True:
        print("\nInventory Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Check Stock")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item name: ").lower()
            quantity = int(input("Enter quantity: "))
            manager.add_item(item, quantity)
            print(f"Added {quantity} of {item}.")
        elif choice == "2":
            item = input("Enter item name to remove: ").lower()
            quantity_str = input("Enter quantity to remove: ")
            if not quantity_str.isdigit():
                print("Invalid quantity. Must be a number.")
                continue

            quantity = int(quantity_str)
            result = manager.remove_item(item, quantity)
            print(result)

        elif choice == "3":
            inventory = manager.view_inventory()
            if not inventory:
                print()
                print("No item found.")
            else:
                for item, qty in inventory.items():
                    print(f"{item}: {qty}")
        elif choice == "4":
            item = input("Enter item name: ").lower()
            stock = manager.get_stock(item)
            if stock == 0:
                print(f"{item} not found")
            else:
                print(f"Stock of {item}: {stock}")

        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
