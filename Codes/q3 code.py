a= int(input("enter the the first number "))
b= input("enter the mathematical operator ")
c= int(input("enter the second number "))
 ###convert the string value
if b=='+':
    r=a+c
elif b=='*':
    r=a*c
elif b=='/':
    r=a/c 
else:
    r=a-c 
print(r)
