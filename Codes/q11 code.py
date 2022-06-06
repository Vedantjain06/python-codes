def palindrome(str):
    char = list(str)
    chartemp= list(str)
    chartemp.reverse()
    if char==chartemp:
        print("palindrome")
    else:
        print("not palindrome")
palindrome("vedant")            