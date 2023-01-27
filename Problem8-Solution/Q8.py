from random import randint

p=int(input("Enter the index of the number to remove\n"))
n=int(input("length of array\n"))

 #Fills an array with random integers from 0 to 100
A=[randint(0,100) for num in range(0,n)]
print(A)
 #lets user retype the index to be removed if it's not in the specified range
while p<0 or p>=n:           
    p=int(input("Enter the index of the number to remove\n"))
 #removes the element
del A[p]
print(A)
