i,m,summation = 1,0,0.0
n = int(input("Enter the number of terms \n"))
for x in range(0,n):
    summation = summation + ((-1)**m)*(1/i)
    i=i+2
    m=m+1
print("Pi = ",4*summation)


