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
countUP = 0
countLW = 0
def up_low(s):

    for letter in s:
        if letter.isupper():
            global countUP
            countUP = countUP + 1
            # print(countUP)
        else:
            global countLW 
            countLW = countLW + 1
            # print(countLW)
    return countUP, countLW

print(up_low(s))  # 5,15
