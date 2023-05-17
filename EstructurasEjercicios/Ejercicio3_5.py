x = int(print("Enter x: "))
y = int(print("Enter y: "))

if x == 0 and y == 0:
    print("Data entry error")

if x > 0 and y > 0:
    print("1 quadrant.")
else:
    if x < 0 and y > 0:
        print("2 quadrant.")
    else:
        if x > 0 and y < 0:
            print("3 quadrant.")
        else:
            print("4 quadrant.")
