starting=int(input("Enter start\n"))
ending=int(input("Enter end\n"))
for i in range(starting,ending):
    if i%9==0 and i%4!=0:
        print(i,end=', ')