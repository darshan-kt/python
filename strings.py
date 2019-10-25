//Indexing and slicing

my_string = 'abcdefg'
print(mystring[1])    //b
print(mystring[-1])    //g
print(mystring[1:])    //bbdcefg       from 1 onwards
print(mystring[:3])    //abc           upto 3
print(mystring[1:4])    //bcd           from 1 to 4
print(mystring[1:6:2])    //bdfg        from 1 to 6 with 2 increment
print(mystring[::1])    //abcdefg     one of increment
print(mystring[::2])    //aceg        two increment
print(mystring[::-1])    //gfedcba    Note:Interview question: Reverse the string or list whithout using for loop
