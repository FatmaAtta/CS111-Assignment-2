a=[]
x=[]
a.extend(range(1,101))
#print(len(a))
for i in range(1,101):
    x.append(a[-i])
print(a)
print("\n")
print(x)