n = int(input("Enter number of triangles: "))
contE = 0
contI = 0
contS = 0

for i in range(n):
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 2: "))

    if side1 == side2 and side1 == side3:
        print("Equilateral triangle.")
        contE += 1
    else:
        if side1 == side2 or side1 == side3 or side2 == side3:
            print("Isosceles triangle.")
            contI += 1
        else:
            print("Scalene triangle.")
            contS += 1

print("Equilateral triangles: ", contE)
print("Isosceles triangles: ", contI)
print("Scalene triangles: ", contS)
