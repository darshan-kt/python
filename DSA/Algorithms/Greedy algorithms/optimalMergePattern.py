import heapq


def minComputation(n, files):
    
    H = files
    sum = 0
    
    Solution = 0
    
    while n > 1:
        # print(n)
        
        a = heapq.heappop(H)     # Remove first element from heap and store in a variable
        
        b = heapq.heappop(H)     # Remove first element from heap and store in b variable
        
        sum = a + b
        
        heapq.heappush(H, sum)   #Insert element into heap
        
        n -= 1             #Removed 2 elements and inserted 1 element ie, one element reduced at each iteration
        
        Solution = Solution + sum     #Adding optimal solution at each iteration
        
    return Solution
        
        

if __name__ == '__main__':
    
    # Files with their sizes
    files = [30, 10, 20]                     # [2,3,4,5,6,7]
    
    # sort in increasing order 
    files = sorted(files)

    # Number of file bunch
    n = len(files)
    
    result = minComputation(n, files)
    
    print("Optimal solution", result)


