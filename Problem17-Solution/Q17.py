num = int(input("Please enter a positive number\n"))
if(num<0):
    num=int(input("Please enter a positive number\n"))
elif(num>255):
    num=int(input("Please enter a number between 0 and 255\n"))
binary=[0 for i in range(0,8)]
for i in range(1,8):
    if num%2==0:
        binary[-i]=0
    else:
        binary[-i]=1
    num = num//2
print(binary)

