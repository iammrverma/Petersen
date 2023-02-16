import networkx as nx
import matplotlib.pyplot as plt #pip install matplotlib

class PetersenGraph:
    
    def __init__(self):
        self.graph = nx.Graph()
        self.graph.add_nodes_from(range(10))
        self.graph.add_edges_from([(i, (i+1)%5) for i in range(5)])
        self.graph.add_edges_from([(i, i+5) for i in range(5)])
        self.graph.add_edges_from([(i+5, (2*i+1)%5+5) for i in range(5)])
        self.pos = {0: (0, 1), 1: (0.95, 0.31), 2: (0.59, -0.81), 3: (-0.59, -0.81), 4: (-0.95, 0.31),
                    5: (0, 0.5), 6: (0.5, 0.6), 7: (0.3, 0), 8: (-0.3, 0), 9: (-0.5, 0.6)}
        
    def draw(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        nx.draw(self.graph, self.pos, node_size=400, node_color='lightblue', with_labels=True, ax=ax)
        ax.set_title("Petersen Graph")
        plt.show()
        
    def get_adjacency_dict(self):
        return {v: list(self.graph.neighbors(v)) for v in self.graph.nodes()}


if __name__ == "__main__":
    p = PetersenGraph()
    
    print(p.get_adjacency_dict())
    p.draw()
