target = 72
count = 0
while True:
    n = int(input("Enter your guess: "))
    count += 1
    if n < 0 or n > 100:
        print("Sorry, your guess is out of range.")
    else:
        if n < target:
            print("Sorry, your guess is too low.")
        elif n > target:
            print("Sorry, your guess is too high.")
        else:
            print("Congratulations, your guess is correct.")
            print(f"Total number of guesses is {count}.")
            break