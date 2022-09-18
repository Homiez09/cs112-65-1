a = int(input())
b = int(input())
c = int(input())

if (a > 0 and b > 0 and c > 0):
    if c > a and c > b:
        print(a**2 + b**2 == c**2)
    elif b > a and b > c: 
        print(a**2 + c**2 == b**2)
    else:
        print(b**2 + c**2 == a**2)