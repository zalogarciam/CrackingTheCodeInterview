
class ListGraph:
    def __init__(self, size):
        #self.graph =  {k: [] for k in range(size)}
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

    def build_order(self, head): # BFS
        queue = [head]
        visited = [head]
        while len(queue) > 0:
            vertex = queue.pop(0)
            if vertex is not None:
                for i in self.graph[vertex]:
                    if i not in visited and i is not None:
                        visited.append(i)
                        queue.append(i)

        print('Visited', visited)

    def build_order_v2(self):
        queue = []
        dependencies_list = []
        for project in self.graph:
            for dependency in self.graph[project]:
                if dependency not in dependencies_list and dependency is not None:
                    dependencies_list.append(dependency)

        for project in self.graph:
            if project not in dependencies_list:
                queue.append(project)

        visited = []
        build_list = []
        while len(queue) > 0:
            project = queue.pop(0)
            visited.append(project)
            if project is not None:
                build_list.append(project)
                for i in self.graph[project]:
                    if i not in visited and i is not None:
                        visited.append(i)
                        queue.append(i)

        print('Build List', build_list)

new_graph = ListGraph(6)
new_graph.add_edge(('a'), ('d') )
new_graph.add_edge(('f') , ('b') )
new_graph.add_edge(('b'), ('d') )
new_graph.add_edge(('f') , ('a'))
new_graph.add_edge(('d'), ('c'))
new_graph.add_edge(('e'), (None))
new_graph.build_order('f')
new_graph.build_order_v2()
new_graph.print_graph()

new_graph2 = ListGraph(8)

new_graph2.add_edge(('f'), ('c') )
new_graph2.add_edge(('f') , ('b') )
new_graph2.add_edge(('f'), ('a') )
new_graph2.add_edge(('c') , ('a'))
new_graph2.add_edge(('b'), ('a'))
new_graph2.add_edge(('b'), ('h'))
new_graph2.add_edge(('a'), ('e'))
new_graph2.add_edge(('d'), ('g'))
new_graph2.build_order_v2()