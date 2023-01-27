num = input("enter an integer\n")
length=len(num)
number=[int(x)**3 for x in num]
sum=0

for i in range(0,length):
    sum+=int(number[i])
if str(sum)==num:
    print(num, " is an Armstrong number\n")
else:
    print(num, " is not an Armstrong number\n")



