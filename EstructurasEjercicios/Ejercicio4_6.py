vector1 = []
vector2 = []
summ = 0

while len(vector1) < 15:
    number = int(input("Enter first list: "))
    vector1.append(number)

summ = sum(vector1)

while len(vector2) < 15:
    number = int(input("Enter second list: "))
    vector2.append(number)

summ2 = sum(vector2)

if summ > summ2:
    print("List 1 is higher.")
else:
    if summ < summ2:
        print("List 2 is higher.")
    else:
        print("Equal lists")