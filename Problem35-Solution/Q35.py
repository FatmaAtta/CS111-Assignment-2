#Q35. Exercise 11: Write a Python program that will take a non-empty string and an int n, return a new string where the char at index n has been removed.
#The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)
string=input("Enter a string\n")
n=int(input("Enter the index\n"))
if n<len(string) and n>=0:
    print(string[:n],string[n+1:],sep='')
else:
    n=int(input("Enter an index within range"))
