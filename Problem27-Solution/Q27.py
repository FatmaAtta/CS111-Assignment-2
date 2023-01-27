num = input("enter an integer\n")
length=len(num)
number=[int(x) for x in num]
sum=0

for i in range(0,length):
    sum+=int(number[i])
print(sum)


