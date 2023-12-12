from world import World
from backpack import Backpack
from text_ui import TextUI

class Game:
    """
    Ahoy, Captain of Adventure! Welcome to the helm of your very own quest in 'Treasure Island Adventure'. The Game class is the beating heart of our escapade, where all the magic of exploration and discovery happens.

    Here, we weave together the world of rooms, the treasures in your backpack, and the salty banter with your pirate interface. It's where we listen to your commands and spin them into stories of daring and danger.

    Attributes:
        world (World): The grand map of all the places you can explore.
        backpack (Backpack): Your trusty sack for stowing away all your finds.
        ui (TextUI): Your partner in crime, spinning tales and taking notes.
        current_room (Room): Where you are right now, looking for glory.
    """
    def __init__(self):
        """
        As soon as you step into this world of swashbuckling and treasure-hunting, we set the stage, load the map, prep your backpack, and roll out the welcome message.

        You start your journey at the beach - the sandy doorstep to endless adventures.
        """
        self.world = World()
        self.backpack = Backpack(capacity=5, max_weight=10)
        self.ui = TextUI()
        self.ui.show_welcome_message()
        self.current_room = self.world.get_room("beach")

    def start(self):
        """
        Raise the anchor and set sail! This is where your story unfolds, one command at a time. Will you find treasure, or will you find trouble? Only the fates (and your commands) will tell.

        The loop keeps running until you decide it's time to heave-ho and call it a day.
        """
        while True:
            self.ui.print(self.current_room.get_long_description())
            command = self.ui.get_command()
            finished = self.process_command(command)
            if finished:
                break
        self.ui.print("Thanks for playing. Goodbye!")

    def process_command(self, command):
        """
        Commands are the wind in your sails. Here, we take your words and turn them into action. Will you go north? Take the mysterious amulet? It's all in your hands, Captain!

        :param command: Your orders, loud and clear.
        :return: A flag to signal if it's time to drop anchor and end the game.
        """
        if not command:
            self.ui.print("I don't understand... try speaking Pirate?")
            return False

        cmd = command[0].lower()
        if cmd == 'quit':
            return True
        elif cmd == 'go':
            self.handle_go_command(command)
        elif cmd == 'look':
            self.ui.print(self.current_room.get_long_description())
        elif cmd == 'take':
            self.handle_take_command(command)
        elif cmd == 'drop':
            self.handle_drop_command(command)
        elif cmd == 'inventory':
            self.handle_inventory_command()
        elif cmd == 'help':
            self.ui.show_help()
        else:
            self.ui.print("Yarr! That's not a valid command, matey!")
        return False
    
    def handle_take_command(self, command):
        """
        Handles the 'take' command to pick up an item and add it to the backpack.

        :param command: The command entered by the player.
        """
        if len(command) < 2:
            self.ui.print("Take what, matey?")
            return

        item_name = command[1].lower()
        item = self.current_room.get_item(item_name)
        if item:
            if self.backpack.add_item(item):
                self.current_room.remove_item(item)
                self.ui.print(f"Ye successfully took the {item_name}!")
            else:
                self.ui.print("Can't take that, matey! Yer backpack's as full as a treasure chest.")
        else:
            self.ui.print(f"No {item_name} here, ye must be seein' things!")

    def handle_drop_command(self, command):
        """
        Handles the 'drop' command to remove an item from the backpack and leave it in the current room.

        :param command: The command entered by the player.
        """
        if len(command) < 2:
            self.ui.print("Drop what, ye scallywag?")
            return

        item_name = command[1].lower()
        item = self.backpack.get_item(item_name)
        if item:
            self.backpack.remove_item(item)
            self.current_room.add_item(item)
            self.ui.print(f"Ye dropped the {item_name} like it's hot!")
        else:
            self.ui.print(f"Ye can't drop what ye don't have, savvy?")

    def handle_go_command(self, command):
        """
        Handles the 'go' command to move the player to a different room.

        :param command: The command entered by the player.
        """
        if len(command) < 2:
            self.ui.print("Go where?")
            return
        direction = command[1].lower()
        self.go_room(direction)

    def go_room(self, direction):
        """
        Moves the player to the room in the specified direction.

        :param direction: The direction to move in.
        """
        next_room = self.current_room.get_exit(direction)
        if next_room:
            self.current_room = next_room
            self.ui.print(f"Moving to {direction}...")
            self.ui.print(self.current_room.get_long_description())
        else:
            self.ui.print("There's no way in that direction!")

    def handle_inventory_command(self):
        """
        Handles the 'inventory' command to display the contents of the player's backpack.
        """
        items = self.backpack.list_items()
        self.ui.show_inventory(items)

def main():
    """
    All hands on deck! This is where your adventure begins. Just run this script, and you're off to the races, or rather, the high seas of adventure!
    """

    game = Game()
    game.start()

if __name__ == "__main__":
    main()