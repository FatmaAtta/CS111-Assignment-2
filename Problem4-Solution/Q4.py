#Q4. You need to write an algorithm for finding the factorial of a non-negative integer n.
#Recall that the factorial of n is defined as the product: 1×2 × 3 × …..× (n-1) × n The factorial of 0 is defined to be 1.
#Draw a flowchart diagram for your algorithm. Test the execution of the flowchart step-by-step on n = 0, 2, 6, 10
# Implement the algorithm as a Python script. Test the execution of the flowchart step-by-step on n = 0, 2, 6, 10
def factorial(n):
    if n==0 or n==1:
        fact=1
    else:
        fact=n*factorial(n-1)
    return fact
n=int(input("Enter a number \n"))
print(n,"! = ",factorial(n))
