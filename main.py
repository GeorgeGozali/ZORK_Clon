import json

DEFAULT_HEALTH = 100
START_LOCATION = "West Of House"


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

    def get_place(self, place_name=START_LOCATION):
        # TODO return Place object for this room
        # something like return Place(**self.map_dict.get(place_name)
        return Place(**self.map_dict.get(place_name))

    def get_direction(self, direction):
        if direction == "":
            print("You can't go that way.")
        elif self.map_dict.get(direction):
            print(direction)
            return self.get_place(direction)
        else:
            print(direction)

    def look(self, current_room):
        print(current_room.place)
        print(current_room.description)

    def get(self, place_name):
        return self.map_dict.get(place_name)


class Player():
    _health = DEFAULT_HEALTH

    def __init__(self, location=START_LOCATION):
        self.location = location

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
    player = Player()
    map = Map()
    current_room: Place = map.get_place()
    # map.look(current_room)
    # print(map.get_direction(current_room.exits.get("n")))
    # print(map.get_direction(current_room.exits.get("e")))
    # print(map.get_direction(current_room.exits.get("nw")))

    # print(map.place())
    while True:
        user_input = input(">")
        if user_input == "look":
            map.look(current_room)
        elif user_input in ("n", "s", "e", "w", "ne", "nw", "se", "sw"):
            if map.get_direction(current_room.exits.get(user_input)):
                current_room = map.get_direction(current_room.exits.get(user_input))
            else:
                map.get_direction(current_room.exits.get(user_input))

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
