# Graph: Remove Edge

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        # Check if both vertices exist in the adjacency list
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Remove v2 from v1's adjacency list
            self.adj_list[v1].remove(v2)
            # Remove v1 from v2's adjacency list
            self.adj_list[v2].remove(v1)
            return True  # Edge successfully removed
        return False  # Edge not removed

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")

print()  # Add a blank line for spacing
my_graph.print_graph()
print()

my_graph.remove_edge("A", "B")

my_graph.print_graph()
