#Q13. Design an algorithm for finding all the factors of a positive integer.
#For example, in the case of the integer 12, your algorithm should report the values 1, 2, 3, 4, 6, and 12. 
num = int(input("Enter a positive number\n"))
 #lets user re-enter a number if number was negative
while num<0:
    num = int(input("Enter a positive number\n"))
 #creates a list with all factors of a number
factors=[i for i in range(1,num+1) if num % i == 0]
print(factors,end=' ')


