numOfAssign = input("Enter number of grades to process: ")
numOfAssign = int(numOfAssign)
studentName = input("Enter a student name: ")
total = 0
counter = 0
while counter < numOfAssign:
    grade = input("Please enter an assignemnt grade: ")
    grade = int(grade)
    total = total + grade
    counter = counter + 1

average = total / numOfAssign
print("Student " + studentName + " received a final grade of" ,average)


