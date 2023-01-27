#Q30. Exercise 6: Write a Python program to calculate the power of two numbers. Don't use ** operator.
def power(basenum,pownum):
    result = 1
    for i in range(pownum):
        result=result*basenum
    return result
basenum=int(input("Enter base\n"))
pownum=int(input("Enter power\n"))
print(power(basenum,pownum))
