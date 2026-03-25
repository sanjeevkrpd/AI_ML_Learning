color = input("Enter color : ")

match color :
    case "Green":
        print("Go")
    case "Yellow":
        print("look")
    case "Red":
        print("Stop")
    case _:
        print("Not matched")