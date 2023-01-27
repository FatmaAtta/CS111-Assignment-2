upCase=[0,0,0,0,0]
word=input("Enter a word of 5 letters \n")
while len(word)>5:
    word=input("Please enter a word of 5 letters\n")
ascii=[ord(i) for i in word]
for i in range(0,5):
    if ((ascii[i])>=65 and (ascii[i])<=90):
        upCase[i]=chr(ascii[i])
    else:
        upCase[i]=chr((ascii[i]-32))
for i in range(5):
    print(upCase[i],end='')
print("\n")
