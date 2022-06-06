def frequency(arr, n):
 
    # Sort the array
    arr.sort()
 
    max = 1 #each element will be present atleast once
    Num = arr[0]
    c = 1
 
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            c += 1
        else:
            c = 1
        if (c > max):
            max = c #updated the max value to the present num frequency
            Num = arr[i - 1]
 
    return Num
    return print(f"{Num} repeated {max}times")
print(frequency([2,4,56,6,54,33,5,5,5,6,6,6,6,7],14))  