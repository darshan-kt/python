from collections import deque
import timeit

#BFS or level order

#Node class
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
        if self.left_child != None:
            return True
        else:
            return False
        
    def has_right_child(self):
        if self.right_child != None:
            return True
        else:
            return False
        
    # def __repr__(self):
    #     return f"{self.get_value()}"              #This will print o/p in just value format: [apple, banana, cherry, dates, orange, grapes, mango]
        # return f"Node({self.get_value()})"      #This will print o/p in Node value format: [Node(apple), Node(banana), Node(cherry), Node(dates), Node(orange), Node(grapes), Node(mango)]
    
    
# Tree class
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    

# Queue class
class Queue(object):
    def __init__(self):
        self.q = deque()
        
    def enq(self, value):
        return self.q.appendleft(value)
    
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()   
        else:
            return None
    
    
#BFS algorithm syntax
def bfs(tree):
    # Define empty visit order list
    visit_order = []
    # Create a object for queue class
    q = Queue()
    # Get the root node
    node = tree.get_root()
    #Add root node into queue
    q.enq(node)
    # Delete the added root from queue and save that root/node as node variable
    node = q.deq()
    
    #Start looping
    while node is not None:          #Repeat looping untill node varible become None ie, removing all the elements from queue
        # Append node varible on visit_order list
        visit_order.append(node.get_value())       
        # Check/Get the left node and add into queue
        if node.has_left_child():
            q.enq(node.get_left_child())
            
        # Check/Get for right node and add into queue
        if node.has_right_child():
            q.enq(node.get_right_child())
            
        # Delete the first in node from queue and assign into node variable(ie, this assigned node varible back to loop and check for right and left node. At end Once tree reaches to left node, and that also deque from queue, the deq() method return None. Thats the end of loop)
        node = q.deq()
        
    return visit_order   #Once queue become empty 



tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))
tree.get_root().get_left_child().set_right_child(Node("orange"))
tree.get_root().get_left_child().get_left_child().set_left_child(Node("grapes"))
tree.get_root().get_left_child().get_left_child().set_right_child(Node("mango"))
start = timeit.default_timer()
result = bfs(tree)
stop = timeit.default_timer()
print('Time: ', stop - start)
print(result)              #o/p: [apple, banana, cherry, dates, orange, grapes, mango]

'''
                         apple
                |                     |
              banana                cherry
         |          | 
      dates       orange
'''