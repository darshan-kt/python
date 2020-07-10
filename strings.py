//Indexing and slicing { This same concept can be used for strings, lists, tuples, dist }

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
    
   
  // .format : adding the string/number in between the sentance using {} and .format(' ')  kind of fill in the blanks
  
  print(" darshan is {} boy" .format('good'))     //darshan is good boy
  print(" {c} is {a} {b}" .format('a= good', 'b= boy', 'c=darshan'))    //darshan is good boy   or can use index also instead of variables inside curly brackets

  // another way of using .format
  name= "darshan"
  age = 23
  print(f'{name} is {age} years old.')      //darshan is 23 years old
  
  //concatination
  a= darshan
  b= a + " boss"
  print(b)    //darshan boss
  
  a.upper()    //DARSHAN
  a.lower()    //darshan
  
  //create a list of strings/words
  c= " darshan is a boss"
  c.split()                            // ['darshan', 'is', 'a', 'boss']
  
  
  //Lists
  my_list =[1,2,3,4]
  my_list.append(5)       //[1,2,3,4,5]
  my_list.pop()           //[1,2,3,4]   delete last one
  my_list.pop(2)          //[1,2,4]     delete 2nd index num
  
  my_new_list = ['a' ,'d', 'c', 'b']
  my_new_list.sort()          // ['a' ,'b', 'c', 'd']    oreder in the correct 
  
  //distinaries
  key-value pair mechanism with flower brackets
  my_dist={'apple':red, 'ball':360}
  my_dist[apple]             //red
  
  //Tuples
  compare to lists these are immutables- values inside the brackets/tuples cann't changed using indexing, uses curly brackets
  my_list = [1,2,3,4]
  my_list[2] = "abc"    //[1,2, "abc", 4]

//sets
#un-oder collection of unique elements, avoid repeative unique number inside it
my_set = set()
my_set.add(1)
my_set.add(1)
my_set.add(1)
print my_set     #output gives set([1]) means avoid repetative elements

my_list = [1,1,2,2,3,3,3,4,4,4,5,5,5]
print set(my_list) #output [1,2,3,4,5]
  
  my_tuple = (1,2,3,4)
  my_tuple[2] = "abc"    //error 
  
  //Boolens 
    # Booleans are operators that allow u to convey True or False statements, usually used to deal with control flow and logic

    
  //file I/O
myfile = open('/home/darshan_k_t/skillup/python/dar.txt')
contents = myfile.read()
print contents
# print myfile.read()
print myfile.seek(0)    #reset file cursor location
print myfile.readline()

with open("/home/darshan_k_t/skillup/python/dar.txt") as my_new_file:    #change file name
    content = my_new_file.read()
    print content
    
with open('/home/darshan_k_t/skillup/python/my_new_file', mode='a') as f:  
    f.write("\n Add BOSS is back!")  #added new line
   
with open('/home/darshan_k_t/skillup/python/my_new_file', mode='r') as f:    
    print (f.read())   # reading the added file
  
#write a script to open file, write something and close it
y = open("test.txt", 'w')
y.write("Hello World")
y.close()

