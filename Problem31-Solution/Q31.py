#Q31. Exercise 7: Write a Python program to take from the user three integer numbers (x,y, z) and your program should search about an operations 
#(e.g., +, -,*,%, etc) that can be executed on both x and y such that the result should be z, then you program would print x operations y = z
def operation(x,y,z):
    if x+y==z:
        print(x,' + ',y,' = ',z)
    elif x-y==z:
         print(x,' - ',y,' = ',z)
    elif x*y==z:
         print(x,' * ',y,' = ',z)
    elif x/y==z:
         print(x,' / ',y,' = ',z)
    elif x%y==z:
         print(x,' % ',y,' = ',z)
    elif x**y==z:
         print(x,' ** ',y,' = ',z)
    elif x//y==z:
         print(x,' // ',y,' = ',z)
x=int(input("Enter x\n"))
y=int(input("Enter y\n"))
z=int(input("Enter z\n"))
operation(x,y,z)
