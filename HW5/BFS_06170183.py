from collections import defaultdict 

class Graph:
 def __init__(self): 
        self.graph = defaultdict(list)
        
 def addEdge(self,u,v): 
        self.graph[u].append(v)
          
 def BFS(self, s):
        if s in self.graph:
            queue=[]
            go=[]
            queue.append(s)
            go.append(s)
            while queue:
                path=queue.pop(0)                
                for i in self.graph[path]:
                  if i  not in go:                     
                      queue.append(i)
                      go.append(i)
                      
            return go
        else:
            print("no way")

 def DFS(self, s):
   if s in self.graph:
     stack=[]
     go=[]
     stack.append(s)
     while stack:
         path=stack.pop(-1)
         go.append(path)
         for i in self.graph[path]:
             if i not in go:
                 stack.append(i)          
     return go
   else:
       print("no way")
