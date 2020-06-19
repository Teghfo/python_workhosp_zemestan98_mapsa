class Graph:
    def __init__(self):
        self.adj_mat = {}

    def add_node(self, node):
        if node in self.adj_mat:
            return 'node ro darim'

        else:
            self.adj_mat[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adj_mat and node1 in self.adj_mat:
            self.adj_mat[node1].append(node2)
            self.adj_mat[node2].append(node1)

        else:
            print(f'{node1} or {node2} not exist')

    def print_graph(self):
        print(self.adj_mat)


g = Graph()

g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')

g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('d', 'c')

g.print_graph()