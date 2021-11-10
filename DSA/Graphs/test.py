import math
a=0
s=1
d=2
f=3
g=4
h=5
values = [a,s,d,f,g,h]
dictn = { }
for node in values:
    dictn[node] = math.inf
    
# print(dictn)


#or     Compressed way representation

 
distance_dict = {node: math.inf for node in values}
# print(distance_dict)


mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
mylistSort = sorted(mylist, key = lambda x: x[1])  #Compares all the second element in list of mylist and based min values it will sort list of list. ie, 2nd list has 2 so it comes first, then 3rd list 2nd elemt is 5 so this list comes 2nd, and 1st list 2nd element as 8 so this list ocmes last
print(mylistSort)     #[[1, 2, 3], [2, 5, 6], [7, 8]]

mylistSort1 = sorted(mylist, key = lambda x: x[1])[0]
print(mylistSort1)      #Considers very first list from sorted list ie, [1, 2, 3]

# print(sorted(dictn.items()), key=lambda x:x[1])
# j, k = sorted(dictn.items(), key=lambda x: x[1])[0]
# print(j, k)

# darshan = 2000
disn = {'darshan': 18}
print(disn.pop('darshan'))   #returns value of key