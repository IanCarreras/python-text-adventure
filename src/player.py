# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location, items=None):
        self.name = name
        self.location = location
        self.items = items

    def add_item(item):
        if items is None:
            items = []
        items.append_to(item, items)
        return items

    def __str__(self):
        return f'{self.name}'