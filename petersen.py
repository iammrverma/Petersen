import networkx as nx
import matplotlib.pyplot as plt

class Petersen:
    def __init__(self, vertex_count, adjacent_count):
        if not (adjacent_count >= 1 and adjacent_count <= vertex_count//2):
            raise ValueError('Number of adjacent vertices must be between 1 and half of number of vertices')
        print("Petersen graph initialized")
        
        self.vertex_count = vertex_count
        self.adjacent_count = adjacent_count
    
        self.edges = []
        self.vertices = []
        self.adj_list = {}
        self.get()
    
    def get(self):
        '''
        this function returns a dictionary with vertices as key and list of adjacent vertices as value but length of value list should be always equal to self.adjacent_count
        '''
        for i in range(1, self.vertex_count+1):
            adj = [((i+j-1) % self.vertex_count)+1 for j in range(1, self.adjacent_count+1)]
            if len(adj) == self.adjacent_count:
                self.adj_list[i] = adj
    
    def __str__(self):
        '''
        this function returns the adjacency list as a string
        '''
        adj_str = ''
        for vertex, adj_list in self.adj_list.items():
            adj_str += f'{vertex}: {adj_list}\n'
        return adj_str
    
    def draw(self):
        '''
        This function uses networkx and matplotlib to draw the Petersen graph.
        '''
        # Create a networkx graph
        G = nx.Graph()
        G.add_nodes_from(self.adj_list.keys())
        for vertex, adj_list in self.adj_list.items():
            for adj_vertex in adj_list:
                G.add_edge(vertex, adj_vertex)
        
        # Set the positions of the nodes in a circular layout
        pos = nx.circular_layout(G)

        # Draw the nodes and edges of the graph using matplotlib
        nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
        
        # Draw the labels of the nodes
        labels = {vertex: str(vertex) for vertex in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color='white')
        
        # Set the axis limits and remove the axis labels
        plt.xlim(-1.2, 1.2)
        plt.ylim(-1.2, 1.2)
        plt.axis('off')

        # Show the graph
        plt.show()

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter degree of each  vertex: "))

    g = Petersen(n, m)
    print(g)
    g.draw()
