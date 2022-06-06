import array
arr=[]
def arraytir(arr):
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] > arr[j]):    
                temp = arr[i]  
                arr[i] = arr[j]    
                arr[j] = temp  
    for j in range(100):
        if arr[j]==arr[j+1]:
            print(arr[j])
arraytir([1,2,3,4,6,6,5,]) 

        