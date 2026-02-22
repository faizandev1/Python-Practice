Name = input("What is your  age ?")
print ("Your age is "+ Name)


 


if Name >= "18":
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")

attempt = 3

while attempt > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "Faizan" and password == "Lionking":
        print("Welcome to system")
        break
    else:
        attempt -= 1
        if attempt > 0:
            print("Invalid username or password. Try again.")
        else:
            print("Account locked. No attempts left.")
