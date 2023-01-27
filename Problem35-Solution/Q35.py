string=input("Enter a string\n")
n=int(input("Enter the index\n"))
if n<len(string) and n>=0:
    print(string[:n],string[n+1:],sep='')
else:
    n=int(input("Enter an index within range"))
