n = int(input("Enter number of triangles: "))
cont = 0

for i in range(n):
    base = int(input("Enter a base of triangle: "))
    height = int(input("Enter a height of triangle: "))
    surface = (base * height) / 2
    if surface > 12:
        cont += 1
    print("Base of triangle: ", base)
    print("Height of triangle: ", height)
    print("Surface of triangle: ", surface)

print("Number of triangles with surface area greater than 12: " + str(cont))

