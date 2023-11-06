class Graph:
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
        self.m_directed = directed
		
        self.m_adj_list = {node: set() for node in self.m_nodes}   

    def add_edge(self, node1, node2):
        self.m_adj_list[node1].add(node2)

        if self.m_directed=='False':
            self.m_adj_list[node2].add(node1)
            
    def dfs(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        # print(path,visited)
        if start == target:
            return path
        for neighbour in self.m_adj_list[start]:
            # print(self.m_adj_list[start])
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None    
n= int(input('enter no.of nodes : '))
directed = input('Is the graph directed : ')
graph = Graph(n, directed)
x = int(input('no.of edges : '))
print('enter edges one after one')
while True:
    a,b = map(int,input().split())
    if a==-1 and b==-1:
        break
    graph.add_edge(a,b)
start, target = map(int,input('enter start and target nodes : ').split())
path = []
path = graph.dfs(start, target, path=[], visited=set())
if path==None:
    print('path not found')
else:
    print('path found')
    print('path is',path)
