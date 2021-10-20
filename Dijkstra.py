import sys
class Dijkstra:

    def shortestDistance(self, edges, vertices):

        self.graph = {x : [] for x in range(vertices)}
        self.fill_graph(edges, vertices)
        if vertices == 1:
            return [0]
        if vertices == 0:
            return []
        min_d = self.dijkstra(vertices)
        for i in range(len(min_d)):
            if min_d[i] == sys.maxsize:
                min_d[i] = -1
        return min_d

    def fill_graph(self, edges, vertices):

        for node1, node2, dist in edges:
            self.graph[node1] += [(node2, dist)]

    def minimum_distance(self, min_d, spt_vertices, vertices):

        min_val = sys.maxsize
        min_node = -1
        for node in range(vertices):
            if min_d[node] < min_val and not spt_vertices[node]:
                min_val = min_d[node]
                min_node = node
        return min_node
    
    def successors_nodes(self, node):

        return self.graph[node]

    def dijkstra(self, vertices):

        start_node = 0
        min_d = [sys.maxsize] * vertices
        min_d[start_node] = 0
        spt_vertices = [False] * vertices

        for node in range(vertices):
            min_i = self.minimum_distance(min_d, spt_vertices, vertices)
            if min_i == -1:
                continue
            spt_vertices[min_i] = True
            for v, d in self.successors_nodes(min_i):
                if d > 0 and not spt_vertices[v] and min_d[v] > min_d[min_i] + d:
                    min_d[v] = min_d[min_i] + d

        return min_d
"""
vertices = 6
edges = [[0, 1, 4], [0, 2, 2], [1, 3, 2], [1, 4, 3], [2, 1, 1], [2, 3, 2], [2, 4, 5], [4, 3, 1], [5, 2, 2]]
d=Dijkstra()
print(d.shortestDistance(edges,vertices))
"""


