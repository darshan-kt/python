def binary_search(array, target):

    while True:
        center_list = round(len(array)/2)    #get center element index

        if target == array[center_list]:
            return center_list, "Solution found"               #return index of solution 

        elif target < array[center_list]:
            array = array[:center_list]

        else:
            array = array[center_list:]

        if len(array) == 1:
            return -1,  "Solution not found"                       #return -1 if solutions not found


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
print(binary_search(array, target))