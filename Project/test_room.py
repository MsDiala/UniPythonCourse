import unittest
from room import Room, Item


class TestRoom(unittest.TestCase):
  
  
  def setUp(self):
    self.shovel = Item("shovel", "A sturdy shovel, useful for digging", 1)
    self.key = Item("key", "A mysterious key with ancient symbols", 1)
    self.treasure = Item("treasure", "treasure", 1)
    self.map = Item("map", "A tattered map showing unknown lands", 1)
    self.medicine = Item("herbal_medicine",
                         "A pouch of healing herbs, useful for wounds", 1)
    self.compass = Item("compass", "An old but still functional compass", 1)
    self.spyglass = Item("spyglass",
        "An old spyglass, maybe you can spot something in the distance", 1)

  def test_add_item(self):
    room = Room(description="Test Room")
    room.add_item(self.shovel)

    self.assertIn(self.shovel, room.items)

  def test_remove_item(self):
    room = Room(description="Test Room")
    room.add_item(self.shovel)
    room.remove_item(self.shovel)

    self.assertNotIn(self.shovel, room.items)

  def test_get_item(self):
    room = Room(description="Test Room")
    room.add_item(self.shovel)

    retrieved_item = room.get_item("shovel")

    self.assertEqual(retrieved_item, self.shovel)

  def test_get_item_description_no_items(self):
    room = Room(description="Empty Room")

    item_description = room.get_item_description()

    self.assertEqual(item_description, "No items to be seen here.")

  def test_get_item_description_with_items(self):
    room = Room(description="Room with Items")
    room.add_item(self.shovel)
    room.add_item(self.key)

    item_description = room.get_item_description()

    expected_description = "You notice items: shovel (A sturdy shovel, useful for digging), key (A mysterious key with ancient symbols)"
    self.assertEqual(item_description, expected_description)



  def test_get_exit(self):
    room1 = Room(description="Room 1")
    room2 = Room(description="Room 2")
    room1.set_exit("north", room2)

    exit_room = room1.get_exit("north")

    self.assertEqual(exit_room, room2)

  def test_get_exit_invalid_direction(self):
    room = Room(description="Test Room")

    exit_room = room.get_exit("invalid_direction")

    self.assertIsNone(exit_room)


if __name__ == '__main__':
  unittest.main()
