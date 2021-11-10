'''
Implementation approach
Args - custom list/array
s1:   for loop 1. Get the current ith element and assign as min_index
s2:   for loop 2. Check the condition to find element compare to current remaining element in array from i+1th index to last index. THen assign min element index as min_index variable
s3:   Do swap elements outside the second for loop
return - sorted list
'''

def selectionSort(cList):   
    
    for i in range(len(cList)):          #0,1,2,3...
        
        min_index = i
        
        for j in range(i+1, len(cList)):
            
            if cList[min_index] > cList[j]:     #current element > than the remaining jth element within the list(ie, jth element is less than current element so do  swap with jth element)
                
                min_index = j           # Assing jth element index to min_index variable
                
        cList[i], cList[min_index] = cList[min_index], cList[i]
        
    return cList

customList = [4,5,6,2,3,8,1,9,7]
sort = selectionSort(customList)
print(sort)