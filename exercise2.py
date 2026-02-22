# # ID = "3KM3N1U3"
# # Name = input("Enter your name: ")

# # count = 3  # attempts

# # while count > 0:
# #     entered_id = input("Enter ID: ")
# #     if entered_id == ID:
# #         print(Name, "Welcome")
# #         break
# #     else:
# #         count -= 1
# #         if count > 0:
# #             print(f"Invalid ID. You have {count} attempt(s) left.")
# #         else:
# #             print("You have been locked out. Please contact the administrator.")










# Key="A3HN3IMDBBFK3SN"
# Name=input("Enter your Name")

# count=3
# while count>0:
#    enter_id=input("Enter pass Key")
#    if enter_id==Key:
#     print("Welcome",Name,"to our dashboard")
#     break
#    else:
#     count -=1
#     if count>0:
#      print(f"Invalid Key, {count} attempts left")
#     else:
#       print("You are locked contact admin")
    
   

copass_key = 7
num = int(input("Enter a number between 1 to 10: "))

for i in range(1, 11):
    if i == num and i == pass_key:
        print("The number matched:", i)
        break
    else:
        print(i, "not match")
