import unittest
from item import Item
from backpack import Backpack

class TestBackpack(unittest.TestCase):

    def test_add_item_success(self):
        backpack = Backpack(capacity=3, max_weight=10)

        item = Item(name="Gold Coin", weight=3,description="Gold Coin")

        result = backpack.add_item(item)

        self.assertEqual(result, "Ye hoisted the item into your backpack!")
        self.assertEqual(backpack.list_items(), ["Gold Coin"])
        self.assertTrue(backpack.has_item("Gold Coin"))

    def test_add_item_capacity_exceeded(self):
        backpack = Backpack(capacity=1, max_weight=10)
        item1 = Item(name="Gold Coin", weight=3, description="Gold Coin")
        item2 = Item(name="Silver Coin", weight=5, description="Gold Coin")

        backpack.add_item(item1)
        result = backpack.add_item(item2)

        self.assertEqual(result, "Arrr, no more space to stow booty!")
        self.assertEqual(backpack.list_items(), ["Gold Coin"])
        self.assertFalse(backpack.has_item("Silver Coin"))

    def test_add_item_weight_exceeded(self):
        backpack = Backpack(capacity=3, max_weight=5)
        item = Item(name="Gold Coin", weight=6,description="Gold Coin")

        result = backpack.add_item(item)

        self.assertEqual(result, "That's too heavy to carry!")
        self.assertEqual(backpack.list_items(), [])
        self.assertFalse(backpack.has_item("Gold Coin"))

    def test_remove_item_not_present(self):
        backpack = Backpack(capacity=3, max_weight=10)

        result = backpack.remove_item("Silver Coin")

        self.assertEqual(result, "That item's not in yer backpack!")

    def test_list_items(self):
        backpack = Backpack(capacity=3, max_weight=10)
        item1 = Item(name="Gold Coin", weight=3,description="Gold Coin")
        item2 = Item(name="Silver Coin", weight=5,description="Gold Coin")

        backpack.add_item(item1)
        backpack.add_item(item2)

        result = backpack.list_items()

        self.assertEqual(result, ["Gold Coin", "Silver Coin"])

    def test_has_item_true(self):
        backpack = Backpack(capacity=3, max_weight=10)
        item = Item(name="Gold Coin", weight=3,description="Gold Coin")
        backpack.add_item(item)

        result = backpack.has_item("Gold Coin")

        self.assertTrue(result)

    def test_has_item_false(self):
        backpack = Backpack(capacity=3, max_weight=10)

        result = backpack.has_item("Silver Coin")

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
