#Question is find the searching element present in the tree and what is least path travel to reach that
class Node(object):
    
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    # def __repr__(self):
    #     return f"Node({self.get_value()})"



#Changing the tree class w.r.t BST
class Tree():
    def __init__(self):
        self.root = None    #Define root as None
        self.path = []        #This adding to find the traverse path to reach search value


    def set_root(self, value):      #Call set_root method to initialize root or parent node
        self.root = Node(value)

    def get_root(self):         #Simillar to previous to get root of tree
        return self.root

    """
    Rules for BST:
    1. Every node at most have 2 nodes
    2. The left node should be smaller than the parent node
    3. The right node should be greater than the parent node

    Write a comparision function which compares the 2 nodes ie, parent and new_node. This will species where to add node ie, either left or right 
    If incase new_node value equal to parent_node value, u can design the system in 3 ways
    1. Overide the duplicates
    2. Keep a counter to count how many time same node value node add
    3. Keep a list to add same node value. 

    """

    '''
    Insert function
    '''
    def insert(self, value):
        
        node = self.root   #Get the parent/root node
        #Checks for node
        if node == None:
            # set root node using value. This will set the root node as Node(value)
            self.set_root(value)

        else: # if root node is already present then start insertion with root and new_node
            return self.insert_recur(node, Node(value))     #write the new_node in Node(value) format 


    #Insert recursive function
    def insert_recur(self, node, new_node):

        if new_node.get_value() == node.get_value():
            # node.set_value(new_node.get_value())  #Set the same value to node
            node = new_node

        elif new_node.get_value() < node.get_value():    #towards left
            #Check left node is present
            if node.has_left_child():
                #start recusion with using present left_node and new node. This will again checks comparision and repeat 3 if, elif, else conditons
                self.insert_recur(node.get_left_child(), new_node)

            else:   #no node at left so directly set as left child
                node.set_left_child(new_node)

        else:                        #towards right
            if node.has_right_child():
                self.insert_recur(node.get_right_child(), new_node)

            else:
                node.set_right_child(new_node)
                
                
    """
    Implement search
    """
    def search(self, value):
        node = self.root
        
        if node == None:
            return None
        
        else:
            return self.search_recur(node, Node(value))
        
        
    def search_recur(self, node, new_node):
        
        if new_node.get_value() == node.get_value():
            self.path.append(node.get_value())
            return True
        
        elif new_node.get_value() < node.get_value():
            if node.has_left_child():
                self.path.append(node.get_value())
                return self.search_recur(node.get_left_child(), new_node)     #After did recursion, if node present, left_node == new_node so execute above comparision == 0 statement and returns True
            
            else:
                self.path = []
                return False  
            
        else:
            if node.has_right_child():
                self.path.append(node.get_value())
                return self.search_recur(node.get_right_child(), new_node)
            else:
                self.path = []       #If incase node was not present then return empty list
                return False


tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(1)
tree.insert(0)
# tree.insert(6)
# print(tree)                             #Tried to certain functions to print tree, but it doesn't works for me.( I tried __repr__ fucntion in tree class)
# print(tree.search(9))
print(tree.search(0))
print(tree.path)       #prints the list which travels from root to search node 