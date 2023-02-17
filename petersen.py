"""
Author: Raj Verma
Date: 16/02/2023
Branch: exrtaVertex
"""
import networkx as nx
import matplotlib.pyplot as plt

class Petersen:
    def __init__(self, vertex_count, abs_diff):
        '''
        Initializes the Petersen graph with a given number of vertices and a given degree for each vertex.

        Args:
        - vertex_count (int): The number of vertices in the graph.
        - adjacent_count (int): The degree of each vertex in the graph (i.e., the number of adjacent vertices for each vertex).

        Raises:
        - ValueError: If the given adjacent_count is not between 1 and half of the given vertex_count.
        '''
        if not (abs_diff >= 1 and abs_diff <= vertex_count//2):
            raise ValueError('Number of adjacent vertices must be between 1 and half of number of vertices')
        
        self.vertex_count = vertex_count
        self.abs_diff = abs_diff
    
        self.adj_list = {}
        self.get()
    
    def get(self):
        '''
        Returns a dictionary with vertices as keys and a list of adjacent vertices as values, where the length of the value list is always equal to self.adjacent_count.
        '''
        for i in range(1, self.vertex_count+1):
            self.adj_list[i] = [
                (i%self.vertex_count)+1,
                ((i+self.abs_diff-1)%self.vertex_count)+1
            ]
    
    def __str__(self):
        '''
        Returns the adjacency list of the Petersen graph as a string.
        '''
        adj_str = ''
        for vertex, adj_list in self.adj_list.items():
            adj_str += f'{vertex}: {adj_list}\n'
        return adj_str
    
    def draw(self):
        '''
        Draws the Petersen graph using networkx and matplotlib.
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
    # Get user input for number of vertices and degree of each vertex
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter degree of each vertex: "))

    # Create and draw the Petersen graph
    g = Petersen(n, m)
    print(g)
    g.draw()
