#Q29. Exercise 5: Write a python program that takes two integer values (start and end). This program will
#find all numbers (between start and end) which are divisible by 9 but are not divisible by 4.
#The numbers obtained should be printed in a comma-separated sequence on a single line

starting=int(input("Enter start\n"))
ending=int(input("Enter end\n"))
for i in range(starting,ending):
    if i%9==0 and i%4!=0:
        print(i,end=', ')
