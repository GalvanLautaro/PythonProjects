def calculateOddEven(vector):
    i = 0
    contOdd = 0
    contEven = 0

    while i < len(vector):
        if vector[i] % 2 == 0:
            contEven += 1
        else:
            contOdd += 1
        i += 1

    print("Even numbers: " + str(contEven))
    print("Odd numbers: " + str(contOdd))


n = int(input("Enter the number of numbers: "))
vector = []

while len(vector) < n:
    number = int(input("Enter a number: "))
    vector.append(number)

calculateOddEven(vector)