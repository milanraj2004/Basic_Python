seat_type = input("Enter Seat type(sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper --- No AC available")

    case "ac":
        print("AC---- air Conditioning")
    case "general":
        print("General -- No Reservation Required And cheap ")
    case "luxury":
        print("Luxury - Premium Seats are Required with Meals")
    case _:
        print("Invalid seat Type")