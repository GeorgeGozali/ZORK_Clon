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

    def check_inventory(self, item: str) -> bool:
        if item in self.inventory:
            return True
        return False

    def pick_up(self, item: str) -> str:
        self.inventory.append(item)
        return "Taken"

    def list_items(self) -> list:
        return self.inventory

    def open(self):
        pass
