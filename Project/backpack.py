class Backpack:
    """
    Imagine a backpack as your trusty companion on an epic quest. It's got space for all your loot and treasures but remember, it can only take so much before it's bursting at the seams!

    The Backpack class is like the virtual version of that: it helps keep track of all the cool stuff your character is hauling around. It's smart enough to know its limits, both in how many items it can hold and the total weight it can manage.

    Attributes:
        contents (list): Think of this as the main pocket of your backpack where all your items are kept.
        capacity (int): This is the max number of trinkets and tools you can stuff in there.
        max_weight (float): This is the heaviest load your backpack can handle without breaking your back.
        current_weight (float): Here's the current heft of everything you've got packed.
    """

    def __init__(self, capacity, max_weight):
        """
        When you first sling your backpack over your shoulder, this is like deciding how big it is and how much it can carry. You're setting it up for your adventure.

        :param capacity: How many items can you pack? This number keeps you from overpacking.
        :param max_weight: What's the weight limit? Keep it light enough to carry on your journey.
        """


        self.contents = []
        self.capacity = capacity
        self.max_weight = max_weight
        self.current_weight = 0

    def add_item(self, item):
        """
        Found something shiny? Use this to tuck it into your backpack. But watch out – if it's too heavy or your bag's too full, you'll have to leave it behind.

        :param item: The cool thing you're trying to pack. It's gotta have weight, or it's like it's not even there.
        :return: A little note to yourself saying if the item's snug in your backpack or if you've gotta drop something else first.
        """


        if len(self.contents) < self.capacity and self.current_weight + item.weight <= self.max_weight:
            self.contents.append(item)
            self.current_weight += item.weight
            return "Ye hoisted the item into your backpack!"
        elif len(self.contents) >= self.capacity:
            return "Arrr, no more space to stow booty!"
        else:
            return "That's too heavy to carry!"

    def remove_item(self, item):
        """
        Dropping items is part of the adventure. Maybe you're lightening the load, or maybe you're just making room for an even better treasure.

        :param item: The thing you're taking out. It's like saying bye to an old friend.
        :return: A quick message that tells you the item's been removed. No need to turn back!
        """

        if item in self.contents:
            self.contents.remove(item)
            self.current_weight -= item.weight
            return f"Ye dropped the {item.name} like a hot potato!"
        return "That item's not in yer backpack!"

    def list_items(self):
        """
        Want to see a quick list of your inventory? This is like dumping out your backpack but in a neat, organized way.

        :return: A lineup of everything you've got packed, so you know what you're working with.
        """


        return [item.name for item in self.contents]

    def has_item(self, item_name):
        """
        Ever wonder if you packed that one thing? This is like quickly rummaging through your bag to check.

        :param item_name: The name of the thing you're digging for.
        :return: A simple yes or no – did you pack it, or is it still lying on your bedroom floor?
        """
        return any(item.name.lower() == item_name.lower() for item in self.contents)
