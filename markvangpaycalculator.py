EnterData = str.lower(input("Would you like to calculate your pay? Enter yes or no: "))
NewData = 0

y = "yes"
n = "no"

while EnterData == y:
    EmployeeName = input("Please enter the employees name: ")
    HourlyRate = input("Please enter the amount of pay (example: 14.35): ")
    h = int(float(HourlyRate))
    TotalHours = input("Please enter the amount of hours worked (example 4.25): ")
    t = int(float(TotalHours))
    print("Employee Name: ", EmployeeName)
    print("Hourly Rate: $", HourlyRate)
    print("Total hours worked: ", TotalHours)
    print("Total Pay: $", h * t)
    NewData = input("Would you like to enter another employee? Enter yes or no: ")
    if NewData != y:
        break
if EnterData == n:
    print("Thank you for using the program.")
if NewData == n:
    print("Thank you for using the program.")
else:
    print("Please only enter yes or no")



