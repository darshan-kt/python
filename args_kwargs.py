# the below function wil accept only 2 parameter for this function and assign their value to a&b
'''
def my_fun(a,b):
    return sum((a,b))
'''
#  *args is a data structure, it will accepts n number of parameters for function and return tuples
'''
def my_fun(*args):
    return(sum(args))
print(my_fun(1,2,3,4,5))
'''

#  **kwargs are another kind of data structure, stores n number of dictionary inside it and return back Dictionarys
'''
def my_fun(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}". format(kwargs['fruit']))
print(my_fun(fruit='apple'))
'''

def myfun(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I will buy {} {}" .format(args[0], kwargs['food']))
    
print(myfun(10,20,30, fruit='banana', food='egg rice'))
