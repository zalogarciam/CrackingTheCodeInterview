
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

    def DFS(self, vertex, visited):
        if vertex not in visited:
            print(vertex)
            visited.append(vertex)
            if vertex is not None:
                for i in self.graph[vertex]:
                    self.DFS(i, visited)

    def DFS_iterative(self, vertex):
        visited = []
        stack = []
        stack.append(vertex)
        while len(stack) > 0:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex)
                visited.append(vertex)
            if vertex is not None:
                for i in self.graph[vertex]:
                    if i not in visited:
                        stack.append(i)


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



    def bidirectional_search(self, src, des):

        visited_src = [src]
        queue_src = [src]
        visited_des = [des]
        queue_des = [des]
        while len(queue_src) > 0 and len(queue_des) > 0:
            src = queue_src.pop(-1)
            des = queue_des.pop(-1)

            if src not in self.intersection_list and src is not None:
                self.intersection_list.append(src)
            else:
                print('Intersection in: ', src)
                break

            if des not in self.intersection_list and des is not None:
                self.intersection_list.append(des)
            else:
                print('Intersection in: ', des)
                break

            for i in self.graph[src]:
                if i not in visited_src:
                    queue_src.append(i)
                    visited_src.append(i)

            for i in self.graph[des]:
                if i not in visited_des:
                    queue_des.append(i)
                    visited_des.append(i)

    def is_route(self, src, des):
        list = self.BFS(src)
        if des in list:
            print('Route Found')
            return True
        else:
            print('Route not found')
            return False

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

list_graph = ListGraph(15)


list_graph.add_edge(0, 1)
list_graph.add_edge(0, 3)
list_graph.add_edge(1, 2)
list_graph.add_edge(2, 0)
list_graph.add_edge(3, 2)
list_graph.add_edge(3, 1)
list_graph.add_edge(0, 4)
list_graph.add_edge(1, 4)
list_graph.add_edge(4, 6)
list_graph.add_edge(2, 5)
list_graph.add_edge(3, 5)
list_graph.add_edge(5, 6)
list_graph.add_edge(6, 7)
list_graph.add_edge(8, 7)
list_graph.add_edge(9, 8)
list_graph.add_edge(10, 8)
list_graph.add_edge(14, 10)
list_graph.add_edge(13, 10)
list_graph.add_edge(12, 9)
list_graph.add_edge(11, 9)

list_graph.bidirectional_search(0, 14)
list_graph.bidirectional_search(0, 2)
list_graph.del_edge(1, 2)
list_graph.DFS(0, [])
list_graph.DFS_iterative(0)
list_graph.BFS(0)
list_graph.BFS(2)
list_graph.print_graph()