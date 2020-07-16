def reverse(text):
    wordlist = text.split()
    reverse_list = wordlist[::-1]
    print(' '.join(reverse_list))
    return wordlist

reverse('I am boss')

## boss am I
