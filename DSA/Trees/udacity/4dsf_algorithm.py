import timeit

# #Node class
class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def get_left_child(self):
        return self.left_child
    
    def set_left_child(self, node):
        self.left_child = node
        
    def get_right_child(self):
        return self.right_child
    
    def set_right_child(self, node):
        self.right_child = node
        
    def has_left_child(self):
        return self.left_child != None

    def has_right_child(self):
        return self.right_child != None
        
    # def __repr__(self):
    #     return f"{self.get_value()}"              #This will print o/p in just value format: [apple, banana, cherry, dates, orange, grapes, mango]    
    
    
# Tree class
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    
    
#dfs pre_order

def pre_order(tree):                        # ROOT, LEFT, RIGHT   (traverse order)
    #Create visit_order empty list
    visit_order = list()
    #Get root node
    root = tree.get_root() 
    
    #defining traverse recursive function
    def traverse(node):
        if node is not None:
            
            # Append node to visit_order
            visit_order.append(node.get_value())
            
            # tranverse left
            if node.has_left_child():
                traverse(node.get_left_child())
            
            # traverse right
            if node.has_right_child():
                traverse(node.get_right_child())

    # First tranverse root node
    traverse(root)
    
    return visit_order



# DFS In-order
def in_order(tree):              # LEFT, ROOT, RIGHT
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if Node is not None:
            
            if node.has_left_child():        #left
                traverse(node.get_left_child())
                
            visit_order.append(node.get_value())    #root/node
            
            if node.has_right_child():           #right
                traverse(node.get_right_child())
    
    traverse(root)
    return visit_order


#DFS Post-Order
def post_order(tree):            #LEFT, RIGHT, ROOT
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            
            if node.has_left_child():             #LEFT
                traverse(node.get_left_child())
                
            if node.has_right_child():            #RIGHT
                traverse(node.get_right_child())
                
            visit_order.append(node.get_value())   #Root/node                  
    
    traverse(root)
    return visit_order




tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_left_child().set_right_child(Node("orange"))
tree.get_root().get_left_child().get_left_child().set_left_child(Node("grapes"))
tree.get_root().get_left_child().get_left_child().set_right_child(Node("mango"))
# test1 = pre_order(tree)
start = timeit.default_timer()
test1 = pre_order(tree)
stop = timeit.default_timer()
print('Time: ', stop - start)

# test2 = in_order(tree)
# test3 = post_order(tree)
# print("pre-order", test1)
# print("In-oreder", test2)
# print("Post-order", test3)


'''
                         apple
                |                     |
              banana                cherry
         |          | 
      dates       orange
'''