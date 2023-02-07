from map import map_dict


class Map:
    current_location = "West Of House"

    def __init__(self):
        if self.__dict__.get("place") is None:
            self.move(**map_dict.get(self.current_location))

    def move(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.current_location = self.__dict__.get("place")

    def look(self):
        print(self.__dict__.get("place"))
        print(self.__dict__.get("description"), "\n")


# class BASE(Map):
#     pass


class Player(Map):
    _health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value: int) -> None:
        self._health = new_value

    def moves(self, direction):
        new_direction = self.__dict__.get("exits").get(direction)
        if new_direction:
            try:
                super().move(**map_dict.get(new_direction))
                self.current_location = map_dict.get(new_direction)
                self.look()
            except TypeError:
                print(new_direction, "\n")
        else:
            print("You can't go that way.\n")


player = Player()

while True:
    user_input = input(">")
    if user_input == "q":
        user_input = input("Are you sure you want to quit? ")
        while user_input.lower() not in ("y", "yes", "n", "no"):
            user_input = input("Please answer yes or no.>")
        if user_input.lower() in ("y", "yes"):
            break
    elif user_input == "look":
        player.look()
    elif user_input in ("n", "s", "e", "w", "ne", "nw", "se", "sw"):
        player.moves(user_input)
        # print(dir(player))
