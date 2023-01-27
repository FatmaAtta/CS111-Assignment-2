time1=input("Enter time 1\n").split(',')
time2=input("Enter time 2\n").split(',')

t1=int(time1[0])*3600+int(time1[1])*60+int(time1[2])  #converting the time into seconds
t2=int(time2[0])*3600+int(time2[1])*60+int(time2[2])  #converting the time into seconds

t3=t1-t2

hour3=t3//3600
min3=(t3-hour3*3600)//60
sec3=t3-(hour3*3600+min3*60)

print(hour3,", ",min3,", ",sec3)
