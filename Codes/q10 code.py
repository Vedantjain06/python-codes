a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

a = a ^ b
b = a ^ b  # ^ is xor operator 
a = a ^ b

print('Values After Swapping')
print('a = ',a, 'and b = ',b)