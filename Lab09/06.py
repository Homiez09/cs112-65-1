def alternating_sum(n):
    i = 1
    total = 0
    while i <= n:
        if i % 2 == 0:
            total -= i
        else:
            total += i
        i += 1
    return total 

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, alternating_sum(n)))