#Q5. Write an algorithm to take a string from the user then reverse it (e.g. if it contains abbxc, then the output will be cxbba).
#reverses the string
string=[]
string=input("Enter a string \n")
for i in range(len(string)-1,-1,-1):
    print(string[i],end=' ')

