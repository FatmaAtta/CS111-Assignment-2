#Q28. Exercise 4: update exercise 3 to check whether a given number is an Armstrong number or not.
#A positive integer is called an Armstrong number if the sum of the cubes of individual digits of the
#number is equal to that number itself. For example, the sum of cubes of individual digits of the number
#153 is 1* 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3 = 153. Hence, number 153 is an Armstrong number.

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
