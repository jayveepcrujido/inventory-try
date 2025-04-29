import unittest
import data
from inventory_manager import FruitInventoryManager


class TestInventoryManager(unittest.TestCase):

    def setUp(self):
        data.inventory.clear()
        self.manager = FruitInventoryManager()

    def test_add_item(self):
        self.manager.add_item("apples", 10)
        self.assertEqual(self.manager.get_stock("apples"), 10)

    def test_remove_item(self):
        self.manager.add_item("bananas", 5)
        result = self.manager.remove_item("bananas", 5)
        self.assertIn("Removed all", result)
        self.assertEqual(self.manager.get_stock("bananas"), 0)

    def test_view_inventory(self):
        self.manager.add_item("oranges", 7)
        inventory = self.manager.view_inventory()
        self.assertIn("oranges", inventory)
        self.assertEqual(inventory["oranges"], 7)


if __name__ == "__main__":
    unittest.main()
