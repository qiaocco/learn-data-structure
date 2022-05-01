class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return f'<Node: value: {self.value}, next={self.next}>'


class LinkedList:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        node = self.root
        while node.next != None:
            node = node.next

        node.next = Node(value)
        
