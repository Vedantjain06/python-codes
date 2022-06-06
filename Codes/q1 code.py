mylist = [] #declare a empty list
for i in range(1,6): #take 5 charecters for the list from user
    l1 = input(f"enter the number {i} ") 
    l1=int(l1) #convert the string into numerical value as input takes only as string datatype
    mylist.append(l1) #adding item in list in each iteration

b = input("input second parameter for list ")
if b=='asc':
    mylist.sort()
    print(mylist)
elif b=='desc':
    mylist.sort() 
    mylist.reverse()
    print(mylist)
else:
    print("wrong parameter entered")
             