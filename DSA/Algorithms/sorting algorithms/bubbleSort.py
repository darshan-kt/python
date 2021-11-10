'''
Implementation approach
Args - custom list/array
s1:   2 nested for loops.
s2:   Compare ajacent pairs
s3:   Do swap elements
return - sorted list
'''

def bubbleSort(customList):

    for i in range(len(customList)-1):

        for j in range(len(customList)-i-1):

            if customList[j] > customList[j+1]:             #Use (>) for ascending order, use(<) for decending order
                print(customList[j], customList[j+1])

                customList[j], customList[j+1] = customList[j+1], customList[j]

    return customList


cList = [2,3,1,5,4,8,7]
sort = bubbleSort(cList)
print(sort)

