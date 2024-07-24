import time
# t= time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
hour= int(input("enter any time: "))

if (hour>=0 and hour<12):
    print("Good Morning Sir")
elif(hour>12 and hour<=18):
 print("Good afternoon Sir")
else:
 print("Good Night Sir")

