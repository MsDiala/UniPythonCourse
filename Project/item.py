class Item:
    """
    Every hero's journey is filled with items, some mundane, some mythical. Each `Item` in our game is more than just a thing; it's a pocket-sized story, a piece of the puzzle, and a weight in the balance of your quest.

    Picture an `Item` as your in-game treasure, something you might find on a dusty shelf in an old library, or clutched in the grip of a vanquished foe. It's got a name to whisper, a tale to tell, and a heft to it that feels real in your digital grip.

    Attributes:
        name (str): The whispered name of this artifact, how you'll call it forth from your inventory.
        description (str): A snippet of lore, a sentence or two of description to tickle the imagination.
        weight (float): The poundage of this piece of your story, because even in games, gravity is a harsh mistress.
    """
    def __init__(self, name, description, weight):
        """
        This is where an `Item` takes its first breath, born from the ether of your game's world. You name it, describe its essence, and give it weight, grounding it in the reality of your adventure.

        :param name: The label of your item, its calling card in the world.
        :param description: A brief lore of what your item is, could be a line of an old poem or a cryptic clue.
        :param weight: How heavy is this find? Is it a feather from a phoenix or a stone from a golem's heart?
        """

        self.name = name
        self.description = description
        self.weight = weight
