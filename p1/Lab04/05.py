<<<<<<< HEAD
age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

if age >= 15 and age <= 60:
    if income <= 30000 and income >= 1:
        print(f"Your negative income tax is {(income * 0.2):.2f} Baht.")
    elif income <= 79999:
        print(f"Your negative income tax is {(6000 - ((income-30000) * 0.12)):.2f} Baht.")
    else:
        print("Invalid income.")
else:
=======
age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

if age >= 15 and age <= 60:
    if income <= 30000 and income >= 1:
        print(f"Your negative income tax is {(income * 0.2):.2f} Baht.")
    elif income <= 79999:
        print(f"Your negative income tax is {(6000 - ((income-30000) * 0.12)):.2f} Baht.")
    else:
        print("Invalid income.")
else:
>>>>>>> 47493b7 (Update LAB05)
    print("Invalid age.")