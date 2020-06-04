from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Chioma', room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
quit = False


while not quit:

    print(
        f"Hello {player.name}! You are in the room {player.current_room.name}, {player.current_room.description}.")

    selection = input(
        "Where would you like to go? \n North(n) \n South(s) \n West(w)\n East(e) \n\n Please Input Direction:  ")

    if selection == "q":
        quit = True
        print("You Quit, Game Over")
        break
    else:
        try:
            selection = selection.lower().strip()[0]

            if 'Outside' in player.current_room.name:
                if selection != "n":
                    print('oh my, that way leads to destruction, you cannot go')
                else:
                    player.current_room = room["foyer"]
            elif 'Foyer' in player.current_room.name:
                if selection == "n":
                    player.current_room = room["overlook"]
                elif selection == "s":
                    player.current_room = room["outside"]
                elif selection == "e":
                    player.current_room = room["narrow"]
                elif (selection == "w"):
                    print('oh my, that way leads to destruction, you cannot go')

            elif 'Narrow' in player.current_room.name:
                if selection == "n":
                    player.current_room = room["treasure"]
                elif selection == "w":
                    player.current_room = room["foyer"]
                elif (selection == "e") or (selection == "s"):
                    print('oh my, that way leads to destruction, you cannot go')

            elif 'Treasure' in player.current_room.name:
                if selection != "s":
                    print('oh my, that way leads to destruction, you cannot go')
                else:
                    player.current_room = room["narrow"]

            elif 'Overlook' in player.current_room.name:
                if selection != "s":
                    print('oh my, that way leads to destruction, you cannot go')
                else:
                    player.current_room = room["foyer"]

        except TypeError:
            print('enter your direction as an alphabet e.g west or w')
