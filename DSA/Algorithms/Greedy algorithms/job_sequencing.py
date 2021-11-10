import numpy as np

'''
Find max profit by allocating jobs sequence based on deadline for completion using Greedy(local optimal soln at each step lead global optimal solution) approach.

I/P:
jobs        A    B     C     D    E
profit     100   19    27    25   15
deadline    2     2    1     1    3


output: maximum profit ?

Logic: 
Sort profit in decreasing order
Finding maximum deadline time
Initialize max profit job as first job at given deadline slot
Check other max profit jobs and compare with highest profit job deadline and add it in before/after slots 

'''

# DS have to maintained -> [profit, deadline, job]

data = [[100, 3, "A"], [19, 5, "B"], [27, 2, "C"], [25, 1, "D"], [25, 4, "E"] ]


#Sorting
data1 = sorted(data)  #sort
data2 = data1[::-1]   #reverse in decreasing order



# Finding maximum deadline time
deadlineList = []
for i in range(len(data)):
    deadlineList.append(data[i][1])
    
duration = max(deadlineList)


# Initialize first Job info. 
n = data2[0][1]                #maxProfit deadline
maxProfit = data2[0][0]
#Create an array to store order of jobs allocation
order = np.zeros(shape=duration, dtype=str)        #VIP   keep look on dtype param while creating array. Must and should keep "str"          
#Add first job allocating order
order[n-1] = data2[0][2]      #need add jobs in n-1 order because array in integer order but we use slots like 0-1 is 1st slot, 1-2 is 2nd slot, 2-3 is 3rd slot
# print(order.shape[0])



for i in range(1, len(data2)):
    
    slot = data2[i][1]
    job = data2[i][2]
    
    
    if slot <= n and order[0] == "":          #untill oth index array because full
        
        if order[slot - 1] == "":           #Current duration job slot should be empty
        
            maxProfit = maxProfit + data2[i][0]
            order[slot - 1] = job         #Allocating at 1 slot lower like n-1 in previous

      
        
    if slot >= n and order[order.shape[0] - 1] == "":      #untill order reaches its boundary
        
        if order[slot - 1] == "":
            
            maxProfit = maxProfit + data2[i][0]
            order[slot - 1] = job         #Allocating at 1 slot lower like n-1 in previous
        
        
        
print(order, maxProfit)
    
    
    
    
    
    

