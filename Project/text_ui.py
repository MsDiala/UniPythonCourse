class TextUI:
    """
    Yo-ho-ho and a bottle of rum! Welcome to the TextUI, matey! This be the part of the ship's wheel that lets ye talk to the game and it talks back to ye. It's how ye'll give orders to your character and find out what's afoot on your grand adventure.

    Whether ye be barking commands, gabbin' with a parrot, or just takin' in the sights of Treasure Island, the TextUI be your trusty parley partner.

    No fancy graphics here – we're old school, like a map and compass guiding ye through the high seas of text-based escapades.
    """
    def get_command(self):
        """
        Call out to the winds and tell the game what ye want to do! Speak, and ye shall be heard. Your commands are the wind in the sails of your adventure.

        :return: A hearty list o' words that make up your command, split faster than a cutlass through the riggin'.
        """
        return input('Ahoy! What be yer command? > ').split()

    def print(self, text):
        """
        When the game's got somethin' to say, it'll say it through this here method. Like a message in a bottle, it delivers the news to ye with a pirate's flair.

        :param text: The words the game is dyin' to spill to ye.
        """
        print(f"Pirate says: {text}")

    def show_welcome_message(self):
        """
        Here be the grand entrance, the opening curtain to our tale of high seas and hidden treasures! This be the welcome that greets ye as ye step into the world of adventure.

        The message'll be decked out with all the pomp and circumstance worthy of a pirate's quest for glory and gold.
        """
        welcome_message = (
            "\n****************************************************\n"
            "**** Welcome to the Treasure Island Adventure! ****\n"
            "**** Embark on a thrilling quest for treasure, ****\n"
            "**** facing perilous challenges and mysteries!  ****\n"
            "**** Type 'help' to see available commands.     ****\n"
            "****************************************************\n"
        )
        self.print(welcome_message)

    def show_inventory(self, items):
        """
        Take a gander inside your backpack with this little charm. It'll tell ye what ye've got stowed away – be it gold, grub, or gizmos.

        :param items: A list o' the names of all the treasures ye be carryin'.
        """
        if items:
            self.print("In your backpack ye have: " + ", ".join(items))
        else:
            self.print("Yer backpack is as empty as a deserted island!")

    def show_help(self):
        """
        If ye ever find yerself in a spot of bother or just scratching yer noggin about what to do next, call on this little lifeline. It'll give ye the lay of the land and the know-how to navigate these treacherous waters.

        Ye'll get a rundown of all the commands ye can shout to make things happen, along with a few pearls of wisdom for good measure.
        """
        help_message = (
            "Available commands:\n"
            "- 'go [direction]' to move to another room (e.g., 'go north')\n"
            "- 'take [item]' to pick up an item\n"
            "- 'drop [item]' to drop an item from your inventory\n"
            "- 'inventory' to check what's in your backpack\n"
            "- 'look' to get a description of your surroundings\n"
            "- 'quit' to abandon the quest and exit the game\n"
            "- 'help' for showing this help message\n"
            "Keep yer wits about ye, and good luck on yer quest!"
        )
        self.print(help_message)
