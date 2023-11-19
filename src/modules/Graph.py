from modules.Edge import Edge

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node] = []

    def add_edge(self, start, end, weight):
        if start in self.nodes.keys() and end in self.nodes.keys():
            edge = Edge(start, end, weight)
            self.nodes[start].append(edge)
            self.nodes[end].append(edge)
            self.edges.append(edge)
        else:
            print("Some of the nodes are not in the graph.")

    def get_nodes_with_most_edges(self):
        current_max = 0

        # Encontrar el número máximo de aristas
        for key in self.nodes.keys():
            if len(self.nodes[key]) > current_max:
                current_max = len(self.nodes[key])

        # Encontrar los nodos con el número máximo de aristas
        nodes = []
        for key in self.nodes.keys():
            if len(self.nodes[key]) == current_max:
                nodes.append(key)

        # Top 3
        nodes_sorted = sorted(self.nodes.items(), key=lambda x: len(x[1]), reverse=True)
        top_3_nodes = [item[0] for item in nodes_sorted][:3]
        number_edges_top_3 = [len(self.nodes[key]) for key in top_3_nodes]
        return[nodes, top_3_nodes, current_max, number_edges_top_3]
    
    def get_strongest_edge(self):
        current_max = 0

        # Encontrar el número máximo de aristas
        for edge in self.edges:
            if edge.weight.size > current_max:
                current_max = edge.weight.size

        # Encontrar las aristas con el número máximo de aristas
        edges = []
        for edge in self.edges:
            if edge.weight.size == current_max:
                edges.append(edge)

        return edges

    def print_graph(self):
        print("Nodes: ")
        for node in self.nodes.keys():
            print("-", node)
            for edge in self.nodes[node]:
                print("  --", edge)