from re import A
from sqlite3 import apilevel


def countinstring(str):
    char=list(str)
    c=len(str)
    alp=digit=spec=0 #initialize value of each to zero
    for i in range(0,c):
        temp=ord(char[i]) #saves the ascii value of charecter in temp
        if temp>=65 and temp<=90:
            alp=alp+1
        elif temp>=97 and temp<=122:
            alp=alp+1  
        elif temp>=48 and temp<=57:
            digit=digit+1      
        else:
            spec=spec+1
    return alp,spec,digit
print(countinstring("vedant54387^"))                 