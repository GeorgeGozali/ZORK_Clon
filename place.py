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

    def check_item(self, item: str) -> bool:
        if item.strip() in self.items:
            return True
        return False

    def remove_item(self, item: str) -> None:
        self.items.remove(item)

    def can_enter(self) -> bool:
        if self.required_items is None:
            return True
        else:
            return False

    def __str__(self):
        return self.place
