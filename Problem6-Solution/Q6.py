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