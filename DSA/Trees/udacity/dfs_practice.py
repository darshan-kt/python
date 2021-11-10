
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
    def __repr__(self):
        return f"Node({self.get_value()})"

    # def __str__(self):
    #     return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root
    
    
def pre_order(tree):
    
    visit_order = list()
    root = tree.get_root() 
  
    def traverse(node):
  
        if node:          #node should be present                  root,left,right
            
            #visit
            visit_order.append(node.get_value())
            if node.has_left_child():
                # traverse left 
                traverse(node.get_left_child())

            if node.has_right_child():
                #traverse right
                traverse(node.get_right_child())
      
    traverse(root)     #1st iteration
    
    return visit_order



def in_order(tree):               # left, root, right
    
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # visit node
            visit_order.append(node.get_value())
            
            # traverse right sub-tree
            traverse(node.get_right_child())
    
    traverse(root)
    
    return visit_order



def post_order(tree):       # left, right, root
    
    visit_order = list()
    root = tree.get_root()
    
    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())
            
            # traverse right subtree
            traverse(node.get_right_child())
            
            # visit node
            visit_order.append(node.get_value())
    
    traverse(root)
    
    return visit_order
    
    
    
#%% Testing
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_left_child().set_right_child(Node("orange"))
tree.get_root().get_left_child().get_left_child().set_left_child(Node("grapes"))
tree.get_root().get_left_child().get_left_child().set_right_child(Node("mango"))
test1 = pre_order(tree)
test2 = in_order(tree)
test3 = post_order(tree)
print("pre-order", test1)
print("in-order", test2)
print("post-order", test3)

'''
                         apple
                |                     |
              banana                cherry
         |          | 
      dates       orange
'''

# n0 = Node("apple")
# n1 = Node("banana")
# n2 = Node("dates")
# n3 = Node("orange")
# n4 = Node("cherry")
# n0.set_left_child(n1)
# print(n0.get_left_child())