def reverse(text):
    wordlist = text.split()    #split() used for breaks the string into words seperate in list ie, ['I', 'am', 'boss']  
    reverse_list = wordlist[::-1]  # this will reverse reverse the words order in list ie, ['boss', 'am', 'I']
    print(' '.join(reverse_list))   # ''.join() function joins the string from list and element list gives string    **** '--'.joint() function add '--' between words 
    return wordlist

reverse('I am boss')

## boss am I



def myfunc(letters):
    letter = []
    for index in range(len(letters)):
        # print(index)
        if index % 2 == 0:
            letter.append(letters[index].upper())    #['A', 'C', 'E', 'G']
        else:
            letter.append(letters[index].lower())    #['b', 'd', 'f']
    return ''.join(letter)

a = myfunc('abcdefg')
print(a)

## AbCdEfG

def spy_game(nums):
	code = []
	for num in nums:
		if num == 0:
			code.append(0)
		elif num == 7:
			code.append(7)
			print(code)
			break

	return code == [0,0,7]

print(spy_game([1,2,3,0,0,7,9,7]))

'''
# LEGB Rule for checking the variable 
Local : First check within the local function to if any variables or defined or not
Enclosing Bracket: Then it checks the variable defined with the enclosing bracket space defined in the function.
Global : Finally it checks for variable defined at the top level or at the begining of code.
Built-in : If variable not defined in all the cases it check its an in built variable(len,sum..) or not.
'''

#Global Varibale
num = 'Global String'
def great():
    #Enclosing Varibale
    num = 'Enclosing String'
    def hello():
        #Local Varibale
        num = 'local String'
    return num
print(great())  #This print 'local string', if comment that then it check for enclosing and print 'Enclosing String', if u again comment that final it looks at global varible and prints 'Global String' 


x = 5
def fun():
    global x   # Goto global declaration space and grab value of x
    print('Initial x value is ', x)
    #locla assignment
    x = 200
    print("Value of x is ', x)
    return x   #return x =200
   
#Find upper and lower case letter in the given string	  
s = 'Hi Boss How Are You!'
def up_low(s):
    countUP = 0
    countLW = 0
    for letter in s:
        if letter.isupper():
            countUP = countUP + 1
            # print(countUP)
        elif letter.islower():
            countLW = countLW + 1
            # print(countLW)
        else:
            pass
    return countUP, countLW
	  
	  #(or) By using Dictionary approach
	  
def up_low(s):
    d = {'countUP':0, 'countLW':0}
    for letter in s:
        if letter.isupper():
            d['countUP'] += 1
            # print(countUP)
        elif letter.islower():
            d['countLW'] += 1
            # print(countLW)
        else:
            pass
    return d['countUP'], d['countLW']

print(up_low(s))  # 5,10

#Check the given number with in the range or not
def check_range(num, low_range, high_range):
	if num in range(low_range, high_range+1):
	  print(Yes num is within the given range)
	 else:
	  print(No num is within the given range)
	return num
print(check_range(5,2,7)) #Yes num(5) is within the given range
print(check_range(10,2,7)) #No num(10) is within the given range
	  
	  
#Check pallidrome or not
s = 'nurses run'
def palindrome(s):
    #remove spaces in String
    s = s.replace(' ','')
    print(s)
    # Check sting is == reverse version of the string
    if s == s[::-1]:
        print(palindrome)
    else:
        print("Not a palindrome")

print(palindrome(s))	
	  
