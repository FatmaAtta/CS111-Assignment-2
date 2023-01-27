string = input("Enter a string\n")
letters = 0
digits = 0
for i in range(0,len(string)):
    if (ord(string[i])>=48 and ord(string[i])<=57):
        digits+=1
    elif ((ord(string[i])>=65 and ord(string[i])<=90) or ((ord(string[i])>=97 and ord(string[i])<=122))):
        letters+=1
print("Letters ",letters,"\n","Digits ",digits,"\n")

