from queue import Queue

class Graph:
    def __init__(self, num_of_nodes, directed):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
		
        self.m_directed = directed
		
        self.m_adj_list = {node: set() for node in self.m_nodes}      
	
    def add_edge(self, node1, node2):
        self.m_adj_list[node1].add(node2)

        if self.m_directed == 'False':
            self.m_adj_list[node2].add(node1)
        
    def bfs(self, start, target):
        visited = set()
        queue = Queue()
        queue.put(start)
        visited.add(start)
        
        parent = dict()
        parent[start] = None

        path_found = False
        while not queue.empty():
            current_node = queue.get()
            if current_node == target:
                path_found = True
                break

            for next_node in self.m_adj_list[current_node]:
                if next_node not in visited:
                    queue.put(next_node)
                    parent[next_node] = current_node
                    visited.add(next_node)
                    
        path = []
        if path_found:
            path.append(target)
            while parent[target] is not None:
                path.append(parent[target]) 
                target = parent[target]
            path.reverse()
        return path

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
path = graph.bfs(start, target)
if len(path)==0:
    print('path not found')
else:
    print('path found')
    print('path is',path)