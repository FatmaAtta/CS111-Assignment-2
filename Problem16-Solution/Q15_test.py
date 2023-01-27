n=input("Enter a phrase\n")
phrase=[i for i in n]
enc=[]
for i in range(0,len(phrase)):
    if phrase[i]==' ':
        enc.append(' ') #for spaces to remain spaces
    else:
        enc.append(chr(ord(phrase[i])+1)) #chr() converts ascii value into its corresponding character, ord() returns the ascii calue of the character
print(enc)

