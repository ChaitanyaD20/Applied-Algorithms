class StronglyConnectedComponents:

    def scc(self, students: int, knows: [[int]]) -> [[int]]:
        
        self.graph = {x : [] for x in range(students)}
        for node1, node2 in knows:
            self.addEdge(node1, node2, True)
        stack = []
        visited_ele = [False] * students
        for i in range(students):

            if visited_ele[i]==False:
                self.fillOrder(i, visited_ele, stack)
        self.temporary_list = []
        self.getTranspose(students)
        
        visited_ele =[False] * students
        result_list = []
        
        while stack:
            i = stack.pop()
            if visited_ele[i]==False:
                self.dFSUtility(i, visited_ele)
                result_list.append(self.temporary_list)
                self.temporary_list = []
        return result_list

    def addEdge(self, node1, node2, flag):
    	
        if flag:
            self.graph[node1].append(node2)
        else:
            self.transpose[node1].append(node2)

    def dFSUtility(self, node, visited_ele):

        visited_ele[node]= True
        self.temporary_list.append(node)
        for elem in self.transpose[node]:
            if visited_ele[elem]==False:
                self.dFSUtility(elem, visited_ele)
    
    def fillOrder(self, node, visited_ele, stack):
        
        visited_ele[node]= True
        for elem in self.graph[node]:
            if visited_ele[elem]==False:
                self.fillOrder(elem, visited_ele, stack)
        stack = stack.append(node)
      
    def getTranspose(self, students):
        
        self.transpose = {x : [] for x in range(students)}
        for i in self.graph:
            for j in self.graph[i]:
                self.addEdge(j, i, False)

"""
s=StronglyConnectedComponents()
print(s.scc(5,[[0, 1], [1, 2], [2, 0], [2, 3], [4, 3], [3, 4]]))
"""