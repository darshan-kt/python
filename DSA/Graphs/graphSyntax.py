'''
Trees are special kind of graph DS. So the syntax used for tree can also simillar to Graph. 
ie, First have to create Node class and then have to create Graph class.
In Node class, 2 DMs(value, children) and 2 MFs(add_child, remove_child)

In Graph class, 1 DM(nodes to store all nodeslist) and 2 MFs(add_edge, remove_edge)
'''

class Node(object):
    # Simillar to Tree graphNode will have 2 variables. Node value and childrens. Here children may be plenty so create a empty list for storing all.
    def __init__(self, value):
        self.value = value
        self.children = []

    # Simillar to set value, here define add_child function to add new_node into children
    def add_child(self, new_node):
        self.children.append(new_node)

    # Remove/Delete node from children list
    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)
            
    # For printing
    def __repr__(self):
        return f"{self.value}"

#Graph class
class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)


    def remove_edge(self, node1, node2):
        if (node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)


'''
Graph: Unweighted-undirected graph

        S -- G -- A
           /   \    \
          /     \    \
         R  --   H -- P

'''


#Node objects
nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')


#Graph object
graph1 = Graph([nodeG, nodeR, nodeA, nodeP, nodeH, nodeS])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeR,nodeH)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeP,nodeA)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeS,nodeG)

#Check the children nodes for nodeA
# for i in nodeA.children:      #Use for loop because we are using list format for children
#     print(i, end=" ")
    
#Check for children node for all node
for node in graph1.nodes:
    print("Parent node", node)
    print("Children nodes")
    for child in node.children:
        print( child, end=" ")
    print("\n")