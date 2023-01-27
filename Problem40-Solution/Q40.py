#Q40. Exercise 16: Write a python function that takes an integer number (size) then it generates Fibonacci sequence with the given size. (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence
looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fib(size):
    a,b=0,1
    print('1 ',end='')
    for i in range(1,size):
        a,b=b,a+b
        print(b,end=' ')
size=int(input("Enter size\n"))
fib(size)
