# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        if self.items is None:
            self.items = []
        self.items.append(item)
        return self.items

    def __str__(self):
        if items is not None:
            return f''
        return f'{self.name}: {self.description}'