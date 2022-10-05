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

n = input()
mode = input()

if n == '':
    print("ERROR")
else:
    n = int(n)
    if n >= 0:
        if mode.lower() == 'e':
            print(sum([fibonacci(i) for i in range(0, n+1, 2)]))
        elif mode.lower() == 'o':
            print(sum([fibonacci(i) for i in range(1, n+1, 2)]) if n != 0 else "ERROR")
        else:
            print("ERROR")
    else:
        print("ERROR")