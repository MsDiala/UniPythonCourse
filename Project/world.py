from room import Room


class World:
    """
    Welcome to the 'World' class, the heart of our game's universe! It's like a canvas where we paint our game's landscape with rooms that players can wander through and explore.

    Think of it as the grand map of an adventurer's playground. It's where all the magic of the game comes together, connecting different places with doorways and paths that lead to mystery and excitement.

    Attributes:
        rooms (dict): Our very own atlas of adventure, this is where we keep track of all the rooms by their names.
    """

    def __init__(self):
        """
        When we bring our game world to life, this is where it starts. It's like opening the doors to all the rooms and saying, "Here's our world, go explore!"
        """
        self.rooms = {}
        self.create_rooms()


    def create_rooms(self):
        
        """
        This is where we roll up our sleeves and build our world, room by room. We're talking about setting up secret passages, hidden corners, and all the exciting places players will discover.

        It's all behind the scenes, so you don't need to pass anything here—just watch the world take shape!
        """


        # Create rooms
        self.rooms["beach"] = Room("on the sandy Beach, the starting point of your adventure")
        self.rooms["jungle"] = Room("in the dense Jungle surrounding the island")
        self.rooms["hidden_cove"] = Room("at a Hidden Cove with a shipwreck")
        self.rooms["ancient_ruins"] = Room("among Ancient Ruins, remnants of an old civilization")
        self.rooms["mysterious_cave"] = Room("at the entrance to a Mysterious Cave")
        self.rooms["treasure_room"] = Room("in the Treasure Room, glittering with gold")
        self.rooms["echo_chamber"] = Room("inside the Echo Chamber, where every sound is amplified")
        self.rooms["forgotten_path"] = Room("on a Forgotten Path, overgrown and barely visible")
        self.rooms["cliffside"] = Room("on the Cliffside, overlooking the roaring sea")
        self.rooms["dark_abyss"] = Room("at the edge of a Dark Abyss, leading into unknown depths")
        self.rooms["secret_tunnel"] = Room("in a Secret Tunnel, hidden beneath the island")

        # Setting up exits for each room
        self.rooms["beach"].set_exit("north", self.rooms["jungle"])
        self.rooms["jungle"].set_exit("south", self.rooms["beach"])
        self.rooms["jungle"].set_exit("east", self.rooms["hidden_cove"])
        self.rooms["hidden_cove"].set_exit("west", self.rooms["jungle"])
        self.rooms["jungle"].set_exit("north", self.rooms["ancient_ruins"])
        self.rooms["ancient_ruins"].set_exit("south", self.rooms["jungle"])
        self.rooms["ancient_ruins"].set_exit("east", self.rooms["mysterious_cave"])
        self.rooms["mysterious_cave"].set_exit("west", self.rooms["ancient_ruins"])
        self.rooms["mysterious_cave"].set_exit("north", self.rooms["treasure_room"])
        self.rooms["treasure_room"].set_exit("south", self.rooms["mysterious_cave"])
        self.rooms["mysterious_cave"].set_exit("down", self.rooms["dark_abyss"])
        self.rooms["dark_abyss"].set_exit("up", self.rooms["mysterious_cave"])
        self.rooms["dark_abyss"].set_exit("north", self.rooms["secret_tunnel"])
        self.rooms["secret_tunnel"].set_exit("south", self.rooms["dark_abyss"])
        self.rooms["secret_tunnel"].set_exit("east", self.rooms["echo_chamber"])
        self.rooms["echo_chamber"].set_exit("west", self.rooms["secret_tunnel"])
        self.rooms["beach"].set_exit("east", self.rooms["cliffside"])
        self.rooms["cliffside"].set_exit("west", self.rooms["beach"])
        self.rooms["cliffside"].set_exit("north", self.rooms["forgotten_path"])
        self.rooms["forgotten_path"].set_exit("south", self.rooms["cliffside"])

    def get_room(self, room_name):
        """
            Ever get lost and need to find your way to a specific room? Just whisper the name of the place to this method, and it'll guide you right there.

            :param room_name: Just the name of the room you're looking for, like 'mysterious_cave' or 'ancient_ruins'.
            :return: The Room itself, ready to welcome you, or a gentle 'None' if it seems you're looking for a legend or myth.
            """
        return self.rooms.get(room_name)