n = 1234

t1 = n % 10
t2 = n // 10 % 10
t3 = n // 100 % 10
t4 = n // 1000 % 10

j = 10


for i in range(4):
    print(n//j %10)
    j *= 10

print(t1, t2, t3, t4)