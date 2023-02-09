from map import Map
from player import Player
from place import Place

import constrants as C


def run():
    map = Map()
    current_room: Place = map.get_place(C.START_LOCATION)
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
        elif user_input in C.DIRECTIONS:
            direction = map.get_place(current_room.exits.get(user_input))
            if isinstance(direction, Place):
                current_room = direction
            if direction:
                print(direction, "\n")
            else:
                print("You can't go that way.\n")
        elif user_input.startswith("look") and user_input[-1] in C.DIRECTIONS:
            print(map.look_direction(current_room, user_input[-1]), "\n")

        elif user_input.startswith("get"):
            try:
                item = user_input.strip().split(" ")[1]
                if current_room.check_item(item):
                    print(player.pick_up(item))
                    current_room.remove_item(item)
                elif player.check_inventory(item):
                    print("You already have that.\n")
                else:
                    print("You can't see any such thing.\n")
            except IndexError:
                print("What do you want to get?\n")

        elif user_input == "bag":
            print(player.list_items())
        elif user_input.startswith("open"):
            pass
        else:
            print(user_input)
            print("That's not a verb I recognise.\n")


if __name__ == '__main__':
    run()
