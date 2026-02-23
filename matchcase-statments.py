key = int(input("Enter your pass key"))

match key:
    case 2678:
        print("This is key is orignated from lahore")
    case 26760:
        print("This key is generated from islamabad")
    case 2676:
        print("This key is generated from main origin")
    case _:
        print("This key dont have any key routes")

