from collections import deque

class TopologicalSort:
        
    def topoSort(self, pre_requisites: [[int]], total_courses: int) -> [int]:    
        
        incoming_edges={}
        outgoing_edge_count={}

        #Incoming edges lists out the edges that are directed towards itself, and outgoing_edge_count will count the number of outgoing edges a node has.
        for i in range(total_courses):
            incoming_edges[i]=[]
            outgoing_edge_count[i]=0

        
        for i, j in pre_requisites:
            incoming_edges[j].append(i)
            outgoing_edge_count[i] += 1

        #Atleast one node should have 0 outgoing edges, so we use deque to find out all the incoming edges towards init using deque. We store the init on stack.
        #Once we find those, we reduce the outgoing edge count of its incoming nodes, and repeat the operation with another node whose outgoing egde count is 0.

        init = [node for node in incoming_edges if outgoing_edge_count[node] == 0]

        queue = deque(init)

        stack = []
        while queue:

            current = queue.popleft()
            stack.append(current)
            
            for edge in incoming_edges[current]:
                outgoing_edge_count[edge] -= 1
            
                if outgoing_edge_count[edge] == 0:
                    queue.append(edge)
        
        topological_sort_list=[]

        #From stack we pop out all the elements to give the correct Topological sort order.
        for i in range(len(stack)):
            topological_sort_list.append(stack[len(stack)-i-1])
  
        return topological_sort_list

