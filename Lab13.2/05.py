def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c

n = int(input())
mode = input()

if n >= 0:
    if mode.lower() == 'e':
        print(sum([fibonacci(i) for i in range(0, n+1, 2)]))
    elif mode.lower() == 'o':
        print(sum([fibonacci(i) for i in range(1, n+1, 2)]))
    else:
        print("ERROR")
else:
    print("ERROR")