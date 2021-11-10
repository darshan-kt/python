

'''
Find max profit with min cost using Greedy(local optimal soln at each step lead global optimal solution) approach.

I/P:
objs    obj1  obj2  obj3
profit   25    24    15
weight   18    15    10

capacity 20kg

output: maximum profit ?

Logic: 
find p/w ratio
sort in decreasing order
write adding logic

'''

profit = [25, 24, 15]
weight = [18, 15, 10]
p_w_ratio = []
capacity = 20
max_profit = 0


#Finding find p/w ratio
for idx in range(len(profit)):
    
    # p_w_ratio.append(profit[idx]/weight[idx])
    p_w_ratio.append([profit[idx]/weight[idx], idx])        #VIP logic   keep index as second variable and p/w as first variable, so can easily sort list based on p/w ratio  
   

#sort in decreasing order
in_ratio = sorted(p_w_ratio)   #to get increasing order
de_ratio = in_ratio[::-1]         #reverse list to get decreasing order


for maxP_W, idx in de_ratio:
    # print(maxP_W, idx)

    index = idx    #index corresponds to profit and weight list order
    
    if  capacity >= weight[index]: 
        max_profit = max_profit + profit[index]
        
    if capacity > 0 and weight[index] >= capacity:
        max_profit = max_profit + (capacity/weight[index]) * profit[index]      #Formula: profit = capacity_left / weight * profit
        
    if capacity == 0:
        break
        
    capacity = capacity - weight[index]          #Substract capacity value after conditions other it will for preceding(down the order) conditions
    
    
          
print(max_profit)


        
        
