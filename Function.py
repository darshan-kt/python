def reverse(text):
    wordlist = text.split()    #split() breaks the each words seperate in list
    reverse_list = wordlist[::-1]  # this will reverse reverse the words order in list
    print(' '.join(reverse_list))   # ''.join() function joins the string from list and element list gives string
    return wordlist

reverse('I am boss')

## boss am I
