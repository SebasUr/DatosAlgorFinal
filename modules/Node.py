class Node:
    id = 1
    def __init__(self, data, next=None, prev=None):
        self.id = Node.id
        self.data = data
        self.next = next
        self.prev = prev
        Node.id += 1

    def __str__(self):
        return f"Node {self.id}: {self.data}"