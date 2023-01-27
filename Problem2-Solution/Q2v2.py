#Q2. Assume that you are given time-of-the-day in the format hours-minutes-seconds, 
#using 24 hours format. Devise an algorithm to subtract one time from another. 
#The specification is: Input: integers h1, m1, s1 – representing a time,
#e.g. 13, 30, 12 h2, m2, s2 – represents another time that is prior to the first time,
#e.g., 11,40, 56. Output: integers h, m, s – difference between the two times in hours-minutes-seconds
#format. For the examples above, this will be 1, 49. 16

time1=input("Enter time 1\n").split(',')
time2=input("Enter time 2\n").split(',')

t1=int(time1[0])*3600+int(time1[1])*60+int(time1[2])  #converting the time into seconds
t2=int(time2[0])*3600+int(time2[1])*60+int(time2[2])  #converting the time into seconds

t3=t1-t2

hour3=t3//3600
min3=(t3-hour3*3600)//60
sec3=t3-(hour3*3600+min3*60)

print(hour3,", ",min3,", ",sec3)
