def sqrt_n_times(x, n):
    x = x
    while n > 0:
        x = x**(1/2)
        n -= 1
    return x

x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )

