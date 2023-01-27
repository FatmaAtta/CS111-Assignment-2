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




