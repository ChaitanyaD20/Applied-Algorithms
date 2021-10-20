class CriticalLink:
    
    def criticalLink(self, n : int, links : [[int]]) -> int:

        self.graph = {x : [] for x in range(n)}
        self.Time = 0
        self.critical_links = 0

        for node1, node2 in links:
            self.add_edge(node1, node2)

        visited_node = [False] * n
        disc = [float("Inf")] * n
        low = [float("Inf")] * n
        parent_node = [-1] * n

        for i in range(n):
            if visited_node[i] == False:
                self.dfs_helper_function(i, visited_node, parent_node, low, disc)
        
        return self.critical_links
    
    def add_edge(self, node1, node2):

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def dfs_helper_function(self, next_vertex, visited_node, parent_node, low, disc):

        visited_node[next_vertex] = True
        disc[next_vertex] = self.Time
        low[next_vertex] = self.Time
        self.Time += 1

        for v in self.graph[next_vertex]:

            if visited_node[v] == False:
                parent_node[v] = next_vertex
                self.dfs_helper_function(v, visited_node, parent_node, low, disc)
                low[next_vertex] = min(low[next_vertex],  low[v])
            
                if low[v] > disc[next_vertex]:
                    self.critical_links += 1
            
            elif v != parent_node[next_vertex]:
                low[next_vertex] = min(low[next_vertex], disc[v])

"""
c=CriticalLink()
links=[[0,1],[1,2],[2,0],[1,3]]
print(c.criticalLink(4,links))
"""        