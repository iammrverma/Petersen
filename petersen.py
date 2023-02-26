"""
Author: Raj Verma
Date: 17/02/2023
Description: This program defines a class Petersen that represents the Petersen graph, which is a small, non-planar, symmetrically regular graph. It takes input from the user for the number of vertices and absolute difference between inner vertices, and then draws the graph using networkx and matplotlib.
"""
import networkx as nx
import matplotlib.pyplot as plt


class Petersen:
    def __init__(self, vertex_count, abs_diff):
        '''
        Initializes the Petersen graph with a given number of vertices and absolute difference between adjacent vertices.

        Args:
        - vertex_count (int): The number of vertices in the graph.
        - abs_diff (int): The absolute difference between adjacent vertices.

        Raises:
        - ValueError: If vertex_count or abs_diff is not an integer, or if abs_diff is not between 1 and half of vertex_count.
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
        self.adjacent_vertices = self._calculate_adjacent_vertices()

    def _calculate_adjacent_vertices(self):
        '''
        Calculates the adjacent vertices for each vertex in the graph.

        Returns:
        - adj_list (dict): A dictionary where each key is a vertex in the graph and the corresponding value is a list of adjacent vertices.
        '''
        adj_list = {}
        for vertex in range(1, self.vertex_count+1):
            adjacent_vertices = []
            for edge in self.edges:
                if vertex in edge:
                    other_vertex = edge[0] if edge[1] == vertex else edge[1]
                    adjacent_vertices.append(other_vertex)
            adj_list[vertex] = adjacent_vertices
        return adj_list
    
    def print_adj_vertices(self):
        '''
        Prints the adjacent vertices for each vertex in the graph.
        '''       
        for vertex, adj_vertices in self.adjacent_vertices.items():
            print(f"{vertex}: {', '.join(str(v) for v in adj_vertices)}")

    def _calculate_edges(self):
        '''
        Calculates the edges of the Petersen graph.

        Returns:
        - edges (list): A list of tuples, where each tuple represents an edge(a, b, w) in the graph. where a, b are vertices and w is weight
        '''
        outer_nodes = self.outer_nodes
        inner_nodes = self.inner_nodes

        edges = []
        # Add weighted edges
        for i in range(1, self.vertex_count+1):
            # between outer node and inner node
            inner_x_outer_weight = 6*self.vertex_count-2*i+1
            edges.append((outer_nodes[i%self.vertex_count] , inner_nodes[i%self.vertex_count], inner_x_outer_weight))
            
            # between adjacent nodes in outer circle
            outer_weight = 2*self.vertex_count+2*i-1
            edges.append((outer_nodes[i-1], outer_nodes[i % self.vertex_count], outer_weight))
            
            # between adjacent nodes in outer circle
            inner_weight = 2*i-1
            if i == self.vertex_count:
                inner_weight = 2*(self.vertex_count-self.abs_diff)+1
            if i == self.vertex_count-self.abs_diff+1:
                inner_weight = 2*self.vertex_count-1
            edges.append((inner_nodes[i-1], inner_nodes[(i-1+self.abs_diff) % self.vertex_count], inner_weight))

        return edges
    
    def draw(self):
        '''
        Draws the Petersen graph using networkx and matplotlib.
        '''
        outer_nodes = self.outer_nodes[::-1] # Reorder the outer_nodes to make them clcokwise
        inner_nodes = self.inner_nodes[::-1] # Reorder the inner_nodes to make them clcokwise

        # Initialize a graph object
        G = nx.Graph()

        # Add the nodes to the graph
        G.add_nodes_from(outer_nodes)
        G.add_nodes_from(inner_nodes)
        G.add_weighted_edges_from(self.edges)

        # Compute the positions of the nodes in the graph using the spring layout algorithm
        outer_pos = nx.circular_layout(outer_nodes)
        inner_pos = nx.circular_layout(inner_nodes)
        for node in inner_nodes: # moving inner nodes slightly toward the center of circle
            x, y = inner_pos[node]
            inner_pos[node] = (x * 0.7, y * 0.7)
            
        pos = {**outer_pos, **inner_pos}

        edge_weights = [edge[2] for edge in self.edges]
        # Draw the nodes and edges
        nx.draw_networkx_nodes(G, pos, nodelist=outer_nodes, node_color='r', node_size=300)
        nx.draw_networkx_nodes(G, pos, nodelist=inner_nodes, node_color='b', node_size=200)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

        labels = {vertex: str(vertex) for vertex in G.nodes()}
        edge_labels = {(edge[0], edge[1]): edge[2] for edge in self.edges}

        nx.draw_networkx_labels(G, pos, labels, font_size=8, font_color='white')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        # Show the graph
        plt.axis('off')
        plt.title(f"Petersen({self.vertex_count}, {self.abs_diff})")
        plt.show()

if __name__ == "__main__":
    # Get user input for number of vertices and absolute difference between inner vertices
    m = int(input("Enter number of vertices: "))
    n = int(input("Enter absolute difference: "))

    # Create and draw the Petersen graph
    g = Petersen(m, n)
    
    g.draw()
