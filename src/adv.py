from room import Room
from item import Item

# Declare all the rooms

items = [
    Item("acorn", "Magic acorn from the oak tree grown on the peak of Bald Mountain in Velen. It can be looted from Imlerith's body."),

    Item("runsetone", "Moon runes can also be used to craft blue, red or yellow meteorite ore, though given that the price of a rune is significantly higher than that of a piece of ore, it seems a poor use of the rune."),

    Item("sword", "one-handed weapon. It once belonged to the Nightingale and former Thieves Guild Guildmaster Gallus Desidenius."),

    Item("shield", "the Daedric artifact of Peryite.")
]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items[2], items[3]]),

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
from player import Player

player = Player("popelincoln87", room['outside'])

dude = "hello"


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
while True:
    print(f"\n{player.currentRoom.name}\n{player.currentRoom.attributes}\n")

    action = input("\nPlease select which direction you would like to go\n 'check items' to see your inventory\n 'check ground' to see items in the current room\n 'take/drop item'\n or press 'q' to exit the game: \n")
    userAction = action.split(' ')
   
    if userAction[0] == 'q':
        print(f"\n\n\nand {player.name} was never heard from again...\n\n\n")
        break
    elif userAction[0] == 'take':
        player.take(userAction[1])
    elif userAction[0] == 'drop':
        player.drop(userAction[1])
    elif userAction[0] == 'check':
        if userAction[1] == 'items':
            player.checkInventory()
        elif userAction[1] == 'ground':
            player.currentRoom.listItems()
        else:
            print('please check either the ground or items in your inventory')
    elif userAction[0] == 'n' or userAction[0] == 'e' or userAction[0] == 's' or userAction[0] == 'w':
        doThis = f"{userAction[0]}_to"
        if hasattr(player.currentRoom, doThis):
            print(f"\n\n{player.currentRoom.name}")
            player.currentRoom = getattr(player.currentRoom, doThis)
            print(f"\n\n\n{player.name} moves into the {player.currentRoom.name}\n\n")
        else:
            print('\n\n\nyou cannot go that direction from here, try another way!')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.