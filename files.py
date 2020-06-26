# Create a file as mytext.txt and save this

# open that file
myfile = open('my_text.txt')
myfile.read()       #to read the data inside the txt file
myfile.readlines()  #to read each line inside the string

#open the list in another way

with open('my_text.txt') as myfile:
  myfile.read()
  myfile.readlines()
  
 # Different modes are available read, write, append
 1. read mode
 with open('my_text.txt', mode= r) as myfile:
  myfile.read()
 
 2. append mode and write mode(In write mode clears the previous data and add the new data)
 with open('my_text.txt', mode= a) as myfile:
  a = myfile.write('/nAdd this new line')
  print(a)
  
  # Script to create text file and write data into it and close the txt file
  y = open("test.txt", 'w')
  y.write("Hello World")
  y.close()
