class Bipartiteness:
   
    def bipartite(self, edges, vertices):
        if vertices == 0 or vertices == 1:
            return 1
        self.graph = {x : [] for x in range(vertices)}
        self.add_edges(edges)
        return self.breadth_first_search(vertices)

    def add_edges(self, edges):
        for node1, node2 in edges:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
    
    def successor(self, node):
        return self.graph[node]

    def breadth_first_search(self, vertices):
        color = [-1 for x in range(vertices)]
        queue = []
        for i in range(vertices):
            if color[i] == -1:
                queue.append((i, 0))
                color[i] = 0

                while queue:
                    node, c = queue.pop(0)
                    for succ in self.graph[node]:
                        if color[succ] == c:
                            return -1
                        if color[succ] == -1:
                            color[succ] = 1 - c
                            queue.append((succ, color[succ]))
        return 1

"""  
b=Bipartiteness()
vertices = 7
edges = [[0, 6], [1, 6], [1, 2], [5, 6], [3, 2], [3, 4]]
print(b.bipartite(edges,vertices))
"""