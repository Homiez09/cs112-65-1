def factorial(n):
    i = 1
    ans = 1
    while i <= n:
        ans *= i
        i += 1
    return ans

n = int(input("Enter n: "))
print(f"{n}!", "=", factorial(n))