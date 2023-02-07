from map import map_dict


class Map:
    def move(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)



# class BASE(Map):
#     pass


class User(Map):
    _health = 100
    current_location = map_dict.get("West Of House")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value):
        self._health = new_value

    def move(self, direction):
        new_direction = self.current_location['exits'][direction]
        if map_dict.get(new_direction):
            super().move(**map_dict.get(new_direction))
            self.current_location = map_dict.get(new_direction)
        elif new_direction is None:
            print("You can't go that way.")
        else:
            print(new_direction)


u = User()

while True:
    user_input = input(">")
    if user_input == "q":
        break
    elif user_input == "look":
        print(u.current_location.get("place"))
        print(u.current_location.get("description"), "\n")
    elif user_input in ("n", "s", "e", "w", "ne", "nw", "se", "sw"):
        u.move(user_input)
        print(u.current_location['place'], "\n")
