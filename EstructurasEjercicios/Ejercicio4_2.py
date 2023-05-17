n = int(input("Enter number of people: "))
i = 0
vector = []

while i < n:
    height = float(input("Enter the height of the person: "))
    vector.append(height)
    i += 1

summ = sum(vector)
avarage = summ / len(vector)
print("The avarage is: ", avarage)