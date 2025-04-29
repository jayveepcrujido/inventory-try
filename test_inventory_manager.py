import unittest
import data
from inventory_manager import FruitInventoryManager


class TestInventoryManager(unittest.TestCase):
    
    def setUp(self):
        data.inventory.clear()  # Clear any previous inventory data before each test
        self.manager = FruitInventoryManager()  # Initialize the manager

    def test_add_item(self):
        self.manager.add_item("apples", 10)  # Add apples with quantity 10
        self.assertEqual(self.manager.get_stock("apples"), 10)  # Assert apples have stock of 10

    def test_remove_item(self):
        self.manager.add_item("bananas", 5)  # Add bananas with quantity 5
        result = self.manager.remove_item("bananas", 5)  # Remove all bananas
        self.assertIn("Removed all", result)  # Check the result contains 'Removed all'
        self.assertEqual(self.manager.get_stock("bananas"), 0)  # Assert bananas stock is now 0

    def test_view_inventory(self):
        self.manager.add_item("oranges", 7)  # Add oranges with quantity 7
        inventory = self.manager.view_inventory()  # View the current inventory
        self.assertIn("oranges", inventory)  # Check that oranges are in the inventory
        self.assertEqual(inventory["oranges"], 7)  # Assert oranges quantity is 7


if __name__ == "__main__":
    unittest.main()
