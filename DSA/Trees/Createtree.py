

class TreeNode:        #Crating tree class
    def __init__(self, data, children = []):     #Intialize each node with 2 params. ie, node data and linked subNode lists(child list)
        self.data = data
        self.children = children
        
        
    def __str__(self, level=0):                   #Printing purpose
        ret = " "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):                 #Method to add children to specific node
        self.children.append(TreeNode)
        
tree = TreeNode('Drinks', [])           #Creating a node object using initializer step
cold = TreeNode("cold", [])             #Creating cold node object
hot = TreeNode('hot', [])               #Creating hot node object
tree.addChild(cold)                     #Adding the created node object to another node object using addchild MF. ie, tree node object will become parent node and cold object becomes child node 
tree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)


