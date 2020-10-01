#Python program to implement topological sorting of a DAG 
from collections import defaultdict 
  
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list)                  #dictionary containing adjacency List 
        self.V = vertices                               #No. of vertices 
  
    #  add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recursion for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print stack 
  
g= Graph(6) 
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 
  
print("Following is a Topological Sort of the given graph")
g.topologicalSort() 
