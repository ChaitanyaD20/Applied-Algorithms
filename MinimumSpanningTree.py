class MinimumSpanningTree:
    def mst(self, edges: [[int]], vertices: int) -> int:
        self.graph = []
        self.add_edges(edges)
        return self.kruskals(vertices)

    def add_edges(self, edges):
        for node1, node2, weight in edges:
            self.graph.append([node1, node2, weight])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, left, right):
        left_root = self.find(parent, left)
        right_root = self.find(parent, right)
        if rank[left_root] < rank[right_root]:
            parent[left_root] = right_root
        elif rank[left_root] > rank[right_root]:
            parent[right_root] = left_root
        else:
            parent[right_root] = left_root
            rank[left_root] += 1
    
    def kruskals(self, vertices):
        mst = 0
        sorted_index = 0
        index = 0
        self.graph = sorted(self.graph, key = lambda x: x[2])
        parent = []
        rank = []

        for node in range(vertices):
            parent.append(node)
            rank.append(0)

        while index < vertices - 1:
            node1, node2, weight = self.graph[sorted_index]
            sorted_index += 1
            left = self.find(parent, node1)
            right = self.find(parent, node2)
            if left != right:
                index += 1
                mst += weight
                self.union(parent, rank, left, right)
        return mst

"""
m=MinimumSpanningTree()
edges = [[0, 1, 3], [1, 2, 1], [2, 0, 2]]
vertices = 3
print(m.mst(edges,vertices))
"""