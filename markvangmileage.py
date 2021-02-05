EnterData = str.lower(input("Would you like to calculate average miles per gallon? Enter yes or no: "))
NewTrip = 0

y = "yes"
n = "no"


while EnterData == y:
    CarName = input("Please enter your car's name: ")
    AmountOfGas = input("Please enter the amount gas: ")
    g = int(float(AmountOfGas))
    AmountOfMiles = input("Please enter the amount of miles traveled: ")
    m = int(float(AmountOfMiles))
    print("Car Name: ", CarName)
    print("Amount of Gas(gal): ", AmountOfGas)
    print("Total Miles Driven(mi): ", AmountOfMiles)
    print("Average Miles Per Gallon (MPG):", m / g)
    NewTrip = input("Would you like to calculate another trip? Enter yes or no: ")
    if NewTrip != y:
        break
if EnterData == n:
    print("Thank you for using the program.")
elif NewTrip == n:
    print("Thank you for using the program.")
else:
    print("Please only enter yes or no")



