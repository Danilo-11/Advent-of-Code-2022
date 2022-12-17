class File:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
