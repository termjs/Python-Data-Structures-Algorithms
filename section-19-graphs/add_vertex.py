# Graph: Add Vertex

class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.adj_list = {}

    def add_vertex(self, vertex):
        # Add a vertex if it does not already exist in the adjacency list
        if vertex not in self.adj_list.keys():  # Check if the vertex is not in the list
            self.adj_list[vertex] = []          # Add the vertex with an empty list of neighbors
            return True                         # Return True if the vertex was added
        return False                            # Return False if the vertex already exists
    
    def print_graph(self):
        # Print each vertex and its list of adjacent vertices
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

my_graph = Graph()

# Add vertex "A" to the graph
my_graph.add_vertex("A")

# Print the adjacency list of the graph
my_graph.print_graph()
