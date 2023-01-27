def power(basenum,pownum):
    result = 1
    for i in range(pownum):
        result=result*basenum
    return result
basenum=int(input("Enter base\n"))
pownum=int(input("Enter power\n"))
print(power(basenum,pownum))
