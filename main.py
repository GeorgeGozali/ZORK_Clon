import json

DEFAULT_HEALTH = 100
START_LOCATION = "West Of House"
DIRECTIONS = ["n", "s", "e", "w", "ne", "nw", "se", "sw"]


class Place:
    def __init__(self, place, description, exits):
        self.place = place
        self.description = description
        self.exits = exits
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
        print(current_room.description, "\n")

    # def get(self, place_name):
    #     return self.map_dict.get(place_name)


class Player():
    _health = DEFAULT_HEALTH

    def __init__(self, location=START_LOCATION):
        self.location = location
        self.inventory = []

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_value: int) -> None:
        self._health = new_value

    def pick_up(self, current_room, item=None):
        if not item:
            return "What do you want to pick up?"
        elif item in current_room.items and item not in self.inventory:
            self.inventory.append(item)
            return "Taken."
        elif item in self.inventory:
            return "You already have that."
        else:
            "You can't see any such thing."

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


player = Player()


def run():
    player = Player()
    map = Map()
    current_room: Place = map.get_place(player.location)

    while True:
        user_input = input(">")
        if user_input == "look":
            map.look(current_room)
        elif user_input in DIRECTIONS:
            direction = map.get_place(current_room.exits.get(user_input))
            if isinstance(direction, Place):
                current_room = direction
            if direction:
                print(direction, "\n")
            else:
                print("You can't go that way.\n")
        elif user_input.startswith("look") and user_input[-1] in DIRECTIONS:
            print(map.look_direction(current_room, user_input[-1]), "\n")
        elif user_input.startswith("get"):
            print(player.pick_up())
        else:
            print(user_input)
            print("That's not a verb I recognise.\n")

    # current_room = map.get(current_room.get_north())
    # current_room.get_south()
    # while True:
    #     user_input = input(">")
    #     if user_input == "q":
    #         user_input = input("Are you sure you want to quit? ")
    #         while user_input.lower() not in ("y", "yes", "n", "no"):
    #             user_input = input("Please answer yes or no.>")
    #         if user_input.lower() in ("y", "yes"):
    #             break
    #     elif user_input == "look":
    #         player.look()
    #     elif user_input in ("n", "s", "e", "w", "ne", "nw", "se", "sw"):
    #         player.move(user_input)


if __name__ == '__main__':
    # player = Player()
    # player.map = Map()
    run()
