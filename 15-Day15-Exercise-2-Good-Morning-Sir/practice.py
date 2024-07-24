# import time

# current_time = time.localtime()

# current_hour = current_time.tm_hour + 5
# current_min = current_time.tm_min

# if 5<= current_hour <12:
#     print("goodmorning")
# elif 12<= current_hour <=16:
#     print("goodafternoon")
# else:
#     print("goodnight")    

# # print("the time now is: ",current_hour,current_min)

import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if 4 <= hour <= 12:
    print("good morning")
