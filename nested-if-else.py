Age=int(input("Enter your age "))

if Age>=21:
    print(
        "You are a Teenager"
        
    )
elif Age<=18:
    if Age>10 and Age<17:
     print("Your age group rely in 10-17")
    elif Age>=18 and Age<=20:
       print("Than you are reky in group 18-20")
    else:
       print(
      "You are under age "
   )
