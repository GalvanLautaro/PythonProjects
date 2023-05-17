numberQuestions = int(print("Enter the number of questions: "))
numberCorrectQuestions = int(print("Enther the number of correct questions: "))
percentage = (numberQuestions / numberCorrectQuestions) * 100

if percentage >= 90:
    print("Max level.")
else:
    if percentage >= 75:
        print("Medium level.")
    else:
        if percentage >= 50:
            print("Regular level.")
        else:
            print("Out of level.")