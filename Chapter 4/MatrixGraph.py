class MatrixGraph:
    def __init__(self, size):
        self.size = size
        self.adjMatrix = []
        for i in range(size):
            tmp_list = [0] * size
            self.adjMatrix.append(tmp_list)

    def add_edge(self, src, des):
        #print(self.adjMatrix)
        self.adjMatrix[src][des] = 1

    def del_edge(self, src, des):
        self.adjMatrix[src][des] = 0

    def print_graph(self):
        show = ''
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j] == 1:
                    show += str(i) + " --> " + str(j) + '\n'
        print(show)

matrix_graph = MatrixGraph(5)
matrix_graph.add_edge(0, 1)
matrix_graph.add_edge(1, 2)
matrix_graph.add_edge(2, 0)
matrix_graph.add_edge(3, 2)
matrix_graph.add_edge(3, 1)
matrix_graph.print_graph()
matrix_graph.del_edge(1, 2)
matrix_graph.print_graph()