class FamilyNode:        #Crating tree class
    def __init__(self, node, children=[]):   #Intialize each node with 2 params. ie, node data and linked subNode lists(child list)
        self.node = node
        self.children= children
        
    def __str__(self, level=0):
        ret = " "*level + str(self.node) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChildren(self, FamilyNode):     
        self.children.append(FamilyNode)      #adding children
            
root = FamilyNode("Ramegowda", [])
child1 = FamilyNode("Nanjundegowda", [])
child2 = FamilyNode("Thimmegowda", [])
root.addChildren(child1)
root.addChildren(child2)

grandChild1 = FamilyNode("Naveen", [])
grandChild2 = FamilyNode("Darshan", [])
grandChild3 = FamilyNode("Sudarshan", [])
child1.addChildren(grandChild1)
child2.addChildren(grandChild2)
child2.addChildren(grandChild3)

print(root)