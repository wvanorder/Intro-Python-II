# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, items=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = items

    def __str__(self):
        return f"The person {self.name} is currently in the {self.currentRoom.name} area."

    def take(self, item):
        newItem = [i for i in self.currentRoom.items if i.name == item]
        print(f"Player has picked up {newItem[0].name}")
        self.items.append(newItem[0])

        index = [self.currentRoom.items.index(i) for i in self.currentRoom.items if i.name == item]
        del(self.currentRoom.items[index[0]])

    def drop(self, item):
        index = [self.currentRoom.items.index(i) for i in self.currentRoom.items if i.name == item]
        droppedItem = [i for i in self.items if i.name == item]

        print(f"Player has dropped{droppedItem[0].name}")
        del(self.items[index[0]])

        self.currentRoom.items.append(droppedItem[0])



    def checkInventory(self):
        names = [i.name for i in self.items]
        if len(names) == 0:
            return print("\n\nthe player has no items currently")
        else:
            print("the player currently has: \n")
            return print(*names, sep=', ')