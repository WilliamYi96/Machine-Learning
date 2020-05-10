class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.append(0, item)

    def removeFront(self, item):
        return self.items.pop()
    
    def removeRear(self, item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)