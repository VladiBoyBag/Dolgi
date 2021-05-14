from operator import attrgetter

class Edge:
    def __init__(self, weight, source, destin):
        self.weight = weight
        self.verts = (source, destin)


class Graph:
    def __init__(self, verts):
        self.num_verts = verts
        self.graph = []

    def find(self, parent, num):
        if parent[num] == num:
            return num
        return self.find(parent, parent[num])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root

        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskalmst(self):
        res = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=attrgetter('weight', 'verts'))
        parent, rank = [], []

        for vert in range(self.num_verts):
            parent.append(vert)
            rank.append(0)

        while True:
            w, (u, v) = self.graph[i].weight, self.graph[i].verts
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if (x != y):
                e += 1
                res.append([u, v, w])
                self.union(parent, rank, x, y)

            if e >= self.num_verts - 1:
                break

        for edge in res:
            print(f'{edge[0]} - {edge[1]}, {edge[2]}')


graphs = [[None, 10, 30, 50, 10],
          [10, None, None, 40, None],
          [30, None, None, 20, 10],
          [50, 40, 20, None, 30],
          [10, None, 10, 30, None]]

gr = Graph(len(graphs))

for i in range(len(graphs)):
    for k in range(len(graphs)):
        if k <= i: #Исключают дупликаты, т.к. неориентированные графы
            pass
        elif graphs[i][k] is not None:
            gr.graph.append(Edge(graphs[i][k], i, k))

gr.kruskalmst()