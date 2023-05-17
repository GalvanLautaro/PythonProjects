number = int(input("Enter a number (1-10): "))

for i in range(13):
    aux = number * i
    print(str(number) + " x " + str(i) + ": ", aux)
