def rangeprime(num):
    
    for i in range(2,num): #number should be equal to or greater than 2 
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if(c==0):
            print(f"{i} is prime") #f string used for good visible output
rangeprime(45)            