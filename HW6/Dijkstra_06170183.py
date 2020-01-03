from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def addEdge(self,u,v,w):
        """
        :type u,v,w: int
        :rtype: None
        """

    def Dijkstra(self, s):
      n = len(s)
      visited = [s]
      costs[start] = 0
      costs = []
      parents = dict()
      t=[]
      min = 1
      minNode = None
      for i in range(n):
            if not visited[i] and costs[i] < minCost:
                min = costs[i]
                minNode = i
                t.append(minNode)
                visited[minNode] = True
                
       
        

            for edge in graph[minNode]:
             if not visited[edge[0]] and min + edge[1] < costs[edge[0]]:
                costs[edge[0]] = min + edge[1]
                parents[edge[0]] = minNode
                return costs, parents
        

    def Kruskal(self):
             """
            :rtype: dict
            """
            

