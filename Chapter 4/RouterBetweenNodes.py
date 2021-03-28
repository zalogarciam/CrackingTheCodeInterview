class ListGraph:
    def __init__(self, size):
        self.graph = {}
        self.intersection_list = []

    def add_edge(self, src, des):
        if src not in self.graph:
            self.graph[src] = [des]
        else:
            if len(self.graph[src]) == 1 and self.graph[src][0] is None:
                self.graph[src] = [des]
            else:
                self.graph[src].append(des)

        if des not in self.graph and des is not None:
            self.graph[des] = [None]

    def del_edge(self, src, dest):
        self.graph[src].remove(dest)
        if len(self.graph[src]) == 0:
            del self.graph[src]

    def print_graph(self):
        print(self.graph)

    def BFS(self, vertex):
        list = []
        queue = []
        queue.append(vertex)
        visited = [vertex]
        while len(queue) > 0:
            vertex = queue.pop(-1)
            list.append(vertex)
            if vertex is not None:
                for i in self.graph[vertex]:
                    if i not in visited:
                        visited.append(i)
                        queue.append(i)
        return list

    def is_route(self, src, des):
        list = self.BFS(src)
        if des in list:
            print('Route Found')
            return True
        else:
            print('Route not found')
            return False


graph = ListGraph(7)
graph.add_edge(0, 6)
graph.add_edge(0, 2)
graph.add_edge(2, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 5)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

graph.print_graph()
graph.is_route(0, 5)
graph.is_route(1, 6)