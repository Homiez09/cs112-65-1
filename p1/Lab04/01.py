<<<<<<< HEAD
target = 72 
n = int(input("Enter your guess (0 - 100): "))
if n >= 0 and n <= 100:
    if n > target:
        print("Sorry, your guess is too high, try again later.")
    elif n < target:
        print("Sorry, your guess is too low, try again later.")
    else:
        print("Congratulations, your guess is correct.")
else:
=======
target = 72 
n = int(input("Enter your guess (0 - 100): "))
if n >= 0 and n <= 100:
    if n > target:
        print("Sorry, your guess is too high, try again later.")
    elif n < target:
        print("Sorry, your guess is too low, try again later.")
    else:
        print("Congratulations, your guess is correct.")
else:
>>>>>>> 47493b7 (Update LAB05)
    print('Sorry, out of range, try again later.')