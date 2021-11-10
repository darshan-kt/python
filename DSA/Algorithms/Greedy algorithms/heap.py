import heapq 

'''
    heapify − This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. 
               But rest of the data elements are not necessarily sorted.

    heappush − This function adds an element to the heap without altering the current heap.

    heappop − This function returns the smallest data element from the heap.

    heapreplace − This function replaces the smallest data element with a new value supplied in the function.

'''


H = [4,5,6,7,5]
a = heapq.heappop(H)
heapq.heappop(H)
print(H, a)
heapq.heappush(H,9)
print(H)



#Use heapify to rearrange the elements 
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H,5)
print(H)

# Remove first element
heapq.heappop(H)
print(H)

# Add and remove same element
heapq.heappushpop(H, 3)
print(H)



# Replace an element
# newHeap = heapq.heapreplace(H,6)
# print(newHeap)

# heapq.heapify(H)
# print("Final heapify based on min heap", H)