salary = int(print("Enter the salary: "))
yearsOld = int (print("Enter the years old:"))
newSalary = int

if salary < 500 and yearsOld >= 10:
    newSalary = salary + salary * 0.2
    print("New salary: ", newSalary)

if salary < 500 and yearsOld < 10:
    newSalary = salary + salary * 0.05
    print("New salary: ", newSalary)

if salary >= 500:
    print("Normal salary: ", salary)