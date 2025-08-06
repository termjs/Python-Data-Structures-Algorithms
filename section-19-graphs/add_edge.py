# Graph: Add Edge

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
        
        # {
        #     1: [2],
        #     2: [1]
        # } We want to do this only if both vertices exist

        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # Check if both vertices exist
            self.adj_list[v1].append(v2) # Add v2 to v1
            self.adj_list[v2].append(v1) # Add v1 to v2
            return True # Success and stop
        return False # Fail and stop

my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()
