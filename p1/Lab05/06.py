n = int(input())
ans = 0

if n % 9 == 0:
    while True:
        if n == 0:
            break
        ans += n%10
        n -= n%10
        n = n//10
    print("Yes", int(ans))
else:
    print("No", n%9)