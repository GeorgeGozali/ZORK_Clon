map_dict = {
    "West Of House": {
        "place": "West Of House",
        "description": "This is an open field west of a white house, with a boarded front door.",
        "exits": {
            "n": "North Of House",
            "s": "South Of House",
            "e": "The door is locked, and there is evidently no key.",
            "w": "Forest",
            "ne": None,
            "nw": None,
            "se": None,
            "sw": None
        }
    },
    "North Of House": {
        "place": "North Of House",
        "description": "You are facing the north side of a white house. There is no door here, and all the windows are barred.",
        "exits": {
            "n": "Forest Path",
            "s": "West Of House",
            "e": "Behind House",
            "w": "West Of House",
            "ne": None,
            "nw": None,
            "se": None,
            "sw": None
        }
    },
    "South Of House": {
        "place": "South Of House",
        "description": "You are facing the south side of a white house. There is no door here, and all the windows are barred.",
        "exits": {
            "n": "The windows are all barred.",
            "s": "Forest 3",
            "e": "Behind House",
            "w": "West Of House",
            "ne": None,
            "nw": None,
            "se": None,
            "sw": None
        }
    },
    "Behind House": {
        "place": "Behind House",
        "description": "You are behind the white house. In one corner of the house there is a small window which is slightly ajar.",
        "exits": {
            "n": "North Of House",
            "w": "The window is closed.",
            "s": "South Of House",
            "e": "Clearing",
            "ne": None,
            "nw": None,
            "se": None,
            "sw": None

        }
    },
    "Clearing": {
        "place": "Clearing",
        "description": "You are in a clearing, with a forest surrounding you on the west and south.",
}
