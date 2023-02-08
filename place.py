class Place:
    def __init__(self, place, description, exits, items, required_items=None):
        self.place = place
        self.description = description
        self.exits = exits
        self.items = items
        self.required_items = required_items
        # self.north = exits["n"]
        # self.south = exits["s"]
        # self.east = exits["e"]
        # self.west = exits["w"]
        # self.northeast = exits["ne"]
        # self.northwest = exits["nw"]
        # self.southeast = exits["se"]
        # self.southwest = exits["sw"]

    # TODO create method to check if item is in the room

    def remove_item(self, item: str) -> None:
        self.items.remove(item)

    # TODO "enter" method that returns True if the player can enter this room

    def __str__(self):
        return self.place
