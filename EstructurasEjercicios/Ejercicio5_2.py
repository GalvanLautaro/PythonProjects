summ = 0

for i in range(10):
    number = int(input("Enter a number: "))
    if i > 4:
        summ += number

print("The sum of the last 5 numbers is: ", summ)