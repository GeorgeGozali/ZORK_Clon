import json
from place import Place


class Map:
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
