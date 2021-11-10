#   Created by Elshad Karimov on 15/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Question 1  [Find missing element in a list]

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

check = [1,2,3,4,5,7,8,9,10]           
def findMissing(list, n):
    sum1 = sum(list)
    sum2 = 10*11/2                                # Maths formala(sum of n series) : 1+2+3+......n = n(n+1)/2   Ex: 1+2+..+6   Here n is 6
    print(sum2-sum1)                    #Formula for missing element calculation: (sum of n series) - (sum of list elements) = Missing element

# findMissing(check, 10)
# findMissing(mylist, 100)



# Question 2   [Write a program to find all pair of integers whose sum is equal to given number]  
checkList = [1,2,3,4,5,4,6,7,8] 
targetSum = 8 
def findPairs(list, sum):
    for i in range(len(list)):             #take 1st element as i
        for j in range(i+1,len(list)):     #take each element in betn 2nd element to last element as j and add with i (i.e, i+j)
            
            if list[i] == list[j]:         #if i and j both same then skip those number adding process (Ask this question for interviwer like what if pair of numbers are same?)
                continue
            elif (list[i]+list[j]) == sum:     #if i+j is equal to targetsum, print those numbers
                print(list[i],list[j])
# findPairs(checkList, targetSum)


# # Question 3       [How to check/search the array which contains given number in python using numpy module] or linnear serach in array
import numpy as np 
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print("The given number is present in an array at index position " + str(i))

# findNumber(myArray, 12)



# # Question 4    [How to find maximum product of 2 integers in the array where all the elements are positive]

def findMaxProduct(array):
    maxProduct = 0                     #Create a variable to assign maxProduct value after iteration complition(since as menstion +ve integer take 0 as initial)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > maxProduct:     #If the product is greater than the previous pairs of maxproduct then assign this pairs product as maxProduct 
                maxProduct = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(maxProduct)

# findMaxProduct(myArray)



# #Question 5 - isqunieuq  [Implement algorithm to determine the given list conatains unique characters? (Not repeated characters)]
myList = [1,2,3,4,5,6,7,4,9]

def isUnique(list):
  a=[]             #Creating a new empty list (1)
  for i in list:
    if i in a:     #Check the element which is going to adding is already present in new list  (3)
        print(i)
        return False
    else:
        a.append(i)        #to add all elements into empty list  (2)
  return True

# print(isUnique(myList))



# #Question 6 - permutation       [Find elements in both given list are same(permentation) or not]

def permuntation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:   
        return True
    else:
        return False

# print(permuntation([1,2,3], [3,1,2]))


# # Question 7
import numpy as np
def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)                             #len(matrix) = no. of rows = 3
    for layer in range(n // 2):                # n//2 = 3//2 = 1   and range(1) = 0 = layer
        
        first, last = layer, n - layer - 1        #first = 0 last = 2
        for i in range(first, last):         #1st iteration 0 2nd iteration 1
            # save top
            top = matrix[layer][i]     # =1

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]      #replace 1(matrix[0][0]) by 7(matrix[-1][0])

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]   #replace 7(matrix[-1][0]) by 9(matrix[-1][-1])

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]   #replace 9(matrix[-1][-1]) by 3(matrix[0][-1])

            # top -> right
            matrix[i][- layer - 1] = top         #replace 3(matrix[0][-1]) by 1(matrix[0][0])
    return matrix

myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(myArray)
# print(rotate_matrix(myArray))




##########PATTERNS****************

# n = int(input("Enter the number of rows: "))

def numPattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")    #end=" "  breaks elements with space
        print()         #newline

# numPattern(4)
'''
1
1 2
1 2 3
1 2 3 4
'''

def numPattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end=" ")    #end=" "  breaks elements with space
        print()         #newline
        
# numPattern(5)
'''
1
2 2
3 3 3
4 4 4 4
'''