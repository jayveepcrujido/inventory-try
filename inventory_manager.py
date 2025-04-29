import data


class FruitInventoryManager:  
    def add_item(self, item, quantity):
        if item in data.inventory:
            data.inventory[item] += quantity
        else:
            data.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in data.inventory:
            if data.inventory[item] > quantity:
                data.inventory[item] -= quantity
                remaining = data.inventory[item]
                return (
                    f"Removed {quantity} of {item}. "
                    f"Remaining: {remaining}"
                )
            elif data.inventory[item] == quantity:
                del data.inventory[item]
                return f"Removed all {quantity} of {item}. Item deleted."
            else:
                available = data.inventory[item]
                return (
                    f"Cannot remove {quantity}. "
                    f"Only {available} in stock."
                )
        return f"{item} not found."

    def view_inventory(self):
        return data.inventory

    def get_stock(self, item):
        return data.inventory.get(item, 0)


# CLI
def main():
    manager = FruitInventoryManager()

    while True:
        print("\nInventory Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Check Stock")
        print("5. Exit")

        try:
            choice = input("Choose an option: ")

            if choice == "1":
                item = input("Enter item name: ").lower()
                quantity = int(input("Enter quantity: "))
                manager.add_item(item, quantity)
                print(f"\nAdded {quantity} of {item}.")

            elif choice == "2":
                item = input("Enter item name to remove: ").lower()
                quantity_str = input("Enter quantity to remove: ")
                if not quantity_str.isdigit():
                    raise ValueError("\nInvalid quantity. Must be a number.")
                quantity = int(quantity_str)
                result = manager.remove_item(item, quantity)
                print("\n", result)

            elif choice == "3":
                inventory = manager.view_inventory()
                if not inventory:
                    print("\nNo item found.")
                else:
                    for item, qty in inventory.items():
                        print(f"\n{item}: {qty}")

            elif choice == "4":
                item = input("Enter item name: ").lower()
                stock = manager.get_stock(item)
                if stock == 0:
                    print(f"\n{item} not found")
                else:
                    print(f"\nStock of {item}: {stock}")

            elif choice == "5":
                print("\nExiting Fruit Inventory Manager.")
                break

            else:
                print("\nInvalid choice.")

        except ValueError as ve:
            print(f"\nInput error: {ve}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
