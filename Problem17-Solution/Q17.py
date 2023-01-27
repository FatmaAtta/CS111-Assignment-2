#Q17. We want to write a program to convert a positive decimal number to the equivalent binary number in one byte. We already do this algorithm by hand, but we want to formulate it in the form of pseudocode so we can program it in Python. Your algorithm should:
#1) Take the input from the user.
#2) Check if it is in the range that can be represented in one byte. If not, show an error message.
#3) Convert it to binary and display the result.

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

