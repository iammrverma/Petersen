"""
Author: Raj Verma
Date: 16/02/2023
Branch: main
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
        if not isinstance(vertex_count, int) or not isinstance(abs_diff, int):
            raise ValueError('Both arguments must be integers')        
        if not (abs_diff >= 1 and abs_diff <= vertex_count//2):
            raise ValueError('Absolute Diference must be between 1 and half of number of vertices')
        
        self.vertex_count = vertex_count
        self.abs_diff = abs_diff
        self.outer_nodes = list(range(1, self.vertex_count+1))
        self.inner_nodes = list(range(self.vertex_count+1, 2*self.vertex_count+1))
        self.edges = self._calculate_edges()

    def _calculate_edges(self):
        '''
        Calculates the edges of the Petersen graph.
        '''
        outer_nodes = self.outer_nodes
        inner_nodes = self.inner_nodes

        edges = []
        # Add edges between corresponding nodes in both circles
        for i in range(self.vertex_count):
            edges.append((outer_nodes[i], inner_nodes[i]))
        # Add edges between adjacent nodes in each circle
        for i in range(self.vertex_count):
            edges.append((outer_nodes[i], outer_nodes[(i+1) % len(outer_nodes)]))
        for i in range(self.vertex_count):
            edges.append((inner_nodes[i], inner_nodes[(i+self.abs_diff) % len(inner_nodes)]))

        return edges
    
    def draw(self):
        '''
        Draws the Petersen graph using networkx and matplotlib.
        '''
        outer_nodes = self.outer_nodes
        inner_nodes = self.inner_nodes

        # Reorder the inner nodes to follow the correct order
        inner_nodes = inner_nodes[-1:] + inner_nodes[:-1]
        # Reorder the outer nodes to follow the correct order
        outer_nodes = outer_nodes[-1:] + outer_nodes[:-1]

        # Initialize a graph object
        G = nx.Graph()

        # Add the nodes to the graph
        G.add_nodes_from(outer_nodes)
        G.add_nodes_from(inner_nodes)
        G.add_edges_from(self.edges)

        # Compute the positions of the nodes in the graph using the spring layout algorithm
        outer_pos = nx.circular_layout(outer_nodes)
        inner_pos = nx.circular_layout(inner_nodes)
        for node in inner_nodes: # moving inner nodes slightly toward the center of circle
            x, y = inner_pos[node]
            inner_pos[node] = (x * 0.8, y * 0.8)
            
        pos = {**outer_pos, **inner_pos}

        # Draw the nodes and edges
        nx.draw_networkx_nodes(G, pos, nodelist=outer_nodes, node_color='r', node_size=300)
        nx.draw_networkx_nodes(G, pos, nodelist=inner_nodes, node_color='b', node_size=200)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

        labels = {vertex: str(vertex) for vertex in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='white')

        # Show the graph
        plt.axis('off')
        plt.show()

if __name__ == "__main__":
    # Get user input for number of vertices and abdolute difference between inner vertices
    m = int(input("Enter number of vertices: "))
    n = int(input("Enter absolute difference: "))

    # Create and draw the Petersen graph
    g = Petersen(m, n)
    g.draw()
