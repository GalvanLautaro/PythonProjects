n = int(input("Enter number of employees: "))
i = 0
contLow = 0
contHigh = 0
amount = 0

while i < n:
    salary = int(input("Enter the salary of employee " + str(i) + ": "))
    amount += salary
    if salary < 300:
        if salary > 100:
            contLow += 1
    else:
        contHigh += 1
    i += 1

print(str(contHigh) + " employees are paid more than 300")
print(str(contLow) +  " employees are paid less than 300 and more than 100")
print("The amount of the companies are $" + str(amount))
