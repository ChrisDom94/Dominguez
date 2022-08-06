def convertTemp(temps, tempScale):
    if tempScale == "F":
        temps[0] = ((temps[1]-32) * 5/9)
    elif tempScale == "C":
        temps[1] = ((temps[0] * 9/5) + 32)
    return(temps)
tempEntered = float(input("Enter a temperature value: "))
tempScale = input("Enter a single letter to indicate the temperature scale (C or F): ")

tempScale = (tempScale.upper())

temps = [0,0]

if tempScale == "C":
    temps[0] = tempEntered
elif tempScale == "F":
    temps[1] = tempEntered

(temps, tempScale)

print("You entered ", tempEntered, " degrees ", tempScale, ">>>")
print("The temperature in Celsius is ", temps[0])
print("The temperature in Fahrenheit is ", temps[1])