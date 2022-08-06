from miles import convertToMiles
from kilometers import convertToKilometers

validValue = True
processing = True

while processing:
    userDistance = float(input("Please enter a distance value: "))
    userUnit = input("What is the unit of length (M = miles, KM = kilometers) :")

    if userUnit.upper() == "M":
        convertedDistance = convertToKilometers(userDistance)
        conversionUnit = "kilometers"
        userUnit = "miles"

    elif userUnit.upper() == "KM":
        convertedDistance = convertToMiles(userDistance)
        conversionUnit = "miles"
        userUnit = "kilometers"

    else:
        validValue = False

    if validValue:
        print("Your distance of ", userDistance, " ", userUnit, "is equivalent to", convertedDistance, conversionUnit)
    else:
        print("You entered an invalid unit of lenght.")
        validValue = True
    userKey = input("Press X to quit or enter to continue processing. ")

    if userKey.upper() == "X":
        processing = False
print("Thanks, Goodbye!")