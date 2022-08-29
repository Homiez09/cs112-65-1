def fibo(n):
    a = 1
    b = 1
    i = 3
    c = 0
    if n == 1 or n == 2:
        return 1
    while i <= n:
        c = a + b
        a = b
        b = c
        i += 1
    return c
n = int(input("Enter n: "))
print("fibo({0}) = {1}".format(n, fibo(n)))