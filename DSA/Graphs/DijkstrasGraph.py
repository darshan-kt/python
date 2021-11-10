import math

'''
Youtube link: https://www.youtube.com/watch?v=U5W8-gGblXs

Graph Representation
In order to run Dijkstra's Algorithm, we'll need to add distance to each edge.
We'll use the GraphEdge class below to represent each edge between a node.
'''
# Here the difference is, in previous graphs Each node will be have value and are connected with edges without mentioning distances.
# In this graph node will have value. Connected with edges with distance value. ie, Here added child will have node and distace of edge


#Graph edge class
class GraphEdge:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
        
#Graph node class
class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []             #instead of children use edges. It will store node along with its distance
    
    
    #Adding child this will add child node along with distance on edges list    
    def add_child(self, new_node, distance):
        self.edges.append(GraphEdge(new_node, distance))
            
    def __repr__(self):
        return f"{self.value}"
        
            
    
    
#Graph class
class Graph:
    def __init__(self, node_list):
        self.nodes = node_list
        
    def add_edge(self, node1, node2, distance):
        if (node1 in self.nodes) and (node2 in self.nodes):
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)          
            
            
#Disjktra Algorithm         
def dijkstra(start_node, end_node):
    distance_dict = {node: math.inf for node in graph.nodes}  #For all nodes assign math.inf and store as key-value pairs in disctionary.  Look at test.py script 
    # Because all nodes have infinity as initail distance values (initially what the shortest distance is, let's put it as infinite.)
    # print(distance_dict)
    shortest_path_to_node = {}


    distance_dict[start_node] = 0   #Take the start_node from the disc and assing as 0 distance value
    while distance_dict:
        # Pop the shorest path
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]   #It will sort the all distance values of individual nodes in increment order, then choose the first node distace pair in distc
        # and assign that min distance as node_distance and min distance contained node as current node. ie, By using this figured out the least edge distance having node. Add that node into shortest_path_to_node
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)  #distance_dict.pop(current_node)  returns value stored in current_node key       
        # print(shortest_path_to_node[current_node])

        # print(shortest_path_to_node)
        for edge in current_node.edges:
            # print(edge)
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance

    return shortest_path_to_node[end_node]
            
            
'''
Write the graph on paper using add_edge information.
'''         
            
                  
    
        
node_u = Node('U')
node_d = Node('D')
node_a = Node('A')
node_c = Node('C')
node_i = Node('I')
node_t = Node('T')
node_y = Node('Y')



graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
# graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
# graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
# graph.add_edge(node_c, node_d, 4)
# graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
# graph.add_edge(node_i, node_a, 7)
# graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
# graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
# graph.add_edge(node_y, node_i, 4)
# graph.add_edge(node_y, node_t, 5)


print(dijkstra(node_u, node_y))

