#Question is find the height of tree
class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left_child = left

    def set_right_child(self, right):
        self.right_child = right

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"


#Changing the tree class w.r.t BST
class Tree():
    def __init__(self):
        self.root = None    #Define root as None


    def set_root(self, value):      #Call set_root method to initialize root or parent node
        self.root = Node(value)

    def get_root(self):         #Simillar to previous to get root of tree
        return self.root

    '''
    Insert function
    '''
    def insert(self, value):
        
        node = self.root   #Get the parent/root node
        
        if node == None:
           
            self.set_root(value)

        else: # if root node is already present then start insertion with root and new_node
            return self.insert_recur(node, Node(value))     


    #Insert recursive function
    def insert_recur(self, node, new_node):

        if  new_node.get_value() == node.get_value():
           
            node = new_node

        elif new_node.get_value() < node.get_value():    #towards left
          
            if node.has_left_child():
                
                self.insert_recur(node.get_left_child(), new_node)

            else:   
                node.set_left_child(new_node)

        else:                        #towards right
            if node.has_right_child():
                self.insert_recur(node.get_right_child(), new_node)

            else:
                node.set_right_child(new_node)
                
   
    # #Height of tree          #Mug up this solution   
    def height(self, root):
        
        if root is None:
            return -1
        
        return max(self.height(root.left_child), self.height(root.right_child)) + 1


    
tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(1)
tree.insert(0)
tree.insert(2)
tree.insert(5)
print(tree.height(tree.root))
