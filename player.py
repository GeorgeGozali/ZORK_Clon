import constrants as C


class Player:
    _health = C.DEFAULT_HEALTH

    def __init__(self, location=C.START_LOCATION):
        self.location = location
        self.inventory = []

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value: int) -> None:
        self._health = new_value

    # TODO create method to check if item is in inventory

    def pick_up(self, item):
        self.inventory.append(item)
        return "Taken"

    def open(self):
        pass
