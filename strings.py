//Indexing and slicing

my_string = 'abcdefg'
print(mystring[1])    //b
print(mystring[-1])    //g
print(mystring[1:])    //bbdcefg
print(mystring[:3])    //abc
print(mystring[1:4])    //bcd
print(mystring[1:6:2])    //bdfg
print(mystring[::1])    //abcdefg   -->one of increment
print(mystring[::2])    //aceg      -->two increment
print(mystring[::-1])    //gfedcba   Note:Interview question: Reverse the string or list whithout using for loop
