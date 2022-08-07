<<<<<<< HEAD
year = int(input("Enter year: "))

if not (year > 9999 or year < 1):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Invalid year.")
=======
year = int(input("Enter year: "))

if not (year > 9999 or year < 1):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Invalid year.")
>>>>>>> 47493b7 (Update LAB05)
