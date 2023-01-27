#reverses the string
string=[]
string=input("Enter a string \n")
for i in range(len(string)-1,-1,-1):
    print(string[i],end=' ')

