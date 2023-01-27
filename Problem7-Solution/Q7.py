#Q7. Suppose A is an array of 100 elements. Write a for-loop that stores the elements of A in reverse order in a new array X.
#That is, A[0] must go to X[99], A[1] must go to X[98] and so on.

a=[]
x=[]
a.extend(range(1,101))
#print(len(a))
for i in range(1,101):
    x.append(a[-i])
print(a)
print("\n")
print(x)
