num = int(input("Enter a number of up to 3 digits: "))

if num < 10:
    print("Has one digit.")
else:
    if num < 100:
        print("Has two digits.")
    else:
        if num < 1000:
            print("Has three digits.")
        else:
            print("Data entry error.")