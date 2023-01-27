#Q18. The German mathematician Leibniz (1646–1716) discovered the rather remarkable fact that the
#mathematical constant () Pi ط can be computed using the following mathematical relationship:
#The formula to the right of the equal sign represents an infinite series; each fraction represents a term in that series. If you start with 1, subtract one-third, add one-fifth, and so on, for each of the odd integers, you get a number that gets closer and closer to the value of /4 as you go along. Then we can get .

i,m,summation = 1,0,0.0
n = int(input("Enter the number of terms \n"))
for x in range(0,n):
    summation = summation + ((-1)**m)*(1/i)
    i=i+2
    m=m+1
print("Pi = ",4*summation)
