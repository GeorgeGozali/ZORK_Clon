import json

DEFAULT_HEALTH = 100
START_LOCATION = "West Of House"


class Place:
    def __init__(self, place, description, exits):
        self.place = place
        self.description = description
        self.exits = exits

    def __str__(self):
        return self.place


class Map(Place):
    def __init__(self):
        self.map_dict = {}
        self.load_map()
        # self.place = Place(**self.load_map())

    def load_map(self):
        with open("map.json", "r") as f:
            self.map_dict = json.load(f)

    def get(self, key):
        return self.map_dict.get(key)


class Player():
    _health = DEFAULT_HEALTH
    map = Map()

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value: int) -> None:
        self._health = new_value

    def move(self, direction):
        print(map.__dict__)
        # new_direction = map.
        # if new_direction:
        #     self.current_location = map_dict.get(new_direction)
        #     if self.current_location:
        #         self.update(new_location=new_direction)
        #         self.look()
        #     else:
        #         print(new_direction, "\n")
        # else:
        #     print("You can't go that way.\n")

    # TODO change so it no longer uses class attributes but map/room objects
    def look(self):
        print(self.__dict__.get("place"))
        print(self.__dict__.get("description"), "\n")


player = Player()


def run():
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
            player.move(user_input)


if __name__ == '__main__':
    player = Player()
    # player.map = Map()
    run()
