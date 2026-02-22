
import time
import time

hour = int(time.strftime('%H'))

if 6 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")
# timestamp=time.strftime('%H:%M:%S')//24 hours format
# timestamp=time.strftime('%I:%M:%S:%p') # hours format
# print(timestamp)

# # Ask user to enter time in HH:MM format
# time_input = input("Enter time in HH:MM format (24-hour): ")

# # Extract hour part and convert to int
# hour = int(time_input.split(":")[0])

# # # Decide greeting
# # if 5 <= hour < 12:
# #     print("Good Morning!")
# # elif 12 <= hour < 17:
# #     print("Good Afternoon!")
# # elif 17 <= hour < 21:
# #     print("Good Evening!")
# # else:
# #     print("Good Night!")


 

# Manual Time check
# Current_time=int(input("Enter the time"))
# if Current_time >=7 and Current_time <=12:
#     print("Good Moring")
# elif Current_time >=    12 and Current_time<=18:
#  print("Good Evening")
# elif Current_time >=18 and Current_time<=24:
#           print("Good night")
# else:  
#       print("Re enter the time ")