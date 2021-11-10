from collections import deque               #Must import deque form collections library

# Queue is a linnear DS organozed in FIFO
'''
# Queue DS 
q = deque()
q.appendleft('orange')
q.appendleft('grapes')
q.appendleft('onion')
q.pop()
print(q)         #o/p: deque(['onion', 'grapes'])
'''


# Queue DS with class
class Queue(object):

    def __init__(self):
        self.q = deque()          #Initialize deque class/method in constructor

    # Method for adding value/data to queue (like set_fun(self, vaue))
    def enq(self, value):
        self.q.appendleft(value)
        
    # Method for removing/poping value/data from queue  
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        
        else:
            return None
        
    def __repr__(self):       #Method for executing print statement
        return f"{self.q}"
    
    def len(self): 
        return len(self)
    
    
q = Queue()
q.enq('apple')
q.enq('banana')
q.deq()

print(q)       #deque(['banana'])

