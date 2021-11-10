
def minPlatform(a, b):
    
    arr_time = sorted(a)
    dep_time = sorted(b)
    
    n = len(arr_time)    #number of trains
    
    i = 0   #arrival time index
    j = 0   #departure time index
    
    A = []
    
    while i < n and j < n:
        
        if arr_time[i] <= dep_time[j]:       #need a platoform
            A.append(1)          
            i += 1            #Move to next train(because we are not having platform for this train arrail timings)
             
        else:                             #no need of platforms
            A.append(-1)
            j += 1
            
            
    #Find cumulative sum
    sum = 0
    for k in range(len(A)):
        sum = sum + A[k]
        
        #Update A array as sum value at that instant
        A[k] = sum
        
    minPlatforms = max(A)
    return minPlatforms
        
            


if __name__ == '__main__':

    arr_time = [900, 940, 950, 1100, 1500, 1800]
    dep_time = [910, 1120, 1130, 1200, 1900, 2000]
    
    result = minPlatform(arr_time, dep_time)
    
    print(result)