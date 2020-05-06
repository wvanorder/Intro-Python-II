# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, attributes, items=[]):
        self.name = name
        self.attributes = attributes
        self.items = items

    def listItems(self):
        names = [i.name for i in self.items]
        
        if len(names) == 0:
            return print("\n\nthe room has no items ")
        else:
            print("the room currently has: \n")
            return print(*names, sep=', ')
