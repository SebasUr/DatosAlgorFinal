class Edge:
    def __init__(self, node1, node2, weight):
        self.weight = weight
        self.node1 = node1
        self.node2 = node2

    def __str__(self):
        return f"Edge: {self.node1} - {self.node2} ({self.weight})"