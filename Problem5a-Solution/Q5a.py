#Checks if a string is a palindrome or not
string=[]
revString=[]
st=(input("Enter a string\n "))
string=list(st)
for i in range(len(string)-1,-1,-1):
    revString.append(string[i])
if string==revString:
    print(st," is a palindrome\n")
