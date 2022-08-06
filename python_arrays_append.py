print("Welcome to the Ice Creamery")

print()

flavorsList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Nepolitian"]
flavorsList[1] = "Rocky Road"
flavorsList.append("Chocolate")
flavorsList.sort()
numFlavors = len(flavorsList)

print("These are the", numFlavors, "flavor we are serving today at The Ice Creamery: ")

for flavor in flavorsList:
    print("Flavor#: ", flavorsList.index(flavor)+1, " ", flavor)

print()

conePrices={"S":"$1.50","M":"$2.50","L":"$3.50"}
coneSizes={"S":"smallish","M":"more for me","L":"lotta lickin"}

customerSize = input("Please enter the cone size of your choosing: S, M, or L: ").upper()
if (customerSize != "S") and (customerSize != "M") and (customerSize != "L"):
        print("Sorry, that's not a valid size. You must enter S, M, or L.")
else:
    customerFlavor = int(input("Please enter your flavor number: "))
    if (customerFlavor < 1 or customerFlavor > 8):
        print("Sorry, that's not a valid flavor number. We have", numFlavors, "flavors of ice cream today.")
    else:
        print()
        print("Your total is: ", conePrices[customerSize])
        print("Your", coneSizes[customerSize], "sized cone of The Ice Creamery's", flavorsList[customerFlavor-1], "will arrive shortly.")

print()
print("Thank you for visiting the Ice Cream Creamery")



