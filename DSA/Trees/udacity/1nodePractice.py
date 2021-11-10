
class Node(object):                           #Defining a class based on new style guides. it supports in python3. ie, defining a class as subclass for object class or defing class as inherit with object
    def __init__(self, value= None):      # Each node contains 3 variables ie, value, left child and right child. Each variable contains 2 MFs, one for getting data and one for setting data
        self.value = value
        self.left_child = None         #THis can be added using DF/methods    
        self.right_child = None



# Defining fuctions for get and set value
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
# Defining functions for get and set left child node
    def get_left_child(self):
        return self.left_child
    
    def set_left_child(self, node):
        self.left_child = node       
        
# Defining functions for get and set right child node
    def get_right_child(self):
        return self.right_child
    
    def set_right_child(self, node):
        self.right_child = node 
    
# Defining functions to check left and right child exit or not
    def has_left_child(self):
        return self.left_child is not None
    
    def has_right_child(self):
        return self.right_child is not None
    
             #OR
    # def has_left_child(self):
    #     if self.left_child != None:
    #         return True
    #     else:
    #         return False
        
    # def has_right_child(self):
    #     if self.right_child != None:
    #         return True
    #     else:
    #         return False


    # define __repr_ to decide what a print statement displays for a Node object     (Very important funtion to display print statement, without this print statement will not work)
    def __repr__(self):                                 #This function is using because we are using node as Node(value) format
        return f"Node({self.get_value()})"         
  
'''
             apple
     banana           cherry
dates    orange

'''

'''
Node inspection

# root = Node("apple")
# n1 = Node("banana")
# n2 = Node("dates")
# n3 = Node("orange")
# n4 = Node("cherry")

# if not root.has_left_child():
#     root.set_left_child(n1)
#     print(root.get_left_child())            #prints the node     ie, Node(banana)
#     print(root.get_left_child().get_value())    #prints the node value  ie, banana
    
# if not root.has_right_child():
#     root.set_right_child(n2)
#     print(root.get_right_child())
#     print(root.get_right_child().get_value())    
'''


class Tree(object):
    def __init__(self, value = None):            #THis will initializes the root of tree just by accepting value. That value will be added with Node(value) ie, inheritance concept
        self.root = Node(value)                 #Assinging root node in the format of Node class. ie, Node(value)
        
    def get_root(self):              #Only one MF that returns root
        return self.root
    
    
tree = Tree("apple")                                 #Only for adding root node
print(tree.get_root())                               #root node
print(tree.get_root().get_value())                   #prints root node value
tree.get_root().set_left_child(Node("banana"))       #Adding Node at left or root. ie, Node should be add with this format Node(value)
print(tree.get_root().get_left_child())              #prints left node
print(tree.get_root().get_left_child().get_value())  #prints left node value