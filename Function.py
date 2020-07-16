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
