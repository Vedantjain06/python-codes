def prime(num1,num2):
    
    for i in range(num1,num2+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                c=c+1
        if(c==0):
            print(f"{i} is prime")
              
prime(5,15)                
