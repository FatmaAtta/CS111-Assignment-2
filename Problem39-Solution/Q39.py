#Q39. Exercise 15: Write an algorithm and draw a flowchart to print the SUM of numbers from LOW to
#HIGH. Test with LOW=3 and HIGH=9.(2) Write a Python program to implement this algorithm.

sum = 0
low=int(input("Enter low\n"))
high=int(input("Enter high\n"))
for i in range(low,high+1):
    sum += i
print(sum)

