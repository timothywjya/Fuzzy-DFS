graph = {'A' : {'I':3, 'D':5},
         'B' : {'F':4},
         'C' : {'H':5, 'A':4},
         'D' : {'B':5, 'G':16},
         'E' : {'F':3},
         'F' : {'H':13, 'G':2},
         'G' : {'E':2, 'F':4, 'D':10},
         'H' : {'F':15},
         'I' : {'C':5, 'H':9, 'D':3},
        }

def dijkstra(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity    = 999999999999
    path        = []
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
                
        for childNode, weight in graph [minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
            
    currentNode = goal
    
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
            
        except KeyError:
            print("Path not reachable")
            break

    path.insert(0,start)
    
    if shortest_distance[goal] != infinity:
        print("Jarak terdekatnya adalah "+str(shortest_distance[goal]))
        print("Jalur yang dilalui adalah "+str(path))
        
dijkstra(graph, 'B','A')