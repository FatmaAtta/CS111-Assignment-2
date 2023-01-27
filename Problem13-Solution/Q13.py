num = int(input("Enter a positive number\n"))
 #lets user re-enter a number if number was negative
while num<0:
    num = int(input("Enter a positive number\n"))
 #creates a list with all factors of a number
factors=[i for i in range(1,num+1) if num % i == 0]
print(factors,end=' ')


