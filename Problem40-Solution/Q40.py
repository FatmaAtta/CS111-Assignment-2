def fib(size):
    a,b=0,1
    print('1 ',end='')
    for i in range(1,size):
        a,b=b,a+b
        print(b,end=' ')
size=int(input("Enter size\n"))
fib(size)