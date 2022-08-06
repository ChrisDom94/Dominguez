recordsList = []
recordCount = 0

file=open("IT244_U5_Data.txt", "r")
for line in file:
    recordsList.append(line.strip())
file.close()

recordsList.append("5,Brady,Bobby,4222 Clinton Way,Los Angeles,CA")

file = open("IT244_U5_Data.txt", "w")
file.write("Customer ID, Last Name, First Name, Address, City, State, Promo Credit\n")

for record in recordsList:
    file.write(record)
    file.write(",$500\n")
    recordCount = recordCount+1
file.close

print("There were", recordCount, "records written to the promo credits csv file.")

