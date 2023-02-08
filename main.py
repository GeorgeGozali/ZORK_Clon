import json

DEFAULT_HEALTH = 100
START_LOCATION = "West Of House"
DIRECTIONS = ["n", "s", "e", "w", "ne", "nw", "se", "sw"]


class Place:
    def __init__(self, place, description, exits, items, required_items):
        self.place = place
        self.description = description
        self.exits = exits
        self.items = items
        self.required_items = None
        # self.north = exits["n"]
        # self.south = exits["s"]
        # self.east = exits["e"]
        # self.west = exits["w"]
        # self.northeast = exits["ne"]
        # self.northwest = exits["nw"]
        # self.southeast = exits["se"]
        # self.southwest = exits["sw"]

    # def look(self):
    #     print(self.place)
    #     print(self.description)

    def __str__(self):
        return self.place

# place1 = Place("West Of House", "idk", {"n": "North Of House"})
# place2 = Place("North Of House", "idk", {"s": "South Of House"})


# map.get(place1.get_north())


class Map(Place):
    def __init__(self):
        self.map_dict = {}
        self.load_map()

    def load_map(self):
        with open("map.json", "r") as f:
            self.map_dict = json.load(f)

    def get_place(self, place_name):
        if self.map_dict.get(place_name):
            return Place(**self.map_dict.get(place_name))
        else:
            return place_name

    def look_direction(self, current_room, direction):
        return current_room.exits.get(direction)

    def look(self, current_room):
        print(current_room.place)
        print(current_room.description)
        if current_room.items:
            print(current_room.items, "\n")
        else:
            print()


class Player():
    _health = DEFAULT_HEALTH
    current_room: Place = None

    def __init__(self, location=START_LOCATION):
        self.location = location
        self.inventory = []

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value: int) -> None:
        self._health = new_value

    def pick_up(self, item=None):
        if not item:
            return "What do you want to pick up?"
        elif item not in self.current_room.items:
            return "You can't see any such thing."
        elif item in self.current_room.items and item not in self.inventory:
            self.inventory.append(item)
            return "Taken."
        else:
            return "You already have that."

    def open(self, current_):
        pass


def run():
    map = Map()
    current_room: Place = map.get_place(START_LOCATION)
    player = Player()
    player.current_room = current_room

    while True:
        user_input = input(">")
        if user_input == "q":
            user_input = input("Are you sure you want to quit? ")
            while user_input.lower() not in ("y", "yes", "n", "no"):
                user_input = input("Please answer yes or no.>")
            if user_input.lower() in ("y", "yes"):
                break
        elif user_input == "look":
            map.look(current_room)
        elif user_input in DIRECTIONS:
            direction = map.get_place(current_room.exits.get(user_input))
            if isinstance(direction, Place):
                current_room = direction
                player.current_room = current_room
            if direction:
                print(direction, "\n")
            else:
                print("You can't go that way.\n")
        elif user_input.startswith("look") and user_input[-1] in DIRECTIONS:
            print(map.look_direction(current_room, user_input[-1]), "\n")
        elif user_input.startswith("get"):
            print(player.pick_up(user_input.split(" ")[1]))
        elif user_input == "bag":
            print(player.inventory)
        else:
            print(user_input)
            print("That's not a verb I recognise.\n")

    # current_room = map.get(current_room.get_north())
    # current_room.get_south()


if __name__ == '__main__':
    # player = Player()
    # player.map = Map()
    run()
