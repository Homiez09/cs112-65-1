target = 1234
i = 0
count = 0
n = input("Enter your guess (4-digit integer): ")

if n == target:
    print("Congratulations, you just mastered my mind!!")
else:
    while i < 4:
        if n % 4 in target:
            count += 1
        i += 1

print(count)