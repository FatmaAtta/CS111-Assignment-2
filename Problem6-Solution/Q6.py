#Write a while-loop to swap every successive pair of elements in an array A of 50 elements,
#i.e., A[0] and A[1] should be swapped, A[2] and A[3] should be swapped and so on.

elements = [i for i in range(1,51)]
print(elements)
print("\n")
i=0
while i < 49:
    temp =elements[i]
    elements[i]=elements[i+1]
    elements[i+1]=temp
    i+=2
print(elements)
