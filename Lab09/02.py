def factor_count(n):
    i = 1
    count = 0
    while i < n + 1:
        if n % i == 0:
            count += 1
        i += 1
    return count
n = int(input("Enter n: "))
c = factor_count(n)
print(c)