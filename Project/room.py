from item import Item  # Ensure this import is correct based on your file structure

class Room:
    """
    Think of a 'Room' as a little world within your game where adventure happens. It's a space that players can explore, filled with items to interact with and doors (exits) that lead to other exciting places.

    Each room has its own vibe, told through its description, and it's packed with potential treasures or tools (items) that can help players on their quest. Oh, and each room has its secrets, which means there might be some clever hints hidden in the descriptions.

    Attributes:
        description (str): A little story snippet that paints a picture of what the room looks like.
        exits (dict): It's like a map of doorways telling you where you can go from here, linking to other rooms.
        items (list): The goodies! This is a collection of items just waiting to be discovered.
    """
    def __init__(self, description):
        """
        When we create a new room, we start with just a description. It's like setting the stage for a play.

        :param description: A string that sets the scene for the room.
        """
        self.description = description
        self.exits = {}
        self.items = []
        self.initialize_items()

    def set_exit(self, direction, neighbor):
        """
        Here's how we make a doorway to another room. You tell the room which way the door goes and where it leads.

        :param direction: A string that says where the door is, like 'north' or 'east'.
        :param neighbor: The room that's just a hop, skip, and a jump through this door.
        """


        self.exits[direction] = neighbor

    def get_item_description(self):
        """
        Want to know what's in the room without picking up each item? This will tell you all about them in one glance.

        :return: A string that's like a list of all the interesting stuff you can find.
        """


        if not self.items:
            return "No items to be seen here."
        else:
            return "You notice items: " + ", ".join([f"{item.name} ({item.description})" for item in self.items])

    def get_long_description(self):
        """
        This is the grand tour of the room! You get the full picture: the exits, the items, and some juicy hints that might tickle your curiosity.

        :return: A string that gives you the full story of what the room is all about.
        """
        item_desc = self.get_item_description()
        exit_desc = "Exits: " + ", ".join(self.exits.keys())
        hint_desc = self.get_hint_description()
        return f"{self.description}. {exit_desc}. Items: {item_desc}. {hint_desc}"

    def get_hint_description(self):
        """
        Everyone loves a good nudge in the right direction! This gives players hints about what might be lurking or hidden in the room.

        :return: A string with a nudge or a whisper of a secret just waiting to be discovered.
        """


        if "beach" in self.description:
            return "The sand to the east seems to have been disturbed recently..."
        if "cliffside" in self.description:
            return "To the north, something glitters faintly in the corner of your eye."
        if "mysterious_cave" in self.description:
            return "Echoes from the north hint at hidden secrets."
        if "secret_tunnel" in self.description:
            return "The walls of the tunnel seem to whisper secrets of a hidden key."
        
        if "abandoned_cabin" in self.description:
            return "An old map might be tucked away in some forgotten corner here."
        
        if "shipwreck" in self.description:
            return "The wreck's remains might still hold navigational tools of old."

        # Add more hints for other rooms as needed
        return "Mysteries seem to lurk in every corner of this place."

    def add_item(self, item):
        """
        Got a new treasure or tool for the room? Here's where it gets added to the room's collection.

        :param item: The new shiny thing or useful gadget that's finding its new home in the room.
        """

        self.items.append(item)

    def remove_item(self, item):
        """
        Time to say goodbye to an item? This is like the room waving farewell as the item leaves its collection.

        :param item: The item that's been picked up and taken on a new adventure.
        """

        self.items.remove(item)

    def get_exit(self, direction):
        """
        Wondering where that door leads? This will tell you which room is just through that exit.

        :param direction: A string that points you to the door you're curious about.
        :return: The room that awaits on the other side, if there is one.
        """
        return self.exits.get(direction, None)

    def initialize_items(self):
        """
        When we first dream up a room, this is like planting seeds for items that'll grow there. It sets up the items that make the room special.
        """
        if "beach" in self.description:
            self.add_item(Item("spyglass", "An old spyglass, maybe you can spot something in the distance", 1))
            self.add_item(Item("shovel", "A sturdy shovel, useful for digging", 3))
        if "secret_tunnel" in self.description:
            self.add_item(Item("key", "A mysterious key with ancient symbols", 1))
    
        if "abandoned_cabin" in self.description:
            self.add_item(Item("map", "A tattered map showing unknown lands", 1))
        
        if "shipwreck" in self.description:
            self.add_item(Item("compass", "An old but still functional compass", 1))


    def get_item(self, item_name):
        """
        Looking for something specific? Call this and it's like asking the room, "Hey, do you have this?"

        :param item_name: The name of the item you're searching for.
        :return: The item if it's there, just waiting for you to find it.
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
