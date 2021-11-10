def add(a,b):
    print (a+b)   # just prints the o/p on termianl and it will not stored anywhere
    return a+b    # this will returns the o/p to variable when used call this fun

sum = add(10,20)  # Because of using return keyward the o/p will stored into sum variable
sum = add('10', '20')  #o/p: '1020'  #python is dynamic datatype assigner it will assign the o/p datatype depending on input given

Functions with logic using list data structure
Check number in list and return true if any number is even
def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            return True
        else:
            pass                 #it will just pass block without returning any thing and makes the loop alive
    
print(check_even_list([1,2,3,4,5]))  # In the 1st iteration checks 1 & enters into else block because pass keyword again back to loop, then 2nd itern returns true because 2(1st value for even check condition) will if block and returns true and terminate the loop 
print(check_even_list([1,3,5]))      # returns None there is no even number to execute if block all are odd numbers and will pass the else block


# We are doing mistakes points
def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            print("True boss", number)
            return number
        else:
            pass
            # return False   #worng!!!
        
print(check_even_list([1,2,3,4,6,8]))     # it returns False and exit the block because it only checks 1st element and coming out from it
'''
Note: Difference between 'print' and 'return'
print just print the value stored in the passing variable on terminal
ex: print(var1)   # print the value there inside var1
return will stores the value to varible which is used to call the function 
ex: var2 = fun()  #fun() o/p data will be stored inside the var2

While using looping concept diff betwn print and return
Inside the loop if use print, it will print change varable data every the loop iteration
ex: def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            print("True boss", number)           
        else:
            pass
        
print(check_even_list([1,2,3,4,6])) # it will prints ('True boss', 2)  ('True boss', 4) ('True boss', 6) and None

Inside the loop if use retun, it will terminates the loop whenever the block of the code executed True and stops iteration
ex: def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            print("True boss", number)
            # return True
        else:
            pass
        
print(check_even_list([1,2,3,4,6,8]))    # during 2nd iteration 2 is even and execute the True block and terminate the looping process

ex2: 
def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            print("True boss", number)
            return number
        else:
            pass
        
print(check_even_list([1,2,3,4,6,8]))   # o/p 2 and terminates the looping processs 
'''


#For Else Statement

def check_even_list(my_lsit):
    for number in my_lsit:
        if number % 2 == 0:
            return True
        else:
            pass                 #it will just pass block without returning any thing
    
    else:
        return False
#OR u can directly use for loop return statement
    return False
    
# print(check_even_list([1,3,5]))  # returns False because inside the for loop body no conditins(no true conditions) will return data and finally else block of for loop will get executed

# return even number in list using for and retrun statement
def check_even_list(my_lsit):
    #create empty list
    even_number_list = []
    for number in my_lsit:
        # even_number_list = []   #Dont create list as local variable to for loop because every loop the appended values changes and contains only last append loop value
        if number % 2 == 0:
            #append this block executed even numbers into list
            even_number_list.append(number)
            
        else:
            pass                 
    
    return even_number_list    #Finally return all appended even number stored in list
    
print(check_even_list([1,2,4,5,6,7,8]))     #o/p : [2,4,6,8]


#Tuples unpacking using Function and For loop
#Find out the maximum hour worked employee or employee of the month
work_hrs = [('darshan', 200), ('boss', 800), ('harsh', 400)]
def find_employee(work_hrs):
    current_mx_hrs = 0
    employee_of_month = ' '
    for employee, hours in work_hrs:

        if hours > current_mx_hrs:
            current_mx_hrs = hours
            employee_of_month = employee
            # print(employee, hours)
            
        else:
            pass
        
    return (employee_of_month, current_mx_hrs)
print(find_employee(work_hrs))                 #o/p: ("boss", 800)
#(or) call the function using below way
name, hour = find_employee(work_hrs)
print(name)                                    #o/p: boss