num1 = int(print("Enter a number: "))
num2 = int(print("Enter a number: "))
num3 = int(print("Enter a number: "))

if num1 < num2 and num1 < num3:
    print(num1)
else:
    if num2 < num3:
        print(num2)
    else:
        print(num3)
if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)