def check_prime(n):
    i = 1
    count = 0
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 1:
        return True
    else:
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")