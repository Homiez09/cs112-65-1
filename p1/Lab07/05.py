while True:
    n = int(input("Enter a number: "))
    if n == 0:
        print("End of program, goodbye.")
        break
    elif n <= 1:
        print("Invalid input, try again.")
    elif n > 1:
        count = 0
        i = 1
        while i <= n:
            if n % i == 0:
                count += 1
            i += 1
        ans = str(n)
        if count == 2:
            ans += " is a prime number."
        else:
            ans += " is not a prime number."
        print(ans)
