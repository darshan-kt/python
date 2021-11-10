'''
Merge sort:
Merge sort is a divide and conquer algorithm that divides a list into equal halves until it has two single elements 
and merges the sub-lists untill the entire list has been reassembled in order.

Follows 2 Steps:
1. Divide: If we have more than 1 element in a list we need to split the list into equal halves by creating mergesort function. 
   Continue this process untill to get single element in list, then this list considered as sorted and return imediately.

2. Conquer: Once have split the list down into single elements, pass those elements into merge function, it will reassembled the entire list in order.


Designing the sytax:
def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    # left =
    # right =

    # Call mergesort recursively with the left and right half
    left = mergesort(left)        
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.

'''

def mergesort(items):

    if len(items) <= 1:
        return items

    #Calculate mid index for slipting 
    mid = len(items) // 2

    # Creating left and right lists to store splitted items
    left = items[:mid]
    right = items[mid:]

    #Splitting again by calling same function recusively untill get single element in list. The len(items) <= 1 condition will returns final splitted element and that will store at end in below variables
    left = mergesort(left)     #Ex: left = [3,4,2,1]  --> [3,4], [2,1] --> [3],[4], [2],[1] this will be the final splitted elements after doing many recursion
    right = mergesort(right)

    return merge(left, right)       #Finally return statement call merge function by passing completely splited left and right lists 


def merge(left, right):
    merged = []     #create a merged list varible to add sorted elements into it.

    left_index = 0
    right_index = 0

    # Use index traverse approach. 
    # ie, tracking the index in both list untill one of list get exhusted, and appending the remaineded list items to merged list
    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] > right[right_index]:  #Ex: left = [5,3] right= [2,1].  left[0] ie, 5 > right[0] ie, 2
            merged.append(right[right_index])      #After append merged = [2]
            right_index += 1                       # right_index = 1  then main loop

        else:
            merged.append(left[left_index])
            left_index += 1

    #Finally add the remianing elements into merged list
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


cList = [5,1,2,4,8,9,55,33,11]
sort = mergesort(cList)
print(sort)