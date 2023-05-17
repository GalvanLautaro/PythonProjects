contApproved = 0
contDisapproved = 0
i = 0

while(i < 10):
    note = int(input("Enter note " + str(i) + ": "))
    if note >= 7:
        contApproved += 1
    else:
        contDisapproved += 1
    i += 1

print("Approved count: ", contApproved)
print("Disapproved count: ", contDisapproved)