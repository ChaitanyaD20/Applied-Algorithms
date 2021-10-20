class BreadthFirstSearch:

    def breadthFirstSearch(self, edges, vertices):

        self.graph = {i: [] for i in range(vertices)}
        
        for n1, n2 in edges:

            self.add(n1, n2)
        return self.breadth_First_Search_helper(vertices)

    def add(self, node1, node2):
        self.graph[node1].append(node2)

    def successor(self, n):
        return self.graph[n]

    def breadth_First_Search_helper(self, vertices):
        if vertices == 0:
            return []

        visited = [False] * vertices
        output = [-1] * vertices
        parent = [x for x in range(vertices)]
        queue = []
        queue.append(0)
        visited[0] = True
        output[0] = 0
        while queue:
            current_node = queue.pop(0)
            for node in self.successor(current_node):
                if not visited[node]:
                    visited[node] = True
                    parent[node] = current_node
                    output[node] = output[parent[node]] + 1
                    queue.append(node)

        return output

"""
b=BreadthFirstSearch()
edges=[[0,1],[0,3],[1,2],[1,3],[2,4],[2,5],[3,6],[3,7]]
vertices=8
print(b.breadthFirstSearch(edges,vertices))
"""