n = int(input("Enter positive integer: "))

if n <= 0:
    print('Invalid number.')
elif n == 1:
    print()
else:
    i = 2
    while True:
        if n % i == 0:
            print(i)
            n = n // i
            i = 2 
            continue
        i += 1
        if n == 1:
            break